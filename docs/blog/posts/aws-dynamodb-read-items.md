---
date: 2023-01-09
authors:
  - silvio
categories:
  - Announcements
tags:
  - AWS
  - Database
  - Open Source
  - Python
---

# Read DynamoDB table items into a Pandas Dataframe

For all the Python developers working on AWS: have you ever wanted to easily read a DynamoDB table directly into a pandas DataFrame?

Check out the latest release of [AWS SDK for pandas](https://github.com/aws/aws-sdk-pandas/releases/tag/2.19.0) (formerly AWS Data Wrangler), where I contributed with a brand new read method for DynamoDB module!

<!-- more -->

## Features

- automatically switch between available DynamoDB read actions, choosing the optimal one (aka "no more headaches fighting with boto3") as defined in this hierarchy `get_item > batch_get_item > query > scan` (inspiration from [here](https://dynobase.dev/dynamodb-scan-vs-query/) and [here](https://github.com/bykka/dynamoit))
- support filtering both on keys and attributes
- automatically sanitize [DynamoDB reserved keywords](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)
- prevent unwanted full table scan
- allow attributes selection via columns kwarg
- support limiting the number of returned items with the `max_items_evaluated` kwarg (a sort of an `head()` method for the table!)
- ...and more!

Read here the full [API reference](https://aws-sdk-pandas.readthedocs.io/en/stable/stubs/awswrangler.dynamodb.read_items.html#awswrangler.dynamodb.read_items).

## History

I found myself putting some effort in trying to handle reading items from a DynamoDB table and returning a Pandas Dataframe. Basically, I wanted to abstract some complexity away from available Boto3 read actions, and handle once for all the headache of thinking about keys, query, scan, etc.: since I was pretty happy with the result, I decided to submit a PR with a candidate for `wr.dynamodb.read_items` in [aws/aws-sdk-pandas#1867](https://github.com/aws/aws-sdk-pandas/issues/1867).

I was aware of the addition of `wr.dynamodb.read_partiql_query` in [aws/aws-sdk-pandas#1390](https://github.com/aws/aws-sdk-pandas/pull/1390), as well as the related issues as reported in [aws/aws-sdk-pandas#1571](https://github.com/aws/aws-sdk-pandas/issues/1571), but the proposed solution does not involve PartiQL: my goal was to avoid as much as possible the risks that come with its usage towards a DynamoDB table, regarding possible translation of a given query to a full scan op (see for example the disclaimer in the [docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.select.html)).
