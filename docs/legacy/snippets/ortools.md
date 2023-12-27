# ortools

## `get_solver`

```python
"""Utils for ortools-based classes."""

from ortools.linear_solver import pywraplp

_solvers = dict(
    SCIP=pywraplp.Solver.SCIP_MIXED_INTEGER_PROGRAMMING,
    CBC=pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING,
    SAT=pywraplp.Solver.SAT_INTEGER_PROGRAMMING
    )


def get_solver(solver: str) -> int:
    """Initialize OR-Tools problem.

    SEE: For reference on solvers performance see [here](https://github.com/google/or-tools/issues/1522)

    Available solvers:

    - 'SCIP' (`SCIP_MIXED_INTEGER_PROGRAMMING`), 
        recommended solver in [source code](https://github.com/google/or-tools/blob/v8.0/ortools/linear_solver/linear_solver.h#L194) 
        at line 194, but free only for academic purpose (see https://www.scipopt.org/index.php#license)
    - 'CBC' (`CBC_MIXED_INTEGER_PROGRAMMING`), solves MIP problem - beware that timeout _can be_ ignored, see for reference:
        - https://stackoverflow.com/questions/63130482/how-to-combine-time-and-gap-limits-with-google-or-tools-in-python
        - https://groups.google.com/g/or-tools-discuss/c/iWz16p6q680
        - https://github.com/google/or-tools/issues/1006
        - https://developers.google.com/optimization/reference/python/linear_solver/pywraplp
        - https://github.com/google/or-tools/issues/644
        - https://github.com/google/or-tools/issues/603
    - 'SAT' (`SAT_INTEGER_PROGRAMMING`), autoscales coefficients to integers and applies Boolean satisfiability test to solve IP problem
        seems best on already integers objective functions (e.g. bin packing). 
        Implements [CDCL algorithm](https://en.wikipedia.org/wiki/Conflict-driven_clause_learning).    

    Other evaluated solvers:

    - 'BOP' (`BOP_INTEGER_PROGRAMMING`), requires only integer variables and works best with only Boolean variables.
        In case of not integer variables, returns problem status ABNORMAL. Does not seem to respect time limit.
    - `CP_SAT`, requires refactoring of API and only integer coefficients (which must be explicitly scaled beforehand)
    - `GLPK_MIXED_INTEGER_PROGRAMMING`, not tested because not installed 
        (caused jupyter kernel death on Windows, see https://developers.google.com/optimization/install/cpp/source_linux#optional_third_party)
    - `CLP_LINEAR_PROGRAMMING`, linear solver which ignores boolean variables declaration
    - `GLOP_LINEAR_PROGRAMMING`, linear solver which ignores boolean variables declaration
    """    
    return _solvers[solver]
```

## `BaseProblem`

