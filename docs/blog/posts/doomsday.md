---
date: 2022-01-05
authors:
  - silvio
categories:
  - Recipes
tags:
  - Development
  - Cmder
  - GNU Make
  - VSC
  - Jupyter
  - Windows Terminal
---

# How to survive a forced reset of local development environment

<!-- more -->

## cmder

### Startup/Tasks

- Task parameters: `/dir "C:\Users\USERNAME\Documents\projects"`.
- Cmd: `cmd -new_console:s /k ""%ConEmuDir%\..\init.bat" " & C:\Users\USERNAME\AppData\Local\Continuum\anaconda3\Scripts\activate.bat C:\Users\USERNAME\AppData\Local\Continuum\anaconda3`

### config/user_aliases.cmd

```bash
conda-activate = C:/Users/USERNAME/Miniconda3/Scripts/activate.bat $*
act-env = make activate-env
uc11 = cd IAM/uc11-justiren
uc11-env = cd IAM/uc11-justiren & make activate-env
aws-login = pushd . && cd C:/Users/USERNAME/Documents/projects/advana/advana-aws-iren-temp-credential-docker/aws_cli_temporary_credentials/Docker/container-mode-advana && make docker-run ACCOUNT=$1 -n && popd
```

## GNU Make

??? example "`config.mk`"
    ```make
    include .env
    export $(cat .env)

    # split AWS_PROFILE to get AWS_ENV
    PROFILE = $(shell echo $(AWS_PROFILE) | cut -f3 -d"-")

    ENV_NAME = ... # conda env name
    CLIP_MESSAGE = "Command stored! You can past and run it in the CLI."
    SECRET_MESSAGE = "Secret stored!"
    PY_VERSION = 3.8
    AWS_SECRET = ...
    SECRET_FIELD = ...
    APP = ...
    STACKS = ...
    AWS_ENV = ...-$(PROFILE)
    ...
    ```

??? example "`Makefile`"

    ```make
    include config.mk
    ## 
    ## -------------------------------------------
    ## |                Makefile                 |
    ## -------------------------------------------
    ## 
    ## create-env
    ##     initialize python virtual environment (LAUNCH FROM BASE ENV!)
    .PHONY: create-env
    create-env:
        @echo $(CLIP_MESSAGE)
        @echo "conda create --name $(ENV_NAME) python=$(PY_VERSION)" | clip
    ## 
    ## unregister-env
    ##     unregister virtual environment in jupyter suite (LAUNCH FROM BASE ENV!)
    .PHONY: unregister-env
    unregister-env:
        jupyter kernelspec uninstall $(ENV_NAME)
    ## 
    ## activate-env
    ##     activate python virtual environment
    .PHONY: activate-env
    activate-env:
        @echo $(CLIP_MESSAGE)
        @echo "conda-activate $(ENV_NAME)" | clip
    ## 
    ## init-env
    ##     initialize miniconda environment installing pip
    .PHONY: init-env
    init-env:
        @echo $(CLIP_MESSAGE)
        @echo "conda install pip" | clip
    ## 
    ## init
    ##     initialize package basic dependencies
    .PHONY: init
    init:
        python -m pip install -r ./requirements.txt
    ## 
    ## register-env
    ##     register virtual environment in jupyter suite
    .PHONY: register-env
    register-env:
        python -m ipykernel install --user --name=$(ENV_NAME)
    ## 
    ## reqs
    ##     save requirements.txt with pipreqs
    .PHONY: reqs
    reqs:
        pipreqs ./ --encoding latin --ignore cdk-app,notebook,data
    ## 
    ## install-package
    ##     install python package in edit mode
    .PHONY: install-package
    install-package:
        python -m pip install -e .
    ## 
    ## st-run [APP]
    ##     run streamlit app
    ##     APP=sandbox or monitor
    .PHONY: st-run
    st-run:
        cd ./dashboard && streamlit run $(APP).py
    ## 
    ## docs-serve
    ##     serve package docs on localhost
    .PHONY: docs-serve
    docs-serve:
        mkdocs serve
    ## 
    ## docs-build
    ##     build package docs as static html website
    .PHONY: docs-build
    docs-build:
        mkdocs build --no-directory-urls
    ## 
    ## test
    ##     execute tests with pytest and dump html report
    .PHONY: test
    test:
        cd tests && pytest
    ##
    ## cdk-deploy [PROFILE, STACKS | STACK]
    ##     deploy cdk app
    ##     PROFILE=dev, test or prod
    ##     STACKS='*'
    ##     STACK=stack suffix name
    .PHONY: cdk-deploy
    cdk-deploy:
        cd ./cdk-app && cdk deploy $(STACKS) --profile $(AWS_ENV)
    ## 
    ## st-pswd [PROFILE, USER]
    ##     retrieve password to connect to Streamlit app
    ##     PROFILE=dev, test or prod
    ##     USER=advana, business or cartografia
    .PHONY: st-pswd
    st-pswd:
        @echo AWS_PROFILE: $(AWS_ENV)
        @aws secretsmanager get-secret-value --secret-id $(AWS_SECRET) --profile $(AWS_ENV) \
        | jq '.SecretString' \
        | awk '{print substr($$0,2,length($$0)-2)}' \
        | sed 's|[\\]||g' \
        | jq '.$(SECRET_FIELD)' \
        | sed 's|["]||g' \
        | clip
        @echo $(CLIP_MESSAGE)
    ## 
    ## gource-play
    ##     shows git history as gource animation
    .PHONY: gource-play
    gource-play:
        git log --pretty=format:"%at|%s" --reverse --no-merges > gource-caption.txt \
        && gource --key \
        --user-image-dir 'PATH_TO_AVATARS' \
        --seconds-per-day 1 \
        --auto-skip-seconds 2 \
        --title "TITLE" \
        --caption-file gource-caption.txt \
        --caption-offset -90 \
        --caption-duration 4 \
        --logo 'PATH_TO_LOGO' \
        --logo-offset 50x1050 -f
    ## 
    ## gource-build
    ##     save git history as gource video
    .PHONY: gource-build
    gource-build:
        git log --pretty=format:"%at|%s" --reverse --no-merges > gource-caption.txt \
        && gource --key \
        --user-image-dir 'PATH_TO_AVATARS' \
        --seconds-per-day .5 \
        --auto-skip-seconds 1 \
        --title "TITLE" \
        --caption-file gource-caption.txt \
        --caption-offset -90 \
        --caption-duration 2 \
        --logo 'PATH_TO_LOGO' \
        --logo-offset 50x1050 -f \
        -o gource.ppm \
        && ffmpeg \
        -y \
        -r 60 \
        -f image2pipe \
        -vcodec ppm \
        -i gource.ppm \
        -vcodec libx264 \
        -preset ultrafast \
        -pix_fmt yuv420p \
        -crf 17 \
        -threads 0 \
        -bf 0 development-history.mp4 \
        && rm gource.ppm
    ## 
    ## help
    ##     show this help
    .PHONY: help
    help: Makefile
        @sed -n 's/^## //p' $<
    ```

