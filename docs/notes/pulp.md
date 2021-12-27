# PuLP

<small>12/08/2019</small>

## Taxonomy and general approach

PuLP is a Python library for linear programming written in a _pythonic_ way.

### Linear, Integer and Mixed-integer programming

For a mathematical program to be a **linear program** you need the following conditions to be true:

- the decision variables must be real variables
- the objective must be a linear expression (wrt. the decision variables)
- the constraints must be linear expressions (wrt. the decision variables)

An **integer program** is a linear program in which all the decision variables need to have only integer values. Since most integer programs contain a mix of continuous variables and integer variables they are often known as **mixed integer programs**.

!!! note
    Integer programs can be very difficult problems to solve and there is a lot of current research finding “good” ways to solve integer programs. Integer programs can be solved using the branch-and-bound process.
    For MIPs of any reasonable size the solution time grows exponentially as the number of integer variables increases.

### The Optimisation Process

<small>source: [PuLP docs](https://coin-or.github.io/pulp/main/the_optimisation_process.html)</small>

1. Getting the problem description
2. Formulating the (equivalent) mathematical program

    - _Identify the Decision Variables_ paying particular attention to units
    - _Formulate the Objective Function_ using the decision variables, we can construct a minimise or maximise objective function. The objective function typically reflects the total cost, or total profit, for a given value of the decision variables
    - _Formulate the Constraints_, either logical or explicit to the problem description. Again, the constraints are expressed in terms of the decision variables.
    - _Identify the Data_ needed for the objective function and constraints. To solve your mathematical program you will need to have some "hard numbers" as variable bounds and/or variable coefficients in your objective function and/or constraints

3. Solving the mathematical program

4. Performing some post-optimal analysis
    - how the optimal solution would change under various changes to the formulation?
    - what the solution’s variable values mean in terms of the original problem description?

## PuLP syntax

### Variables definition

To define a set of variables we can declare a dictionary through `LpVariable.dicts(var_name, var_index, lowBound, upBound, cat)`
where:

- _var_name_ is a string containing the name of the variable
- _var_index_ contains the indices on which variables will be indexed (and will be used to set keys of the dictionary)
- _lowBound_ is the lower bound of the domain of the variables
- _upBound_ is the upper bound of the domain of the variables
- _cat_ is the category of the variable (Integer, Binary or Continuous)

**Example**

To define an 10x1 array of binary variables $x$ we can declare

```python
x = LpVariable.dicts(
    'my_binary_array', 
    range(10), 
    lowBound=0, 
    upBound=1, 
    cat='Binary'
    )
```

To define $X$ as a 5x4 matrix of integer variables $x_{ij}$ such that $0\leq x_{ij}\leq 7$ we can declare

```python
X = LpVariable.dicts(
    'my_integer_matrix', 
    [(i, j) for i in range(5) for j in range(4)], 
    lowBound=0, 
    upBound=7, 
    cat='Integer'
    )
```

### Problem definition

To define an instance of a given problem we first need to initialize it through `problem = LpProblem(problem_name, problem_sense)` where:

- _problem_name_ is a string containing the name of the problem
- _problem_sense_ can be either LpMinimize (default) or LpMaximize

**Example**

To define a minimization problem, we can declare

```python
my_problem = LpProblem("The most difficult problem ever", LpMinimize)
```

To add the objective function into the defined instance, we can use the following syntax `problem += objective_function, objective_function_desc`
where:

- _objective_function_ is the objective function expressed in terms of decision variables and possibly through the use of PuLP built in classes like `lpSum` and/or `LpAffineExpression`
- _objective_function_desc_ is a string containing the description of the objective function to be minimized/maximized

**Example**

To add the (possible) function to be minimized $\sum_{i\in I}a_ix_i$ to our problem we can set

```python
my_problem += lpSum([a[i]*x[i] for i in my_indices]),\
"minimized this affine expression with coefficients a_i and variables x_i"
```

### Constraints

For our problem to be completely defined we must add also the constraints related to the initialized instance using `problem += constraint, constraint_desc`
where:

- _constraint_ is the expression which implements the constraint to be added possibly via the usage of the built-in class `LpConstraint`
- _constraint_desc_ is a string containing the description of the constraint

**Example**

To add to our problem a constraint in the form $\sum_{i\in I}x_i\leq b$ we can set

```python
my_problem += lpSum([x[i] for i in my_indices]) <= b
```

### Solution & debug

To write a (verbose) file with the complete representation of the given problem, we can use `problem.writeLP("problem_name.lp")`. Similarly, to solve the problem and obtain a log with the trace of the optimization process we can use the following code:

```python
my_problem.writeLP("my_problem_name.lp")

from os import dup, dup2, close

logf = open('./optimization_log.txt', 'w')
orig_std_out = dup(1)
dup2(logf.fileno(), 1)

my_problem.solve(pulp.PULP_CBC_CMD(maxSeconds=90, msg=True)) 

dup2(orig_std_out, 1)
close(orig_std_out)
logf.close()
```

where `problem.solve(pulp.PULP_CBC_CMD(maxSeconds=max_seconds, msg=True))` corresponds to the actual call for the solution of the problem, where the default back-end solver has been called with the `msg` keyword set to True (to actually produce the output log) and the `maxSeconds` keyword set to 90 seconds to limit the calculation time.

After the resolution, the objective function value can be obtained by calling:

```python
my_problem.objective.value()
```

In a similar way, we can then check the value(s) assumed by the various decision variables by calling for example:

```python
for i in my_indices:
    print(x[i].value())
```

To check the status of the problem, both before and after the resolution process, we can use:

```python
LpStatus[my_problem.status]
```

which passes to the built-in dictionary `LpStatus` the actual problem status, which can assume one of the following value: Optimal, Not Solved, Infeasible, Unbounded, Undefined.

## Tips & Tricks

### Dummy is good

After the (mathematical) formulation of the problem and the related PuLP implementation, it's _very_ useful to test the program over several dummy input datasets of growing complexity having a known ground-truth. This helps to identify possible implementation mistakes and/or to unveil limitations in the theoretical formulation.

In doing this, the creation of auxiliary data structures to store decision variables output values is often very useful to not get lost within the (possibly) counterintuitive formulation of the problem (see tip below). The following two functions might be useful in monitor variables values:

```python
def print_variable_values(LpVariable, exception=0):
    
    '''
    this function can be used to print the values of a given LpVariable
    which do not equal the exception value (default=0)
    
    INPUT
    LpVariable (dict) --> an LpVariable defined through the related PuLP class
    exception --> the exception value that will cause the variable value not to be printed
    '''
    
    for key in LpVariable:
        value = LpVariable.get(key).value()
        if value != exception:
            print(key,':',value) 
    return

def filter_variable_values(LpVariable, exception=0):
    
    '''
    this function can be used to filter the values of a given LpVariable
    which do not equal the exception value (default=0)
    
    INPUT
    LpVariable (dict) --> an LpVariable defined through the related PuLP class
    exception --> the exception value that will cause the variable value to be filtered out
    
    OUTPUT
    filtered_values (dict) --> a filtered dictionary which contains only the values of the given variable which do not equal the exception value
    '''
    
    filtered_values = {}
    for key in LpVariable:
        value = LpVariable.get(key).value()
        if value != exception:
            filtered_values[key] = value 
    return filtered_values
```

### Change the point of view

The most straightforward implementation of a given minimization (resp. maximization) problem might sometimes involve a non-linear function of the decision variables. For example, we can think about a bin-packing problem in which the cost to be minimized depends in a non-linear way on the number of items contained in each bin. In a more detailed way, we are referring to the problem

$\min\limits_{x}\sum\limits_{j\in\text{bins}} c\left(\sum\limits_{i\in\text{items}}x_{ij}\right)$

being $c(\cdot)$ a non-linear function and $x_{ij}$ a binary variable which indicates if the item $i$ belongs to the bin $j$.

In such occasions, the linearity of the problem can be "manually" restored with the introduction of indicator variables defined over the possible values assumed by the above summation. Given for example that $\sum_{i\in\text{items}}x_{ij}\in\{0,\dots,N\}$, the problem can be written as

$\min \sum\limits_{j\in\text{bins}}\sum\limits_{n=0}^Nc(n)y_{nj}$

where $y_{nj}$ is a binary variable such that

$y_{nj}=1\Leftrightarrow \sum\limits_{i\in\text{items}}x_{ij}=n$

subject to the following constraint

$\sum\limits_{n=0}^Ny_{nj}=1\;\forall j\in\text{bins}$

### The more the better

In the first PuLP implementation, I found useful to write "more" constraints (even if redundant) rather than "less". This forced me to carefully reason about relations between decision variables during the formulation phase, as well as to be sure that I had implemented all the constraints required without missing any (even if in two or more different ways each).

### LaTeX is your friend

Before the implementation phase I found extremely useful to write down the full problem formulation in a clean and clear way (for example, with usage of $\LaTeX$ within Jupyter notebook markdown cells). Again, this forced me to be really sure about the theoretical framework of the problem, making clear all the assumptions and the modelization choices I have made. Moreover, this habit really helps the implementation serving as a to-do-list in terms of constraints to be added within the PuLP problem.

In doing so, I strongly recommend to use a coherent indexing and notation between the theory (markdown cells) and the practice (PuLP code), to avoid transliteration mistakes and help your [System 1](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow) in doing its job.

### Linearize, linearize, linearize

If you desire (or must) stick to PuLP, you want every non-linear part of your formulation to disappear. In doing so, be confident and optimistic that many non-linear formulations can be properly linearized! For example:

- linearize [a product](https://orinanobworld.blogspot.com/2010/10/binary-variables-and-quadratic-terms.html) between a binary variable and a bounded one
- linearize [a logical implication or an equivalence](https://orinanobworld.blogspot.com/2012/05/indicator-implies-relation.html)

In a similar way, you can bypass some PuLP limitations in the implementation. For example:

- to implement **absolute values** (refused by PuLP by default through a raise Error) you can refer to [this](https://stackoverflow.com/questions/51721618/python-pulp-absolute-constraints) as well as [this](https://orinanobworld.blogspot.com/2012/07/modeling-absolute-values.html)
- to implement **strict inequalities** (refused by PuLP by default through a raise Error), if the involved variables can assume only integer values you can follow [this tip](https://stackoverflow.com/questions/50243278/error-disallowing-the-optimal-solution-using-python-pulp).

## Resources

### General

- [PuLP official docs](https://pythonhosted.org/PuLP/)
- [introductive paper by Stuart Mitchell et al.](https://tinyurl.com/y6klce2e)
- [quadratic terms linearization](https://orinanobworld.blogspot.com/2010/10/binary-variables-and-quadratic-terms.html)
- [blog with tutorials, explanations and tips & tricks](http://benalexkeen.com/linear-programming-with-python-and-pulp/)
- [logical implication and equivalence linearization](https://orinanobworld.blogspot.com/2012/05/indicator-implies-relation.html)
- [logical implication and equivalence linearization](https://cs.stackexchange.com/questions/71091/express-a-complex-if-statement-to-linear-programming)
- [lecture notes MIP UniRoma](http://www.dis.uniroma1.it/~or/meccanica/cap12.pdf)
- [lecture notes UniPD operations research and branch-and-bound method](https://www.math.unipd.it/~luigi/courses/ricop/m04.BeB.01.pdf)
- [lecture notes MIP UniPD](http://www.dei.unipd.it/~salvagni/didattica/mip.pdf)

### Bin packing related

- [paper with an implementation which exploits items fragmentation](https://hal.archives-ouvertes.fr/hal-00780434/document)
- [bin packing chapter in the online book Mathematica Optimization: Solving Problems using SCIP and Python](https://scipbook.readthedocs.io/en/latest/bpp.html)
- [introductive LinkedIn post](https://www.linkedin.com/pulse/bin-packing-python-pulp-michael-basilyan)

### Scheduling related

- [post about workers scheduling to minimize cost of shifts](https://towardsdatascience.com/scheduling-with-ease-cost-optimization-tutorial-for-python-c05a5910ee0d)
- [slides about optimal scheduling with PuLP](https://ep2017.europython.eu/media/conference/slides/automatic-conference-scheduling-with-pulp.pdf)
- [paper about Nurse Scheduling Problem](https://www.sciencedirect.com/science/article/pii/S111001681730282X)
- [post about conferences scheduling with PuLP](https://vknight.org/unpeudemath/mathematics/2017/03/01/Scheduling-class-presentations-using-pulp.html)
- [post about Bus Driver Scheduling Problem](https://blog.remix.com/an-intro-to-integer-programming-for-engineers-simplified-bus-scheduling-bd3d64895e92)

## CBC optimal status

I discover that CBC solver used via PuLP sometimes exits with `OPTIMAL` status even if the actual cause is the given time limit: this lead to an incoherent solver status with a globally non-optimum solution.

Below some possible explanations.

Following [this issue](https://github.com/coin-or/pulp/issues/164), one of PuLP authors (at least [from v2.1 on](https://github.com/coin-or/pulp/releases)) states:

> In the case of GUROBI and CPLEX solvers (at least in the CMD interface), pulp returns 1 ('optimal') when an integer solution has been found in the time limit.
>
> This is not the behavior I get from the CBC solver, which returns 0 ['not solved', ndr].
>
> Since having found an integer solution when the time stops is neither "optimal" nor "not solved", both are at the same time misleading and inconsistent.
>
> One possibility is to at least make all solvers return the same status when finishing in the same status. This would make CBC return 1 instead of 0 when at least one integer > solution was found. This is easy to change.
>
> The second, more ambitious possibility, would be to create a new "Integer solution" status in pulp that differentiates from "optimal" and "no solution". This would then be used in the solver interfaces as an additional status to return.

A double check on [PuLP constants](https://github.com/coin-or/pulp/blob/master/pulp/constants.py) confirms that:

- exists a dictionary of PuLP problem statuses with values in `[Not Solved, Optimal, Infeasible, Unbounded, Undefined]`
- exists a dictionary of PuLP solution statuses with values in `[No Solution Found, Optimal Solution Found, Solution Found, No Solution Exists, Solution is Unbounded]`
- `LpSolutionIntegerFeasible = 2` has been mapped to solution status `Solution Found` but it's not the map value for any problem status in `LpStatusToSolution`

Looking into the source code of [PuLP interface to CBC](https://github.com/coin-or/pulp/blob/master/pulp/apis/coin_api.py#L300), we can check the `get_status` function definition:
  
```python
def get_status(self, filename):
    cbcStatus = {
        "Optimal": constants.LpStatusOptimal,
        "Infeasible": constants.LpStatusInfeasible,
        "Integer": constants.LpStatusInfeasible,
        "Unbounded": constants.LpStatusUnbounded,
        "Stopped": constants.LpStatusNotSolved,
    }

    cbcSolStatus = {
        "Optimal": constants.LpSolutionOptimal,
        "Infeasible": constants.LpSolutionInfeasible,
        "Unbounded": constants.LpSolutionUnbounded,
        "Stopped": constants.LpSolutionNoSolutionFound,
    }

    with open(filename) as f:
        statusstrs = f.readline().split()

    status = cbcStatus.get(statusstrs[0], constants.LpStatusUndefined)
    sol_status = cbcSolStatus.get(
        statusstrs[0], constants.LpSolutionNoSolutionFound
    )
    # here we could use some regex expression.
    # Not sure what's more desirable
    if status == constants.LpStatusNotSolved and len(statusstrs) >= 5:
        if statusstrs[4] == "objective":
            status = constants.LpStatusOptimal
            sol_status = constants.LpSolutionIntegerFeasible
    return status, sol_status
```

In one of the last lines we can clearly see that if the problem status is `LpStatusNotSolved`, the same is reassigned to `LpSolutionOptimal` but solution status is not (it is override with `LpSolutionIntegerFeasible`).
