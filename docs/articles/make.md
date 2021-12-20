# GNU Make

`make` is a build tool which tracks the dependencies between the
resources it manages, updating the successors whenever a change in one
or more predecessors is detected.

It was originally developed by Stuart Feldman in 1976 as a Bell Labs
summer intern - he then received the 2003 ACM Software System Award for
the authoring of this widespread tool.

The inspiration came from the experience of a coworker of Feldman who
futilely debugged a program where the executable was accidentally not
being updated after bug had been fixed in the source code.

## Makefile

`make` reads and executes instructions contained in files called
Makefile. They essentially store the description of a pipeline, as well
as dependencies among pipeline blocks.

The main concept in Makefile is represented by *rules*. A rule consists
of three components:

- a *target*, the objective of the rule;
- a *recipe*, which consists in a set of actions to be performed to
achieve the target:
- the *dependencies*, which are a list of prerequisites (other
targets) that must be matched before the recipe can be executed.

The syntax to declare a rule is the following

    target: dependencies
        recipe

where, by default, a *tab* stands as prefix of *every recipe line*.

Each target can be then executed by calling ` make  `<target_name>: the
specified dependencies, if any, will be checked - and executed, if
needed - and the recipe will be then executed.

For example, the following Makefile

    hello:
        echo "hello world"

can be executed by calling `make hello`.

### How `make` reads a Makefile

*(paragraph 3.7 of GNU make user manual)*

`make` does its work in two distinct phases.

During the first phase it reads all the makefiles, included makefiles,
etc. and internalizes all the variables and their values and implicit
and explicit rules, and builds a dependency graph of all the targets and
their prerequisites. During the second phase, `make` uses this
internalized data to determine which targets need to be updated and run
the recipes necessary to update them.

It’s important to understand this two-phase approach because it has a
direct impact on how variable and function expansion happens. We say
that expansion is *immediate* if it happens during the first phase:
`make` will expand that part of the construct as the makefile is parsed.
We say that expansion is *deferred* if it is not immediate. Expansion of
a deferred construct part is delayed until the expansion is used: either
when it is referenced in an immediate context, or when it is needed
during the second phase.

## Basics

- you can change the *tab* as default recipe prefix by overriding it
with ` .RECIPEPREFIX =  `<new_char>
- you can break recipe lines with `\`
- by default, the simple execution of `make` in a directory which
contains a Makefile will execute its first target. You can override
this behaviour by specifying in the Makefile ` .DEFAULT_GOAL :=
    `<target_name>
- you can ask to `make` to execute also other files which respect
Makefile syntax by executing ` make -f  `<filename>`.mk`, where *mk*
is the standard extension for Makefiles
- you can import other Makefiles within a given one by stating
` include  `<filename>`.mk`
- `make`, by default, redirects to stdout all the action of a recipe
before the execution. To avoid such a behaviour (for example, in the
case of an `echo` action) you can prefix a `@` to the action
- comments in Makefile are inserted with a heading `#`

Last but not least, `make` offers a *dry run* mode which shows the steps
that would be executed starting from a given Makefile without actually
executing them. It can be achieved through `make --dry-run` or `make
-n`.

## Variables

Makefile syntax supports *variables*. Basic usage consists in:

- *deferred* assignment with `var_name = var_value` (or *immediate*
assignment with `var_name := var_value`)
- recall via `$(var_name)`

`make` does variable substitution on recipe actions *before* they are
passed to the shell for execution. That means that anything that looks
like a variable will get replaced with the appropriate value. Therefore,
to protect a variable intended to be interpreted by the shell rather
than `make`, you need to double the dollar sign.

In short: `make` variables have a single dollar sign, shell variables
have a double dollar sign.

### Automatic variables

Some variables are automatically computed for each rule and made
accessible in the *recipe* through handy syntax shortcuts. This means
that automatic variables have a limited scope of availability i.e., are
available only within each rule scope (which is, indeed, defined by its
recipe).

Some of them are:

- `$@` , which refers to the target of the rule;
- `$^` , which refers to the complete list of dependencies;
- `$<` , which refers to the first dependency.

In turn, `%` is a wildcard that can be used within both target and
dependencies: the matched pattern can be recalled within the recipe
using the automatic variable `$*`.

It’s also possible to pass a variable to `make` directly at the command
line, by calling ` make  `<target_name>`   `<var_name>`=`<var_value>:
this is useful for example to modify the execution of a given recipe
without permanently altering it.

## Phony targets

Standard Makefile rules expect the target to be *built* by the rule
execution i.e., a rule with a given target is expected to somehow
*create* the target (if needed).

At the same time, `make` functionalities can represent a set of handy
tools also for managing sequences of steps in a given (more “abstract”)
pipeline, possibly without the need of managing concrete targets (files)
or without the limitation of having a unique (preferred) target per
rule.

To overcome this situation, any target can be labelled as *phony* to
inform `make` that no file/directory is actually linked to that target.
This can be achieved by specifying

    .PHONY: target
    target: dependencies
        recipe

