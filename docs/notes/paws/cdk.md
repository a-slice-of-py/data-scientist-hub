# CDK

## DynamoDB

To give write (resp. read) permission to a Lambda on a Dynamo table, both the [CDK docs](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_dynamodb/Table.html#aws_cdk.aws_dynamodb.Table.grant_write_data) and [some snippets](https://github.com/aws-samples/aws-cdk-examples/blob/master/python/dynamodb-lambda/dynamodb_lambda/dynamodb_lambda_stack.py) refer to `grant_write_data` method of the table.

This method should ensure:

1. Lambda permission to perform operations on the table
2. Lambda access to the (possible) KMS key for encrypt/decrypt operations

For the latter there is [this issue](https://github.com/aws/aws-cdk/issues/10010) though, which demonstrates the additional need for:

```python
if table.encryption_key:
    table.encryption_key.grant_decrypt(lambda)
```