```python
import datetime
import multiprocessing
import os
from abc import ABC, abstractmethod
from typing import Optional

from loguru import logger
from ortools.linear_solver import pywraplp
from ... import get_solver


class BaseProblem(pywraplp.Solver, ABC):
    """Implement generic OR problem via ortools."""

    def __init__(
        self,
        solver: str,
        sense: str,
        relaxable: bool,
        time_limit: Optional[int]
        ) -> None:
        """Initialize class and set params.

        Args:
            solver (str): solver name.
            sense (str): optimization sense.
            relaxable (bool): indicate whether the problem can be relaxed via slack variables.
            time_limit (Optional[int]): possible timeout for solution computation.
        """
        super().__init__(
            name=self.__class__.__name__,
            problem_type=get_solver(solver=solver),
            )
        if time_limit:
            self.set_time_limit(int(time_limit) * 1_000)  # time limit converted to milliseconds
            logger.info(f"Solver time limit set to {time_limit} seconds.")

        _n_threads = multiprocessing.cpu_count()
        self.SetNumThreads(_n_threads)
        logger.info(f"All {_n_threads} CPU available to solver.")
        self._set_status_names()
        self.sense = sense
        self.relaxable = relaxable

    def _set_status_names(self) -> None:
        """Set solver status names."""
        # SEE: For reference see [here](https://github.com/google/or-tools/blob/v8.0/ortools/linear_solver/linear_solver.h#L1674) -@A00018578 at 21/1/2021, 12:02:15
        self.status_names = {
            # optimal.
            self.OPTIMAL: 'OPTIMAL',
            # feasible, or stopped by limit.
            self.FEASIBLE: 'FEASIBLE',
            # proven infeasible.
            self.INFEASIBLE: 'INFEASIBLE',
            # proven unbounded.
            self.UNBOUNDED: 'UNBOUNDED',
            # abnormal, i.e., error of some kind.
            self.ABNORMAL: 'ABNORMAL',
            # the model is trivially invalid (NaN coefficients, etc).
            5: 'MODEL_INVALID', # apparentemente rimosso da pywraplp, lo mettiamo per sicurezza
            # not been solved yet.
            self.NOT_SOLVED: 'NOT_SOLVED'
        }
        self.status_whitelist = (self.OPTIMAL, self.FEASIBLE)

    @abstractmethod
    def set_variables(self) -> None:
        """Set problem decision variables."""
        pass

    @abstractmethod
    def set_slack_variables(self) -> None:
        """Set slack variables."""
        pass

    @abstractmethod
    def set_slack_penalty(self) -> None:
        """Set penalty factor for slack variables."""
        pass

    @abstractmethod
    def set_objective(self) -> None:
        """Set problem objective **[abstract method]**."""
        pass

    @abstractmethod
    def set_constraints(self) -> None:
        """Set problem constraints **[abstract method]**."""
        pass

    @abstractmethod
    def build_objective_terms(self) -> None:
        """Build objective function terms **[abstract method]**."""
        pass

    def _set_variables(self) -> None:
        """Set decision variables."""
        if self.relaxable:
            self.set_slack_variables()
        self.set_variables()

    def _set_optimization_sense(self) -> None:
        """Set problem optimization sense."""
        if self.sense == 'min':
            self.Minimize(self.objective)
        elif self.sense == 'max':
            self.Maximize(self.objective)

    def _scale_slack(self, var: pywraplp.Solver.Var) -> pywraplp.Solver.Var:
        """Scale slack variable.

        Args:
            var (pywraplp.Solver.Var): input variable.

        Returns:
            Scaled variable.
        """
        if hasattr(self, 'slack_range'):
            return (var - var.lb())/(var.ub() - var.lb()) * (self.slack_range[1] - self.slack_range[0]) + self.slack_range[0]
        else:
            return var

    def _set_slack_range(self, slack_range: tuple = (1, 2)) -> None:
        """Set scaled slacks range.

        Args:
            slack_range (tuple, optional): Min and max for scaled slacks. Defaults to (1, 2).
        """
        self.slack_range = slack_range

    def _build_slack_terms(self, scaled: bool = True) -> list:
        """Build objective function slack terms.

        Each slack contributes with:
        
        - a positive addend, if problem sense is minimization;
        - a negative addend, if problem sense is maximization.

        Returns:
            List of slack terms.
        """
        if self.relaxable:
            self.set_slack_penalty()
            if scaled:
                self._set_slack_range()
            if self.sense == 'min':
                return [self.slack_penalty * self._scale_slack(var) for var in self.slack.values()]
            elif self.sense == 'max':
                return [-self.slack_penalty * self._scale_slack(var) for var in self.slack.values()]
        else:
            return []

    @timed
    def _build(self) -> None:
        """Build problem."""
        self._set_variables()
        self.set_objective()
        self._set_optimization_sense()
        self.set_constraints()

        # self.SetHint(self.variables(), list(map(lambda x: x.lb(), self.variables())))
        
        # # SEE SAT solver parameters https://github.com/google/or-tools/blob/stable/ortools/sat/sat_parameters.proto
        # outcome = self.SetSolverSpecificParametersAsString('random_seed:0')
        # logger.info(f'random_seed has been set to 0: {outcome}.')
        # outcome = self.SetSolverSpecificParametersAsString('randomize_search:false')
        # logger.info(f'randomize_search has been set to false: {outcome}.')
        # outcome = self.SetSolverSpecificParametersAsString('permute_variable_randomly:false')
        # logger.info(f'permute_variable_randomly has been set to false: {outcome}.')
        # outcome = self.SetSolverSpecificParametersAsString('permute_presolve_constraint_order:false')
        # logger.info(f'permute_presolve_constraint_order has been set to false: {outcome}.')
        # outcome = self.SetSolverSpecificParametersAsString('use_absl_random:false')
        # logger.info(f'use_absl_random has been set to false: {outcome}.')      
                 

    @timed
    def _solve(self, export_model: bool, artifacts_path: str) -> None:
        """Solve OR-Tools problem.

        Args:
            export_model (bool): Controls whether or not problem in LP format must be exported.
            artifacts_path (str): Path in which resolution logs must be stored.
        """
        self.EnableOutput()
        if export_model:
            now = str(datetime.datetime.now())[:19].replace('-', '_').replace(' ', '_').replace(':', '_')
            if not os.path.exists(artifacts_path):
                os.makedirs(artifacts_path)
            with open(f'{artifacts_path}/{now}_{self.__class__.__name__}.txt', 'w') as f:
                f.write(self.ExportModelAsLpFormat(False).replace('\\', '').replace(',_', ','))

        self.status = self.Solve()
        logger.info(f"Problem status: {self.status_names[self.status]}")
```

