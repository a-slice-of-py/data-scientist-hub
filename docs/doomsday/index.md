# ☄️ Doomsday

I just _don't_ want to start all over again: recipes to survive to a forced reset of development local environment.

## cmder

### Startup/Tasks

- Task parameters: `/dir "C:\Users\USERNAME\Documents\projects"`.
- Cmd: `cmd -new_console:s /k ""%ConEmuDir%\..\init.bat" " & C:\Users\USERNAME\AppData\Local\Continuum\anaconda3\Scripts\activate.bat C:\Users\USERNAME\AppData\Local\Continuum\anaconda3`

### config/user_aliases.cmd

```bash
conda-activate = C:/Users/USERNAME/Miniconda3/Scripts/activate.bat $*
uc11 = cd IAM/uc11-justiren
act-env = make activate-env
uc11-env = cd IAM/uc11-justiren & make activate-env
cdk-env = cd IAM/uc11-justiren & make activate-env ENV_NAME=cdk
aws-login = pushd . && cd C:/Users/USERNAME/Documents/projects/advana/advana-aws-iren-temp-credential-docker/aws_cli_temporary_credentials/Docker/container-mode-advana && make docker-run ACCOUNT=$1 -n && popd
```

## GNU Make

### config.mk

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

### Makefile

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

## Tools

- [cmder](https://cmder.net/)
- [draw.io](https://app.diagrams.net/)
- [Sourcetree](https://www.sourcetreeapp.com/)
- [StackEdit](https://stackedit.io/app#)
- [Sublime Text](https://www.sublimetext.com/)
- [Trello](https://trello.com)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Windows Terminal](https://github.com/microsoft/terminal#via-chocolatey-unofficial)

## Bookmarks

### Libraries

- [AWS CDK](https://docs.aws.amazon.com/cdk/api/v2/python/index.html)
- [OR-Tools](https://google.github.io/or-tools/python/ortools/linear_solver/pywraplp)
- [pyjanitor](https://pyjanitor-devs.github.io/pyjanitor/api/functions/#janitor.functions)

### Press review

- [Streamlit changelog](https://docs.streamlit.io/library/changelog)
- [Practical Business Python](https://pbpython.com/)
- [StackOverflow Blog](https://stackoverflow.blog/)
- [Quanta Magazine](https://www.quantamagazine.org/)
- [Integrable Differentials](https://www.adrian.idv.hk/)
- [Domino Data Science blog](https://blog.dominodatalab.com/)
- [Netflix Technology Blog](https://netflixtechblog.medium.com/)
- [Linkedin Engineering](https://engineering.linkedin.com/blog)
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