## JupyterLab Extensions

- [jupyterlab-execute-time](https://github.com/deshaw/jupyterlab-execute-time)
- [@aquirdturtle/collapsible_headings](https://github.com/aquirdTurtle/Collapsible_Headings)
- [jupyterlab-chart-editor](https://github.com/plotly/jupyterlab-chart-editor)
- [jupyterlab-plotly](https://plotly.com/python/getting-started/#jupyterlab-support)
- [jupyterlab-tailwind-theme](https://github.com/simicd/jupyterlab-tailwind-theme)
- [simpledark](https://github.com/ericmiguel/jupyterlab-simpledark)

## Visual Studio Code

??? example "`settings.json`"
    ```json
    {
        "telemetry.telemetryLevel": "off",
        "workbench.colorTheme": "Dracula",
        "python.pythonPath": "C:\\Users\\USERNAME\\Miniconda3\\envs\\ENV\\python.exe",
        "workbench.colorCustomizations": {


        },
          "editor.semanticTokenColorCustomizations": {
              "[Dracula Soft]": { // Apply to this theme only
                  "enabled": false,
                  "rules": {
                      "magicFunction:python": "#ee0000",
                      "function.declaration:python": "#87E570",
                      "class.declaration:python": "#87E570",
                      "function.call.python": "#66D9EF",
                      "*.decorator:python": "#0000dd",
                      "*.typeHint:python": "#6ED5D3",
                      "*.typeHintComment:python": "#aaaaaa"
                  }
              }
          },
        "editor.tokenColorCustomizations": {
            "textMateRules": [
              {
                "scope": "meta.function-call.generic.python",
                "settings": {
                  "foreground": "#66D9EF"
                }
              },
              {
                "scope": ["string.quoted.docstring.multi.python", "punctuation.definition.string.begin.python", "punctuation.definition.string.end.python"],
                "settings":{
                  "foreground": "#E7EE98"
                }
              }
            ]
          },
          "workbench.editorAssociations": {
            "*.ipynb": "jupyter-notebook"
          },
          "python.languageServer": "Pylance",
          "codetags.custom": [
          {"name": "see", "body": "For reference see [here]()"}
          ],
          "todohighlight.keywords": [{
            "text": "SEE",
            "backgroundColor": "#282A36",
            "overviewRulerColor": "grey"
        },
      ],
      "todo-tree.tree.showScanModeButton": false,
      "todo-tree.highlights.enabled": false,
      "files.eol": "\n",
      "todo-tree.general.tags": [
        "BUG",
        "HACK",
        "FIXME",
        "TODO",
        "XXX",
        "[ ]",
        "[x]"
      ],
      "todo-tree.regex.regex": "(//|#|<!--|;|/\\*|^|^\\s*(-|\\d+.))\\s*($TAGS)",
      "security.workspace.trust.untrustedFiles": "open",
      "notebook.cellToolbarLocation": {
        "default": "right",
        "jupyter-notebook": "left"
      },
      "aws.profile": "profile:AWS_PROFILE",
      "aws.sam.enableCodeLenses": false,
      "gitlens.hovers.currentLine.over": "line",
      "gitlens.codeLens.enabled": false,
      "json.schemas": [],
      "terminal.integrated.profiles.windows": {
        "PowerShell": {
          "source": "PowerShell",
          "icon": "terminal-powershell"
        },
        "Command Prompt": {
          "path": [
            "${env:windir}\\Sysnative\\cmd.exe",
            "${env:windir}\\System32\\cmd.exe"
          ],
          "args": [],
          "icon": "terminal-cmd"
        },
        "Git Bash": {
          "source": "Git Bash"
        },
          "cmder": {
            "path": [
              "${env:windir}\\Sysnative\\cmd.exe",
              "${env:windir}\\System32\\cmd.exe"
            ],
            "args": ["/k", "C:/Users/USERNAME/Documents/projects/cmder_mini/vendor/init.bat"],
            "overrideName": true,
            "icon": "pulse",
            "color": "terminal.ansiGreen"
          }
        },
        "terminal.integrated.defaultProfile.windows": "cmder",
        "mypy.dmypyExecutable": "C:\\Users\\USERNAME\\.mypyls\\Scripts\\dmypy.exe"
    }
    ```

### Extensions

- [Ace Palenight theme](https://github.com/acestojanoski/ace-palenight)
- [AWS Toolkit](https://github.com/aws/aws-toolkit-vscode)
- [Better Jinja](https://github.com/samuelcolvin/jinjahtml-vscode)
- [Better TOML](https://github.com/bungcip/better-toml)
- [codetags](https://github.com/cg-cnu/vscode-codetags)
- [Docker](https://github.com/microsoft/vscode-docker)
- [Dracula Official](https://github.com/dracula/visual-studio-code)
- [Excel Viewer](https://github.com/jjuback/gc-excelviewer)
- [Git Graph](https://github.com/mhutchie/vscode-git-graph)
- [GitLens](https://github.com/gitkraken/vscode-gitlens)
- [Jupyter](https://github.com/Microsoft/vscode-jupyter)
- [Jupyter Keymap](https://github.com/Microsoft/vscode-jupyter-keymap)
- [Jupyter Notebook Renderers](https://github.com/Microsoft/vscode-notebook-renderers)
- [Markdown Preview Enhanced](https://github.com/shd101wyy/vscode-markdown-preview-enhanced)
- [markdownlint](https://github.com/DavidAnson/vscode-markdownlint)
- [Notepad++ keymap](https://github.com/Microsoft/vscode-notepadplusplus-keybindings)
- [Pylance](https://github.com/microsoft/pylance-release)
- [Python](https://github.com/Microsoft/vscode-python)
- [Python Docstring Generator](https://github.com/NilsJPWerner/autoDocstring)
- [Remote - Containers](https://github.com/Microsoft/vscode-remote-release)
- [Remote - WSL](https://github.com/Microsoft/vscode-remote-release)
- [TODO Highlight](https://github.com/wayou/vscode-todo-highlight)
- [Todo Tree](https://github.com/Gruntfuggly/todo-tree)

### Key bindings

- To switch focus between editor and terminal, please refer to [this thread](https://superuser.com/questions/1270103/how-to-switch-the-cursor-between-terminal-and-code-in-vscode)

## Windows Terminal

??? example "`settings.json`"
    ```json
    {
        "$schema": "https://aka.ms/terminal-profiles-schema",
        "actions": 
        [
            // {
            //     "command": 
            //     {
            //         "action": "copy",
            //         "singleLine": false
            //     },
            //     "keys": "ctrl+c"
            // },
            {
                "command": "paste",
                "keys": "ctrl+v"
            },
            {
                "command": "find",
                "keys": "ctrl+shift+f"
            },
            {
                "command": 
                {
                    "action": "splitPane",
                    "split": "auto",
                    "splitMode": "duplicate"
                },
                "keys": "alt+shift+d"
            },
            {
                "command": 
                {
                    "action": "splitPane",
                    "profile": "Node.js",
                    "split": "auto"
                },
                "keys": "ctrl+alt+n"
            },
            {
                "command": 
                {
                    "action": "splitPane",
                    "profile": "Ubuntu-18.04",
                    "split": "auto"
                },
                "keys": "ctrl+alt+u"
            },
            {
                "command": 
                {
                    "action": "splitPane",
                    "profile": "PowerShell 7",
                    "split": "auto"
                },
                "keys": "ctrl+alt+s"
            }
        ],
        "alwaysOnTop": false,
        "copyFormatting": "none",
        "copyOnSelect": false,
        "defaultProfile": "{5b4ef9a8-4506-4ac9-930a-5eb1fd0ebf20}",
        "multiLinePasteWarning": false,
        "profiles": 
        {
            "defaults": 
            {
                "startingDirectory": "C:/Users/USERNAME/Documents/projects/"
            },
            "list": 
            [
                {
                    "commandline": "powershell.exe",
                    "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
                    "hidden": false,
                    "name": "Windows PowerShell"
                },
                {
                    "commandline": "cmd.exe",
                    "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
                    "hidden": false,
                    "name": "Command Prompt"
                },
                {
                    "guid": "{b453ae62-4e3d-5e58-b989-0a998ec441b8}",
                    "hidden": false,
                    "name": "Azure Cloud Shell",
                    "source": "Windows.Terminal.Azure"
                },
                {
                    "colorScheme": "synthwave-everything",
                    "guid": "{c6eaf9f4-32a7-5fdc-b5cf-066e8a4b1e40}",
                    "hidden": false,
                    "name": "Ubuntu-18.04",
                    "source": "Windows.Terminal.Wsl"
                },
                {
                    "backgroundImage": "PATH_TO_IMAGE",
                    "backgroundImageAlignment": "right",
                    "backgroundImageOpacity": 0.20000000000000001,
                    "backgroundImageStretchMode": "uniform",
                    "colorScheme": "Sakura",
                    "commandline": "cmd.exe /k C:/Users/USERNAME/Documents/projects/cmder_mini/vendor/init.bat && C:/Users/USERNAME/Miniconda3/Scripts/activate.bat C:/Users/USERNAME/Miniconda3",
                    "guid": "{5b4ef9a8-4506-4ac9-930a-5eb1fd0ebf20}",
                    "hidden": false,
                    "icon": " C:/Users/USERNAME/Documents/projects/cmder_mini/icons/cmder.ico",
                    "name": "Cmder",
                    "cursorShape": "vintage"
                },
                {
                    "commandline": "C:/Program Files/nodejs/node.exe",
                    "icon": "C:/Program Files/nodejs/node_modules/npm/docs/public/icons/icon-48x48.png",
                    "name": "Node.js"
                },
                {
                    "commandline": "C:/Users/USERNAME/Documents/projects/PowerShell-7.1.0-win-x64/pwsh.exe",
                    "icon": "C:/Users/USERNAME/Documents/projects/PowerShell-7.1.0-win-x64/assets/Square150x150Logo.png",
                    "name": "PowerShell 7"
                }
            ]
        },
        "schemes": 
        [
            {
                "name": "NightLionV2",
                "black": "#4c4c4c",
                "red": "#bb0000",
                "green": "#04f623",
                "yellow": "#f3f167",
                "blue": "#64d0f0",
                "purple": "#ce6fdb",
                "cyan": "#00dadf",
                "white": "#bbbbbb",
                "brightBlack": "#555555",
                "brightRed": "#ff5555",
                "brightGreen": "#7df71d",
                "brightYellow": "#ffff55",
                "brightBlue": "#62cbe8",
                "brightPurple": "#ff9bf5",
                "brightCyan": "#00ccd8",
                "brightWhite": "#ffffff",
                "background": "#171717",
                "foreground": "#bbbbbb",
                "selectionBackground": "#b5d5ff",
                "cursorColor": "#bbbbbb"
              },
            {
                "name": "Sakura",
                "black": "#000000",
                "red": "#d52370",
                "green": "#41af1a",
                "yellow": "#bc7053",
                "blue": "#6964ab",
                "purple": "#c71fbf",
                "cyan": "#939393",
                "white": "#998eac",
                "brightBlack": "#786d69",
                "brightRed": "#f41d99",
                "brightGreen": "#22e529",
                "brightYellow": "#f59574",
                "brightBlue": "#9892f1",
                "brightPurple": "#e90cdd",
                "brightCyan": "#eeeeee",
                "brightWhite": "#cbb6ff",
                "background": "#18131e",
                "foreground": "#dd7bdc",
                "selectionBackground": "#c05cbf",
                "cursorColor": "#ff65fd"
              },
            {
                "name": "Laser",
                "black": "#626262",
                "red": "#ff8373",
                "green": "#b4fb73",
                "yellow": "#09b4bd",
                "blue": "#fed300",
                "purple": "#ff90fe",
                "cyan": "#d1d1fe",
                "white": "#f1f1f1",
                "brightBlack": "#8f8f8f",
                "brightRed": "#ffc4be",
                "brightGreen": "#d6fcba",
                "brightYellow": "#fffed5",
                "brightBlue": "#f92883",
                "brightPurple": "#ffb2fe",
                "brightCyan": "#e6e7fe",
                "brightWhite": "#ffffff",
                "background": "#030d18",
                "foreground": "#f106e3",
                "selectionBackground": "#2e206a",
                "cursorColor": "#00ff9c"
              },
              {
                "name": "Aurelia",
                "background": "#1A1A1A",
                "black": "#000000",
                "blue": "#579BD5",
                "brightBlack": "#797979",
                "brightBlue": "#9CDCFE",
                "brightCyan": "#2BC4E2",
                "brightGreen": "#1AD69C",
                "brightPurple": "#975EAB",
                "brightRed": "#EB2A88",
                "brightWhite": "#EAEAEA",
                "brightYellow": "#E9AD95",
                "cursorColor": "#FFFFFF",
                "cyan": "#00B6D6",
                "foreground": "#EA549F",
                "green": "#4EC9B0",
                "purple": "#714896",
                "red": "#E92888",
                "selectionBackground": "#FFFFFF",
                "white": "#EAEAEA",
                "yellow": "#CE9178"
            },
              {
                "name": "Horizon",
                "black": "#0a0a0d",
                "red": "#E95678",
                "green": "#29D398",
                "yellow": "#FAB795",
                "blue": "#26BBD9",
                "purple": "#EE64AC",
                "cyan": "#59E1E3",
                "white": "#e5e5e5",
                "brightBlack": "#848484",
                "brightRed": "#EC6A88",
                "brightGreen": "#3FDAA4",
                "brightYellow": "#FBC3A7",
                "brightBlue": "#3FC4DE",
                "brightPurple": "#F075B5",
                "brightCyan": "#6BE4E6",
                "brightWhite": "#e5e5e5",
                "background": "#1c1e26",
                "foreground": "#bdc0c2"
              },
            {
                "name": "synthwave-everything",
                "black": "#fefefe",
                "red": "#f97e72",
                "green": "#72f1b8",
                "yellow": "#fede5d",
                "blue": "#6d77b3",
                "purple": "#c792ea",
                "cyan": "#f772e0",
                "white": "#fefefe",
                "brightBlack": "#fefefe",
                "brightRed": "#f88414",
                "brightGreen": "#72f1b8",
                "brightYellow": "#fff951",
                "brightBlue": "#36f9f6",
                "brightPurple": "#e1acff",
                "brightCyan": "#f92aad",
                "brightWhite": "#fefefe",
                "background": "#2a2139",
                "foreground": "#f0eff1",
                "selectionBackground": "#181521",
                "cursorColor": "#72f1b8"
              },
              {
                "name": "Dracula",
                "black": "#000000",
                "red": "#ff5555",
                "green": "#50fa7b",
                "yellow": "#f1fa8c",
                "blue": "#bd93f9",
                "purple": "#ff79c6",
                "cyan": "#8be9fd",
                "white": "#bbbbbb",
                "brightBlack": "#555555",
                "brightRed": "#ff5555",
                "brightGreen": "#50fa7b",
                "brightYellow": "#f1fa8c",
                "brightBlue": "#bd93f9",
                "brightPurple": "#ff79c6",
                "brightCyan": "#8be9fd",
                "brightWhite": "#ffffff",
                "background": "#1e1f29",
                "foreground": "#f8f8f2",
                "selectionBackground": "#44475a",
                "cursorColor": "#bbbbbb"
              }
        ],
        "theme": "dark"
    }
    ```

## Tools

- [cmder](https://cmder.net/)
- [draw.io](https://app.diagrams.net/)
- [Sourcetree](https://www.sourcetreeapp.com/)
- [StackEdit](https://stackedit.io/app#)
- [Sublime Text](https://www.sublimetext.com/)
- [Trello](https://trello.com)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Windows Terminal](https://github.com/microsoft/terminal#via-chocolatey-unofficial)
- [WSL2](https://docs.microsoft.com/it-it/windows/wsl/install)
- [Lightshot](https://app.prntscr.com/en/index.html)
- [Just Color Picker](https://annystudio.com/software/colorpicker/)

## Bookmarks

### Libraries

- [AWS CDK](https://docs.aws.amazon.com/cdk/api/v2/python/index.html)
- [OR-Tools](https://google.github.io/or-tools/python/ortools/linear_solver/pywraplp)
- [pyjanitor](https://pyjanitor-devs.github.io/pyjanitor/api/functions/#janitor.functions)
- [Apache Echarts](https://echarts.apache.org/examples/en/index.html#chart-type-line)
- [Streamlit changelog](https://docs.streamlit.io/library/changelog)

### Press review

- [discuss.streamlit](https://discuss.streamlit.io/)
- [Practical Business Python](https://pbpython.com/)
- [StackOverflow Blog](https://stackoverflow.blog/)
- [Quanta Magazine](https://www.quantamagazine.org/)
- [Integrable Differentials](https://www.adrian.idv.hk/)
- [Domino Data Science blog](https://blog.dominodatalab.com/)
- [Netflix Technology Blog](https://netflixtechblog.medium.com/)
- [Linkedin Engineering](https://engineering.linkedin.com/blog)
- [O'Reilly Radar](https://www.oreilly.com/radar/)
- [Towards AI](https://pub.towardsai.net/)
- [TowardsDataScience](https://towardsdatascience.com/data-science/home)

### Misc

- [Coolors palette generator](https://coolors.co/generate)
- [Streamlit emoji](https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json)
- [Streamlitopedia](https://pmbaumgartner.github.io/streamlitopedia/essentials.html)
- [pwdhash](https://pwdhash.github.io/website/)
- [matplotlib colors](https://matplotlib.org/mpl_examples/color/named_colors.hires.png)
- [matplotlib colormaps](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
- [JSON formatter](https://jsonformatter.org/)
- [Unicode table](https://unicode-table.com/en/sets/)
- [Fontawesome icons](https://fontawesome.com/v5.15/icons?d=gallery&p=2&s=solid&m=free)
- [Markdown guide](https://www.markdownguide.org/getting-started/)
- [Bootstrap icons](https://icons.getbootstrap.com/)

## macOS

- [How to setup Python on ARM machines](https://towardsdatascience.com/how-to-easily-set-up-python-on-any-m1-mac-5ea885b73fab)
- [MacOS terminal makeover](https://towardsdatascience.com/the-ultimate-guide-to-your-terminal-makeover-e11f9b87ac99)
- [How to dedup conda env name in terminal](https://github.com/spaceship-prompt/spaceship-prompt/issues/218)
- [Warp terminal](https://www.warp.dev/)

## Troubleshooting

### Jupyter Lab

- If Plotly charts are not rendered into JupyterLab, execute `jupyter labextension install jupyterlab-plotly` in the _server_ environment for JupyterLab.
- To disable new undo/redo behaviour, see [this thread](https://stackoverflow.com/questions/68763795/how-to-undo-redo-changes-inside-the-selected-cell-in-jupyter-notebook).
- To enable auto closing brackets, see [this issue](https://github.com/jupyterlab/jupyterlab/issues/9897#issuecomment-926131944).
- If ipywidgets aren't display properly (e.g. tqdm), see [this issue](https://stackoverflow.com/a/66711390/13790005)
- To activate conda in a PowerShell shell run `.\shell\condabin\conda-hook.ps1`, which can be found in Miniconda3 installation directory (see [this thread](https://stackoverflow.com/a/71665464))
- On Windows, to fix the error `ImportError: DLL load failed while importing _ssl: The specified module could not be found.` refer to [this thread](https://stackoverflow.com/a/60405693) and copy the DLLs to the path of _each Python venv which result broken_
