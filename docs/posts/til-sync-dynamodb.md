---
date: 2024-01-02
authors:
  - silvio
categories:
  - TIL
tags:
  - AWS
  - Database  
---

# Cross-account full table copy options for Amazon DynamoDB

There are several recommended options to perform a [cross-account full copy of a DynamoDB table](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/welcome.html).

It seems reasonable to compare these options based on several different properties: setup time _(low is better)_, approach _(serverless is better)_, involved resources _(few is better)_, costs estimate _(low is better)_ and new code possibly required _(none is better)_.

<!-- more -->

Given the above requirements, one of the best available option seems to be [the one based on AWS Backup](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-amazon-dynamodb-tables-across-accounts-using-aws-backup.html). This solution requires to enable _cross-account backup_ in AWS Backup, but this particular feature might not be available in a developer's hands (e.g. for security or compliance reasons).

The second best might be [this other approach based on Spark jobs handled by Glue](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/src-sink.html). Basically, this requires to create:

- in the _target_ account:
    - a policy which gives write permission to the target DynamoDB table[^1];
    - a (cross-account) role with the source account as trusted entity, equipped with the above policy;
- in the _source_ account:
    - a policy which grants `sts:AssumeRole` on the above mentioned cross-account role;
    - a role with AWS Glue as principal, equipped with the above policy and read permissions on the source DynamoDB table and S3[^2];
    - a Glue job as described [here](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-dynamo-db-cross-account.html) in the section _"For a read and cross-account write across regions"_, equipped with the above role.

!!! tip "How to handle throttled requests"

    With this solution, Glue will generate a high rate of write operations, which might led to throttled requests. To avoid `DynamoDB write exceeds max retry` kind of error, two possible solutions are:

    - increase the number of retries to handle possible throttled DynamoDB write operations to the target table, as suggested [here](https://repost.aws/questions/QUCQVFPbL7T5qv5DKiPi9B9Q/aws-glue-ddb-write-dynamic-frame-from-options-fails-with-requests-throttled);
    - prepare the target table with a ["pre-warm" phase](https://stackoverflow.com/questions/75321823/why-is-dynamodb-sets-read-write-capacity-for-the-on-demand-table).

For reference, a test made with a 4,5 GB table took about 35 minutes, generating a total cost of 17 USD:

- 7,4 USD for the execution of the Glue job (source account)
- 2 USD for the read operations onto the source DynamoDB table (source account)
- 7,6 USD for the write operations onto the target DynamoDB table (target account)

[^1]: This table must already exists.
[^2]: This is needed to let Glue download the job script from S3 assets bucket.