However, this choice as a huge effect on *how* `make` will interpret the
rule associated to the phony target: since no actual file is linked to
the target, from `make` perspective there is no way to determine whether
or not the rule has been already executed. This lead to the consequence
that *rules with phony targets are always executed* (somehow locally
breaking the change tracking feature of the tool itself).

Conversely, since the default nature of a rule is expecting the creation
of a file which name coincides with the rule target, a standard
*non-PHONY* rule which abides this nature *should* use a plain `$@`
somewhere in its recipe to indicate the file it creates.

See more in [this useful thread](https://github.com/swcarpentry/make-novice/issues/98#issuecomment-307361751).

### Phony targets as aliases

Despite the above discussion, phony targets can be very useful in
Makefiles, for example to manage *aliases* that can be recalled with
`make`.

For example, in a Makefile which contains a *build* rule can be useful
to recall this rule with `make build` - while *preserving* the change
tracking feature - despite the fact that the build folder is actually
named “build”.

In such a case, we can define a phony target called `build` with no
recipe but a single dependency pointing to the actual building rule.

    .PHONY: build
    build: build_dir_name

    build_dir_name: dependencies
        recipe

In this case, the first call to `make build` will check for the
dependency `build_dir_name` and will execute it. Then, a second attempt
of calling `make build` will led to this message: `make: Nothing to be
done for 'build'`.

This does not mean that `make` knows that `build` has already been
executed (we must remember that `build` is a phony target, so `make` has
no way to track it\!), but simply that *build rule comes with no actions
to be performed* (empty recipe). So, why in the first execution the
build has been actually performed? Basically, thanks to the automated
dependency tracking of `make`, which triggered the execution of
`build_dir_name`. At the second attempt, `make` recognized that the
dependency has already been executed and simply “lacks” to inform us
about this awareness, limiting the stdout log to the `build` scope.

Conversely, a call to `make build_dir_name` *after* `make build` would
have led to this log: `make: 'build_dir_name' is up to date.` (because,
*now*, `make` has been invoked over a trackable rule which has already
been executed, so the log scope referring to this same rule is closer to
what has happened).

This usage of phony targets obviously shows some limitations, but can be
anyway useful in order to obtain a balance between change tracking
functionalities and ease of use.

More on the topic [here](https://stackoverflow.com/questions/23135840/alias-target-name-in-makefile).

## `make help` trick

In order to obtain an automated *documentation* of a Makefile and be
able to recall it through `make help` you can:

- comments each line that must be included in the help with `##`
(instead of the standard single hash)
- define a custom `help` rule with the following syntax:

``` make
.PHONY: help
help: Makefile
    @sed -n 's/^## //p' $&lt
```

This rule recipe passes the whole Makefile (the unique dependency) to
the stream editor `sed` through the automatic variable `$<`. The editor
then looks for the specified pattern and returns the lines which match
with the pattern to stdout.

## Parallelization

*(paragraph 5.4 of GNU make user manual)*

Normally, `make` will execute only one recipe at a time, waiting for it
to finish before executing the next. However, the `-j` or `--jobs`
option tells `make` to execute many recipes simultaneously.

If the `-j` option is followed by an integer, this is the number of
recipes to execute at once; this is called the number of job slots. If
there is nothing looking like an integer after the `-j` option, there is
no limit on the number of job slots. The default number of job slots is
one, which means serial execution (one thing at a time).

## Makefile vs script

Why (and when) a Makefile should be chosen instead of a simple
automation script?

Generally speaking, we can think to a script as a way to *automate* a
process, while `make` uses Makefile to *define* a process and *build*
everything needed within that process scope: it basically provides an
executable *description* of the process pipeline.

Moreover, `make` automatically determines *which* pieces of a large
program need to be recompiled, and issues commands to recompile *just*
them, but is not limited to programs. We can use it to describe any task
where some files must be updated automatically from others whenever the
others change.

This automated behavior of dependency awareness and change tracking
could be achieved also with scripts, but would require a lot more work.
`make` achieves to do it automatically by performing *topological
sorting* on the DAG built over a given Makefile.

**References** 

- [Why use make over a shell script?](https://stackoverflow.com/questions/3798562/why-use-make-over-a-shell-script)
- [Is a Makefile basically the same thing as a batch file?](https://stackoverflow.com/questions/1739276/is-a-makefile-basically-the-same-thing-as-a-batch-file)
- [Script or makefile for automation?](https://unix.stackexchange.com/questions/496793/script-or-makefile-to-automate-new-user-creation/497601#497601)

## Resources

- [Make novice course](https://swcarpentry.github.io/make-novice/) ➜ ~3 hours introductive lesson to automation with `make` (highly recommended as a good place to start)
- [GNU Make manual](https://www.gnu.org/software/make/manual/make.pdf) ➜ official GNU `make` manual (~200 pages...)
- [Usage in Python projects](http://lifesum.github.io/posts/2016/01/14/make-experiments/) ➜ brief showcase of usage in a Python project