## `Problem`

```python
from typing import Optional

from loguru import logger
from ... import BaseProblem


class Problem(BaseProblem):
    """Extend BaseProblem class to implement concrete problem."""

    def __init__(
        self,
        solver: str,
        sense: str,
        relaxable: bool,
        time_limit: Optional[int],
        **kwargs
        ) -> None:
        """Initialize class and feed params to BaseProblem.

        Args:
            solver (str): solver name.
            sense (str): problem optimization sense.
            relaxable (bool): indicate whether or not the problem can be relaxed.
            time_limit (Optional[int]): possible timeout for solution computation.
        """
        super().__init__(
            solver=solver,
            sense=sense,
            relaxable=relaxable,
            time_limit=time_limit
            )
        self.set_params(**kwargs)

    def set_params(self, **params) -> None:
        """Set the parameters of this problem."""
        for key, value in params.items():
            setattr(self, key, value)

    def fit(self) -> None:
        """Fit problem with data."""
        ...

    def fit_and_solve(self) -> Optional[dict]:
        """Implement a wrapper to sequentially recall fit() and solve() methods.

        Returns:
            Computed solution.
        """
        self.fit()
        return self.solve()
               

    def set_variables(self) -> None:
        """Initialize decision variables."""
        ...

    def set_slack_variables(self) -> None:
        """Set problem slack variables."""
        ...

    def set_constraints(self) -> None:
        """Set all constraints."""
        ...

    @timed
    def set_objective(self) -> None:
        """Set problem objective function as sum of objective and slack terms."""
        self.objective = self.Sum(
            self.build_objective_terms() +
            self._build_slack_terms()
            )

    def solve(
        self,
        export_model: bool = False,
        artifacts_path: str = "./.ortools_artifacts"
        ) -> Optional[dict]:
        """Solve problem and retrieve solution.

        Args:
            export_model (bool, optional): Controls whether or not problem in LP format must be exported. Defaults to False.
            artifacts_path (str, optional): Path in which resolution logs must be stored. Defaults to './ortools_artifacts'.
        """
        # Build and solve
        self._build()
        self._solve(export_model=export_model, artifacts_path=artifacts_path)
        
        # Postprocess solution
        ...

        # Add activated slack to logs as warnings
        if self.relaxable:
            for name, slack in self.slack.items():
                if slack.solution_value() != 0.0:
                    logger.debug(f"Constraint {name[0]} for {name[1]} violated with slack value {slack.solution_value()} [scaled to {self._scale_slack(slack).solution_value()}].")

        if self.status in self.status_whitelist:
            return ...
```

### `Location-Allocation`

