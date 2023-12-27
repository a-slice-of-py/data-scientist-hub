---
date: 2021-12-21
authors:
  - silvio
categories:
  - Recipes
tags:
  - AWS
  - SAM
  - Lambda
---

# Build Lambda layers with AWS SAM

The AWS Serverless Application Model (AWS SAM) is an open-source framework that you can use to build serverless applications on AWS. A useful tutorial can be found [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html).

<!-- more -->

Lambda layers builds can be automated through the code in [aws-lambda-layer](https://github.com/a-slice-of-py/aws-lambda-layer) repo. The idea is forcing AWS SAM to build layers in the same way it builds Lambdas as described [here](https://bryson3gps.wordpress.com/2018/12/06/trick-sam-into-building-your-lambda-layers/) and [here](https://stackoverflow.com/questions/58369170/build-custom-aws-lambda-layer-for-scikit-image/58408130#58408130).

The SAM app structure should look like the following:

``` bash
sam-app/
│
├── lambdas/
│   ├── __init__.py
│   ├── lambda_1.py
│   ├── lambda_2.py
│   └── requirements.txt
│
├── layers/
│   ├── __init__.py
│   ├── dummy_lambda.py
│   └── requirements.txt
│
└── template.yaml
```

You basically have to:

1. define a dummy Lambda function in `template.yaml` with a related `requirements.txt` which is supposed to contain the packages to be included in the layer;
2. define the related layer in `template.yaml` which _ContentUri_ must point to the build path of the dummy lambda;
3. modify any (actual) Lambda source code adding `sys.path.append('/opt')` before importing the required packages.

The addition made in the template should look like this:

``` yaml
  DummyLambda:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: layers/
      Handler: dummy_lambda.lambda_handler
  CustomLayer:
    Type: AWS::Serverless::LayerVersion
    Properties:
      LayerName: CustomLayer
      Description: Simple layer containing custom library
      ContentUri: ./.aws-sam/build/DummyLambda
      CompatibleRuntimes:
        - python3.7
        - python3.8
        - python3.9
      RetentionPolicy: Delete
    DependsOn: DummyLambda
```

## w/ custom local module

The following methods are possible ways to overcome errors related to the import of custom local scripts within AWS Lambda functions, such as `attempted relative import with no known parent package`, `attempted relative import beyond top-level package`, etc.

!!! info
    [Here](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912) you can find a complete overview of relative imports, difference between modules and scripts and more.

In the simplest case in which the custom script `custom_script.py` is a dependency of just one Lambda, it is sufficient to put it in the lambdas
folder, and importing it within the lambda source code with an _implicit relative import_ as `from custom_script import stuff`. The project tree looks like the following:

``` bash
sam-app/
│
├── lambda_1/
│   ├── __init__.py
│   ├── lambda_1.py
│   ├── custom_script.py
│   └── requirements.txt
│
├── lambda_2/
│   ├── __init__.py
│   ├── lambda_2.py
│   └── requirements.txt
│
├── layers/
│   ├── __init__.py
│   ├── dummy_lambda.py
│   └── requirements.txt
│
└── template.yaml
```

For further reference see [this gist](https://gist.github.com/gene1wood/06a64ba80cf3fe886053f0ca6d375bc0).

As of early 2020, it seems there's no standard/straightforward way to build a custom script as shared dependency across two or more lambdas. A possible workaround - inspired from [this thread](https://stackoverflow.com/questions/58402409/sam-build-does-it-also-build-layers) - consists in exploiting the (possibly already created) dummy lambda. Since SAM builds every lambda within the app root folder, you can put the custom script within dummy lambda folder, and import the script with an _implicit relative import_ in the dummy lambda source code, such as `import custom_script`. When SAM builds the layer associated to the dummy lambda, your custom script will be included within the layer as well and can be served as dependecy across all lambdas.

The project tree looks like the following:

``` bash
sam-app/
│
├── lambda_1/
│   ├── __init__.py
│   ├── lambda_1.py
│   └── requirements.txt
│
├── lambda_2/
│   ├── __init__.py
│   ├── lambda_2.py
│   └── requirements.txt
│
├── layers/
│   ├── __init__.py
│   ├── dummy_lambda.py
│   ├── custom_script.py
│   └── requirements.txt
│
└── template.yaml
```
