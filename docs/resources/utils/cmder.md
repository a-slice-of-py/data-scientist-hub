# cmder

```
conda-activate = C:/Users/a00018578/Miniconda3/Scripts/activate.bat $*
uc11 = cd BU-Ambiente/uc11-justiren
act-env = make activate-env
uc11-env = cd BU-Ambiente/uc11-justiren & make activate-env
cdk-env = cd BU-Ambiente/uc11-justiren & make activate-env ENV_NAME=cdk
aws-login = pushd . && cd C:/Users/a00018578/Documents/projects/advana/advana-aws-iren-temp-credential-docker/aws_cli_temporary_credentials/Docker/container-mode-advana && make docker-run ACCOUNT=$1 -n && popd
```

## Integration in VS Code

- [FAQs](https://code.visualstudio.com/docs/editor/integrated-terminal#_can-i-use-cmders-shell-with-the-terminal-on-windows)
- [cmder wiki](https://github.com/cmderdev/cmder/wiki/Seamless-VS-Code-Integration)