```python
from ortools.linear_solver.linear_solver_natural_api import ProductCst
from ... import Problem
self = Problem(...)


def set_assignment_constraints(self) -> None:
    """Add assignment constraints which ensure location-allocation coherency."""
    for i in self.customers:
        self.Add(
            self.Sum(
                [self.X[i, j] for j in self.y]) == 1,
                f"Customer {i} must be allocated to exactly one facility."
                )

    for i, j in self.X.keys():
        self.Add(
            self.X[i, j] <= self.y[j],
            f"If facility {j} is not open, customer {i} cannot be allocated to it."
            )

    for j in self.facility_candidates:
        self.Add(
            self.Sum([self.X[i, j] for i in self.customers]) >= self.y[j],
            f"If facility {j} is open, at least one customer must be allocated to it."
        )

def set_n_facilities_constraint(self) -> None:
    """Add constraint on number of facilities to locate."""
    if getattr(self, 'n_facilities', None):
        self.Add(
            self.Sum([self.y[j] for j in self.facility_candidates]) == self.n_facilities,
            f"Total opened facilities must be exactly {self.n_facilities}.")

def set_max_facilities_constraint(self):
    """Add constraint to limit max number of facilities."""
    if getattr(self, 'max_n_facilities', None):
        self.Add(
            self.Sum([self.y[j] for j in self.facility_candidates]) <= self.max_n_facilities,
            f"Total opened facilities must be at most {self.max_n_facilities}.")

def set_required_facilities_constraint(self):
    """Add constraint to set required facilities."""
    for j in self.required_facilities:
        self.Add(
            self.y[j] == 1,
            f"Facility {j} must be used."
        )

def _build_minisum(self, i: str, j: str) -> ProductCst:
    return (
        self.distance_matrix.loc[i, j] *
        self.X[i, j] *
        self.customers.loc[i, self.weight]
    )

def _build_minisum_penalty(self) -> float:
    return (
        self.distance_matrix.max().max() *
        len(self.X) *
        self.customers.loc[:, self.weight].max()
    )

def locate_facilities(self) -> None:
    """Locate facilities after problem resolution."""
    if self.status in self.status_whitelist:
        self.located_facilities = list(
            j for j in self.y
            if self.y[j].solution_value() == 1
            )

def allocate_customers(self) -> None:
    """Retrieve allocations after problem resolution."""
    if self.status in self.status_whitelist:
        self.allocations = dict(
            (i, j) for i, j in self.X
            if self.X[i, j].solution_value() == 1
            )

def build_objective_terms(self) -> list:
    """Build problem objective function terms.

    Following [ortools docs](https://developers.google.com/optimization/assignment/assignment_example#create_the_objective_function),
    objective function is created as a sum of terms.

    Returns:
        Obective function terms.
    """
    objective_terms = []
    for i, j in self.X.keys():
        objective_terms.append(self._build_minisum(i, j))
    return objective_terms

@timed
def set_constraints(self) -> None:
    """Add constraints to OR-Tools problem."""
    self.set_assignment_constraints()
    self.set_n_facilities_constraint()
    self.set_max_facilities_constraint()
    self.set_required_facilities_constraint()
    ...
```

### Capacitated Vehicle Routing

