# Doomsday

I just _don't_ want to start all over again: recipes to survive to a forced reset of development local environment.

## cmder

```
conda-activate = C:/Users/USERNAME/Miniconda3/Scripts/activate.bat $*
uc11 = cd BU-Ambiente/uc11-justiren
act-env = make activate-env
uc11-env = cd BU-Ambiente/uc11-justiren & make activate-env
cdk-env = cd BU-Ambiente/uc11-justiren & make activate-env ENV_NAME=cdk
aws-login = pushd . && cd C:/Users/USERNAME/Documents/projects/advana/advana-aws-iren-temp-credential-docker/aws_cli_temporary_credentials/Docker/container-mode-advana && make docker-run ACCOUNT=$1 -n && popd
```
