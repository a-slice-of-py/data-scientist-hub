# DynamoDB

An overview of AWS DynamoDB NoSQL database.

## Usage modes

Each Dynamo table has two different usage modes which differ on desired reading and writing capabilities: on-demand and provisioned.

Despite the selected mode, interactions with DynamoDb tables are managed abiding the following consumption schema:

- 1 writing capacity unit (WCU) for each writing operation (up to 1KB)
- 0,5 reading capacity unit (RCU) for each _eventually consistent_ [^1] reading operation (up to 4KB)
- 1 reading capacity unit for each _strongly consistent_ [^2] reading operation (up to 4KB)
- 2 reading/writing capacity units for each _transational_ operation
- multiple capacity units for each operation which exceeds above size limits

### Pricing

As per `eu-central-1` region and as of 2021, the pricing schema is:

- **on-demand**: 1,525 USD per million units
- **provisioned**: 0,000793 USD per RCU/hour (or WCU/hour)

Simplifying:

- on-demand mode bills operations on the table at their incoming rate

	!!! example
		80M writing operations cost 122 USD

- provisioned mode requires assignment of RCU and WCU available _per hour_, and then bills accordingly

	!!! example
		80M writing operations on a provisioned table with 1000 WCU assigned are managed roughly in 22 hours (80M / (1000 WCU * 3600) and cost 22 * 1000 * 0,000793 ~ 17 USD

If no latency in operations management is allowed, on-demand mode ensures that at a price point roughly 7x the baseling provisioned mode. On the other hand, provisioned mode can be more reliable in terms of costs planning (thanks to the capacity assignment made beforehand), but implies a cap on operations manageable and generates fixed costs even when no operations are needed on the table.

### Autoscaling

Provisioned mode comes with the possibility of setting up autoscaling feature, which can increase operations rate when needed (particularly useful in operation peaks management). Autoscaling setup requires:

- min capacity
- max capacity
- target usage rate (ratio between consumed units and available units)

!!! important
	Autoscaling features is in charge of _scaling_ the provisioned capacity within [min, max] range so that the actual usage rate is mantained close to the specified target.

Autoscaling is based on CloudWatch metrics linked to read and write operations: as soon as these metrics detect a usage rate far from the target, a trigger fires a CloudWatch alarm that in turn triggers table autoscaling (the autoscaling feature pricing is based only on the pricing of the involved resources, see [here](https://aws.amazon.com/autoscaling/pricing/)). Therefore, this mechanism suffers of a [warm-up period](https://theburningmonk.com/2017/08/the-problems-with-dynamodb-auto-scaling-and-how-it-might-be-improved/).

If an operation is requested but not performed on a provisioned table (e.g. no autoscaling, incoming rate greater than target, ...) will result as _throttled request_.

> Failed to set write capacity units to 5. Reason: Failed updating table: Subscriber limit exceeded: Provisioned throughput decreases are limited within a given UTC day. After the first 4 decreases, each subsequent decrease in the same UTC day can be performed at most once every 3600 seconds. Number of decreases today: 4

If operations traffic towards the table stops suddenly, autoscaling does its best to reduce provisioned capacity from current to the specified minimum (5 in the above example): after first 4 decreases, it is limited to 1 decrease per hour. This behaviour is somehow a "hidden cost" of provisioned mode: in such situations, you will be billed for an entire hour for the residual peak capacity, even if it is not needed anymore.

### Lambda trigger fails

Assume you have the following scenario:
 
- an on-demand dynamo table
- Dynamo stream enabled with `NEW_IMAGE` mode (stream contains only records _after_ table updates)
- a trigger for a consequent operation implemented by Lambda function watching the stream with `batch_size = 1` and `latest starting position`

!!! question
	What if the Lambda function fails for any reason?

Standard Lambda functions have a 3x retry policy. But when it comes to Lambda watching streams, as stated [here](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-api) and [here](https://aws.amazon.com/lambda/faqs/?nc1=h_ls):

> If the invocation for one record times out, is throttled, or encounters any other error, Lambda will retry until it succeeds (or the record reaches its 24-hour expiration).
>
> If your function returns an error, Lambda retries the batch until processing succeeds or the data expires. To avoid stalled shards, you can configure the event source mapping to retry with a smaller batch size, limit the number of retries, or discard records that are too old.

To customize this behaviour you can specify `DynamoEventSource` parameters as suggested in the [docs](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping) and as available in [CDK](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda_event_sources/DynamoEventSource.html) - in particular:

- `retry_attempts`: Maximum number of retry attempts Valid Range: \*. Minimum value of 0 \*. Maximum value of 10000. Default: - retry until the record expires
- `max_record_age`: The maximum age of a record that Lambda sends to a function for processing. Valid Range: - Minimum value of 60 seconds - Maximum value of 7 days Default: - the retention period configured on the stream

### Main takeaways

- on-demand mode lets you pay for what you actually use, ensuring no performance issue at the cost of an higher price-point
- provisioned mode essentially limits operations costs while turning on user-side the possible performance degradation

## Notes

1. [`put_df`](https://aws-data-wrangler.readthedocs.io/en/2.4.0-docs/stubs/awswrangler.dynamodb.put_df.html#awswrangler.dynamodb.put_df) method of AWS Data Wrangler is nothing but a wrapper of boto3 [`batch_write_item`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.batch_write_item)
2. using the above method to write on Dynamo a Pandas Dataframe coming from `pd.read_json` requires you to cast `np.array` to `list` as well as `float` to [`Decimal`](https://docs.python.org/3/library/decimal.html)
3. each read operation performed via [query](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.query) can be monitored in terms of consumed RCU by parsing the related response looking for `ConsumedCapacity` field

### AWS CDK

To give write (resp. read) permission to a Lambda on a Dynamo table, both the [CDK docs](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_dynamodb/Table.html#aws_cdk.aws_dynamodb.Table.grant_write_data) and [some snippets](https://github.com/aws-samples/aws-cdk-examples/blob/master/python/dynamodb-lambda/dynamodb_lambda/dynamodb_lambda_stack.py) refer to `grant_write_data` method of the table.

This method should ensure:

1. Lambda permission to perform operations on the table
2. Lambda access to the (possible) KMS key for encrypt/decrypt operations

For the latter there is [this issue](https://github.com/aws/aws-cdk/issues/10010) though, which demonstrates the additional need for:

```python
if table.encryption_key:
    table.encryption_key.grant_decrypt(lambda)
```

## Resources

- [DynamoDB and auto-scaling docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)
- [AWS blog post about auto-scaling](https://aws.amazon.com/it/blogs/database/amazon-dynamodb-auto-scaling-performance-and-cost-optimization-at-any-scale/)
- [on-demand mode blog post](https://www.serverless.com/blog/dynamodb-on-demand-serverless)
- [pricing vs mode comparison](https://www.trek10.com/blog/findev-dynamodb-pricing-analysis)
- [on-demand mode stress tests](https://theburningmonk.com/2019/03/understanding-the-scaling-behaviour-of-dynamodb-ondemand-tables/)

[^1]: Reading operations which can suffer of latency if performed close to table updates, returning outdated records.
[^2]: Reading operations which are always up-to-date w.r.t. table updates.
