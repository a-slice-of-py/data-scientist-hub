# EC2

## Instance debug

To check instance initialization:

- establish an SSH connection;
- inspect logs located at `/var/log/cloud-init-output.log` as suggested [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html#user-data-console).

## VPC Subnets

If an AWS Lambda raises timeout connection error while trying to reach a Dynamo DB table, despite inside a VPC with endpoint towards DynamoDB enabled, please refer to [this issue](https://stackoverflow.com/a/54789779): the reason might be related to public subnets randomly assigned to the lambda in a given availability zone.
