# .Aws

## Services

### API Gateway

- [Accessing API Gateway from VPC](https://stackoverflow.com/questions/58175596/access-api-gateway-api-operation-from-vpc)

### Athena

- [Athena window functions (prestodb)](https://prestodb.io/docs/0.172/functions/window.html)
- [Extend geospatial queries in Amazon Athena with UDFs and AWS Lambda](https://aws.amazon.com/blogs/big-data/extend-geospatial-queries-in-amazon-athena-with-udfs-and-aws-lambda/)

### CDK

- [AWS CDK best practices](https://aws.amazon.com/it/blogs/devops/best-practices-for-developing-cloud-applications-with-aws-cdk/)
- [AWS CDK](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_s3/LifecycleRule.html)
- [AWS CloudWatch custom metrics dashboard via CDK](https://dev.to/leeoc/custom-cloudwatch-metrics-using-the-cdk-337f)
- [A no-nonsense guide to AWS CDK](https://blog.phillipninan.com/a-no-nonsense-guide-to-aws-cloud-development-kit-cdk)
- [Constructs vs stacks](https://blog.phillipninan.com/when-to-use-aws-cdk-constructs-vs-stacks)
- [AWS DDK: DataOps Development Kit](https://github.com/awslabs/aws-ddk)
- [Serverless AWS CDK Pipeline best practices](https://blog.serverlessadvocate.com/serverless-aws-cdk-pipeline-best-practices-patterns-part-1-ab80962f109d)
- [How working with AWS CDK made me a better dev](https://dev.to/aws-builders/how-working-with-aws-open-source-tools-made-me-a-better-developer-343c)

#### Dependencies between stacks

- [The base stack](https://blog.phillipninan.com/insider-secrets-of-aws-cdk-the-base-stack)
- [Deployment issue with cross-stack dependencies](https://aws-blog.com/2020/09/deployment-issues-with-cross-stack-dependencies-and-the-cdk.html)
- [Nested stacks](https://bobbyhadz.com/blog/aws-cdk-nested-stack)
- [Share resources between stacks](https://bobbyhadz.com/blog/aws-cdk-share-resources-between-stacks)
- [CDK dependsOn relation](https://bobbyhadz.com/blog/aws-cdk-dependson-relation)

### CodeBuild

- [Docker layer caching for CodeBuild](https://github.com/aws/aws-codebuild-docker-images/issues/26)
- [serving Sphinx docs on S3](https://gist.github.com/monkut/aa011550d596088ef577ad6d82722a20)
- [Continuous Deployment using AWS CodeBuild with CDK](https://netosec.com/continuous-deployment-using-aws-codebuild-with-cdk-for-next-js/)

### CodePipeline

- [AWS Pipeline for continuous deployment via Lambda](https://towardsdatascience.com/overcoming-aws-codepipelines-design-flaws-to-automate-serverless-ml-architecture-deployment-2c250ae5006a)

### Data Wrangler

- [AWS Data Wrangler](https://github.com/awslabs/aws-data-wrangler)

### Dynamo DB

- [`LucidDynamodb` python wrapper](https://github.com/dineshsonachalam/lucid-dynamodb)

### EC2

- [EC2 ssh with `argparse`](https://towardsdatascience.com/improve-your-ec2-ssh-workflow-using-argparse-ae831d1de754)

### Fargate

- [ML pipeline on Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507)

### IAM

- [All AWS managed policies](https://gist.github.com/bernadinm/6f68bfdd015b3f3e0a17b2f00c9ea3f8)
- [IAMbic: Cloud IAM as Code](https://github.com/noqdev/iambic)

### Lambda

- [AWS Lambda power tuning](https://github.com/alexcasalboni/aws-lambda-power-tuning)
- [AWS Lambda tests](https://towardsdatascience.com/how-i-write-meaningful-tests-for-aws-lambda-functions-f009f0a9c587)
- [Lambda function with container image](https://towardsdatascience.com/how-to-build-an-aws-lambda-for-data-science-cec62deaf0e9)
- [Optimizing Lambda functions](https://cloudash.dev/blog/best-practices-for-optimizing-lambda-functions)

### S3

- [Building and operating a pretty big storage system called S3](https://www.allthingsdistributed.com/2023/07/building-and-operating-a-pretty-big-storage-system.html)

### SageMaker

- [KNN on SageMaker](https://github.com/awslabs/amazon-sagemaker-examples/blob/master/introduction_to_amazon_algorithms/k_nearest_neighbors_covtype/k_nearest_neighbors_covtype.ipynb)
- [SageMaker ScriptProcessor](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.ScriptProcessor)
- [Automatic canary releases for ML models](https://towardsdatascience.com/automatic-canary-releases-for-machine-learning-models-38874a756f87)
- [Cross-validation via SageMaker and Step functions](https://towardsdatascience.com/cross-validate-your-machine-learning-model-with-sagemaker-and-step-functions-6610e9c6ab32?source=social.tw)
- [Run custom model via SageMaker (e.g. OR-Tools solver)](https://github.com/aws-samples/wastecollector-planner/blob/main/Sagemaker/Using%20Sagemaker-OR-Tools.ipynb)
- [Automating ML Training on AWS](https://towardsdatascience.com/pipeline-dreams-automating-ml-training-on-aws-8e90a33061fd)

### Shell

- [AWS shell](https://github.com/awslabs/aws-shell)

## Utils

### DevOps

- [Deployment Pipeline Reference Architecture (DPRA) for AWS workloads](https://pipelines.devops.aws.dev/)
- [DevOps Essentials](https://community.aws/concepts/devops-essentials)
- [12 DevOps Best Practices That Make Deploying on Fridays Less Scary](https://community.aws/posts/deploy-on-friday-devops-best-practices)

### Blogposts

- [The history of Amazon forecasting algorithm](https://www.amazon.science/latest-news/the-history-of-amazons-forecasting-algorithm)

### Misc

- [SLAM](https://github.com/miguelgrinberg/slam)
- [MOTO for local test of aws resources](https://github.com/spulec/moto)
- [MOTO tutorial](https://towardsdatascience.com/moto-pytest-and-aws-databases-a-quality-and-data-engineering-crossroads-ae58f9e7b265)
- [Steampipe: query the cloud with plain SQL](https://github.com/turbot/steampipe)
- [Dynamoit: a custom frontend for DynamoDB](https://github.com/bykka/dynamoit)
- [Basti: a CLI tool for securely accessing AWS resources in private networks at almost no cost](https://github.com/BohdanPetryshyn/basti)
- [klotho: an open source tool that transforms plain code into cloud native code](https://github.com/klothoplatform/klotho)

### Streamlit deployment

- [Streamlit deploy on EC2](https://towardsdatascience.com/how-to-deploy-a-streamlit-app-using-an-amazon-free-ec2-instance-416a41f69dc3)
- [Streamlit deploy with Fargate](https://github.com/nicolasmetallo/legendary-streamlit-demo#3-deploy-your-streamlit-app-to-aws-fargate-using-aws-cdk)
- [Streamlit dashboard deployment via ECS](https://aws.amazon.com/it/blogs/opensource/using-streamlit-to-build-an-interactive-dashboard-for-data-analysis-on-aws/)

### Infographics

- [AWS Fundamentals](https://digests.awsfundamentals.com/)