```python
from typing import Optional

import networkx as nx
import pandas as pd
from ... import BaseProblem
from ... import BinPacking


class CVRP(BaseProblem):
    """Extend BaseProblem class to implement custom CVRP problem."""

    def __init__(
        self,
        solver: str,
        sense: str,
        relaxable: bool,
        time_limit: Optional[int],
        **kwargs
        ) -> None:
        """Initialize class and feed params to BaseProblem.

        Args:
            solver (str): solver name.
            sense (str): problem optimization sense.
            relaxable (bool): indicate whether or not the problem can be relaxed.
            time_limit (Optional[int]): possible timeout for solution computation.
        """
        super().__init__(
            solver=solver,
            sense=sense,
            relaxable=relaxable,
            time_limit=time_limit
            )
        self.set_params(**kwargs)

    def set_params(self, **params) -> None:
        """Set the parameters of this model."""
        for key, value in params.items():
            setattr(self, key, value)

    def fit(self, data: ...) -> None:
        """Fit problem with data."""
        n_vehicles = self.compute_n_vehicles(self.data)
        self.vehicles = pd.DataFrame(...)
        self.locations = pd.DataFrame(...)
        self.distance_matrix = pd.DataFrame(...)
        self.vehicle_shift_duration = ...
        self.vehicle_speed = ...

    def compute_n_vehicles(self, data: ...) -> int:
        """Compute minimum number of vehicles via bin packing.

        Args:
            data (...): CVRP data.

        Returns:
            Minimum number of vehicles.
        """
        options = dict(
            solver='SAT',
            sense='min',
            relaxable=False,
            time_limit=30.0
            )
        bp = BinPacking(**options)
        logger.info("Solving BinPacking problem to optimize available vehicles...")
        return bp.fit_and_solve(data)        

    def set_variables(self) -> None:
        """Set problem variables."""
        # Transit variables
        self.X = {
            (k, i, j): self.BoolVar(f"{k}_transit_from_{i}_to_{j}")
            for k in self.vehicles.index
            for i in self.locations.index
            for j in self.locations.index
            if i != j
            }
        # Allocation variables
        self.y = {
            (i, k): self.BoolVar(f"{i}_collected_by_{k}")
            for k in self.vehicles.index
            for i in self.locations.index
        }
        # Load variables (auxiliary)
        self.u = {
            (i, k): self.Var(
                    name=f"load_of_{k}_after_visit_{i}",
                    lb=float(self.locations.loc[i, 'weight']),
                    ub=float(self.vehicles.loc[k, 'capacity']),
                    integer=True
                    )
            for k in self.vehicles.index
            for i in self.locations.index.drop('depot')
        }

    def set_slack_variables(self) -> None:
        ...        

    @timed
    def set_objective(self) -> None:
        """Set problem objective."""
        self.objective = self.Sum(self.build_objective_terms())

    def set_assignment_constraints(self) -> None:
        """Set assignment constraints to ensure route coherence."""
        for i in self.locations.index.drop(['depot', 'dump']):
            self.Add(
                self.Sum([self.y[(i, k)] for k in self.vehicles.index]) == 1,
                f"Location {i} must be visited by exactly one vehicle."
                )

        self.Add(
            self.Sum([self.y[('depot', k)] for k in self.vehicles.index]) <= len(self.vehicles),
            f"All vehicles must visit depot. Up to {len(self.vehicles)} can be used."
        )

    def set_flow_conservation_constraints(self) -> None:
        """Set flow conservation constraints.
        
        Each vehicle must enter to and exit from each node exactly once.
        """
        for i in self.locations.index:
            for k in self.vehicles.index:
                self.Add(
                    self.Sum([self.X[(k, i, j)] for j in self.locations.index if j != i]) == self.y[(i, k)],
                    f"If {k} visits location {i}, then exactly one edge starting from {i} must be traversed from {k}."
                    )

        for i in self.locations.index:
            for k in self.vehicles.index:
                self.Add(
                    self.Sum([self.X[(k, j, i)] for j in self.locations.index if j != i]) == self.y[(i, k)],
                    f"If {k} visits location {i}, then exactly one edge ending in {i} must be traversed from {k}."
                    )

    def set_subtour_elimination_contraints(self) -> None:
        """Set subtour elimination constraints.
        
        SEE:         
        - [subtours example](https://docs.python-mip.com/en/latest/examples.html#the-traveling-salesman-problem)
        - [MTZ conditions for 3-indices model](https://i.stack.imgur.com/ewjuD.png)
        
        """
        for k in self.vehicles.index:
            for i in self.locations.index.drop('depot'):
                for j in self.locations.index.drop('depot'):
                    if (i != j) and (self.locations.loc[i, 'weight'] + self.locations.loc[j, 'weight'] <= self.vehicles.loc[k, 'capacity']):
                        self.Add(
                            self.u[(i, k)] - self.u[(j, k)] + self.vehicles.loc[k, 'capacity'] * self.X[(k, i, j)] <= self.vehicles.loc[k, 'capacity'] - self.locations.loc[j, 'weight'],
                            f"Subtour elimination (A) for {k}, {i} and {j}"
                        )
                        self.Add(
                            self.u[(j, k)] - self.u[(i, k)] + self.vehicles.loc[k, 'capacity'] * self.X[(k, i, j)] <= self.vehicles.loc[k, 'capacity'] + self.locations.loc[j, 'weight'],
                            f"Subtour elimination (B) for {k}, {i} and {j}"
                        )

                self.Add(
                    self.u[(i, k)] - self.locations.loc[i, 'weight'] <= self.vehicles.loc[k, 'capacity'] * (1 - self.X[(k, 'depot', i)]),
                    f"If X({k}, depot, {i}) = 1, then u({i},{k}) = d({i}), Linearization 1"
                )

                self.Add(
                    self.locations.loc[i, 'weight'] - self.u[(i, k)] <= self.vehicles.loc[k, 'capacity'] * (1 - self.X[(k, 'depot', i)]),
                    f"If X({k}, depot, {i}) = 1, then u({i},{k}) = d({i}), Linearization 2"
                )

    def set_capacity_constraints(self) -> None:
        """Set capacity constraints."""
        for k in self.vehicles.index:
            self.Add(
                self.Sum([self.locations.loc[i, 'weight'] * self.y[(i, k)] for i in self.locations.index]) <= self.vehicles.loc[k, 'capacity'],
                f"Capacity constraint for {k}"
            )

    def set_time_constraints(self) -> None:
        """Set time constraints."""
        for k in self.vehicles.index:
            self.Add(
                self.Sum([self.distance_matrix.loc[i, j] * self.X[(k, i, j)] / self.vehicle_speed for i in self.locations.index for j in self.locations.index if i != j]) \
                + self.Sum([self.y[(i, k)] * self.locations.loc[i, 'stop_time'] for i in self.locations.index.drop(['depot', 'dump'])]) <= self.vehicle_shift_duration.seconds,
                f"Route of {k} cannot last more than {self.vehicle_shift_duration}"
            )

    def set_unload_constraints(self) -> None:
        """Set unload constraints."""
        for k in self.vehicles.index:
            self.Add(
                self.X[(k, 'dump', 'depot')] == 1,
                f"{k} must visit dump before depot."
            )            

    @timed
    def set_constraints(self) -> None:
        """Set problem constraints."""
        self.set_assignment_constraints()
        self.set_flow_conservation_constraints()
        self.set_capacity_constraints()
        self.set_subtour_elimination_contraints()
        self.set_time_constraints()
        self.set_unload_constraints()

    def set_slack_penalty(self) -> None:
        ...

    def build_objective_terms(self) -> list:
        """Build objective terms.

        Current problem minimize total travel distance (minisum approach).

        Returns:
            Objective terms.
        """
        objective_terms = []
        for k in self.vehicles.index:
            for i in self.locations.index:
                for j in self.locations.index:
                    if j != i:
                        objective_terms.append(
                            self.distance_matrix.loc[i, j] * self.X[(k, i, j)]
                        )
        return objective_terms

    def _extract_edges(self) -> dict:
        """Extract all route edges from X variables.

        Returns:
            Mapping of vehicles to route as list of edges.
        """
        edges = {}
        if self.status in self.status_whitelist:
            for k in self.vehicles.index:
                edges[k] = list(
                    (i, j)
                    for i in self.locations.index
                    for j in self.locations.index
                    if (i != j) and (self.X[(k, i, j)].solution_value() == 1)
                )
        edges = {vehicle: edgelist for vehicle, edgelist in edges.items() if edgelist and set(edgelist) != set([('depot', 'dump'), ('dump', 'depot')])}
        logger.info(f"Used vehicles: {len(edges)}")
        return edges
    
    def extract_routes(self) -> dict:
        """Reshape routes to list of nodes.

        Returns:
            Mapping of vehicles to route as list of nodes.
        """        
        edges = self._extract_edges()

        routes = {}
        for vehicle, edgelist in edges.items():
            last_location = list(map(lambda x: x[0], filter(lambda x: x[-1] == 'depot', edgelist)))[0]                   
            G = nx.from_edgelist(edgelist, create_using=nx.DiGraph)
            route = nx.shortest_path(G, 'depot', last_location)
            route.append('depot')
            assert len(route) == len(edgelist) + 1, f"Unused edge from edgelist {edgelist} in route {route}."
            routes[vehicle] = route

        return routes

    def solve(
        self,
        verbose: bool = False,
        artifacts_path: str = "./.ortools_artifacts"
        ) -> Optional[dict]:
        """Solve problem and retrieve solution.

        Args:
            verbose (bool, optional): Controls whether or not resolution logs must be saved. Defaults to False.
            artifacts_path (str, optional): Path in which resolution logs must be stored. Defaults to './ortools_artifacts'.
        """
        self._build()
        self._solve(verbose=verbose, artifacts_path=artifacts_path)
        if self.status in self.status_whitelist:
            return self.extract_routes()

    def fit_and_solve(self, data: dict) -> Optional[dict]:
        """Implement a wrapper to sequentially recall fit() and solve() methods.

        Args:
            data (dict): CVRP data.

        Returns:
            Computed solution (if any).
        """
        self.fit(data)
        return self.solve()
```
