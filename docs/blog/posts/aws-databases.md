---
date: 2022-02-01
categories:
  - Guides
---

# AWS databases

<!-- more -->

Main databases types:

- **Relational**: data are stored in tabular form (rows and columns), where each row represents a unique _record_. Tables can be put in relation with each other through joins and queried via SQL;
- **Key-value**: non-relational database where each record stored as a unique _key_ with its associated value, resembling a dictionary-like structure;
- **Document**: semi-structured and hierarchical databases for catalogs and content management systems, often stored as JSON;
- **Graph**: the way the data are stored is graph-based, with nodes and edges connecting each data source with the others;
- **Time-series**: database optimized for records which indices are timestamps.

|   Service  |                      Type                     |            Query language              |                               Use cases                                   |
| -----------| --------------------------------------------- |----------------------------------------|---------------------------------------------------------------------------|
| Athena     | Structured, semi-structured and unstructured  | SQL based on HiveQL DDL and Presto DML | Log analysis, OLAP, BI                                                    |
| Aurora[^1] | Relational                                    | MySQL, PostgreSQL                      | eCommerce, CRM                                                            |
| DocumentDB | Document                                      | compatible with MongoDB query language | product catalogs, images and videos, application data platform            |
| DynamoDB   | Key-value                                     | NoSQL                                  | Mobile and web apps, gaming, IoT                                          |
| Neptune    | Graph                                         | GQL (Apache TinkerPop Gremlin, SPARQL) | Fraud detection, social netowkrs, knowledge graph, recommendation engines |
| Timestream | Time-series                                   | ANSI SQL                               | IoT, DevOps, telemetry, forecasting, analytics                            |
| RDS        | Relational                                    | SQL                                    | DWH, CRM                                                                  |
| Redshift   | Relational                                    | SQL based on PostgreSQL                | Large-scale DWH, data migration, OLAP                                     |

!!! warning "Warning"
    Athena and RDS are somewhat erroneously reported in the above table which refers to _databases_: a deep dive on the main differences is available below.

## Amazon RDS

From the [official docs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html):

> Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

Amazon RDS is not therefore a database engine itself, rather than a tool that helps in managing relational databases on AWS. Essentially, can be thought as an AWS-managed, generally purpose [RDBMS](https://en.wikipedia.org/wiki/Relational_database#RDBMS).

It allows to manage and run six database engines:

- Amazon Aurora
- MySQL
- MariaDB
- PostgreSQL
- Oracle
- Microsoft SQL Server

For a comparison between open source alternatives you can see [this page](/data-scientist-hub/notes/databases).

## Amazon Athena

Amazon Athena it's not a database engine itself but it's defined as an _interactive query service_ based on Apache Presto that makes easy to analyze data stored into S3 via SQL. This means that compute and storage are separate and managed independently.

It is completely serverless and cost-effective, and can be used together with AWS Glue - fully managed ETL service - which takes care of managing a related data catalog as a central source for metadata while preparing data for querying.

In contrast, efficient querying requires data to be _partitioned_ and purposely organized into S3 buckets upfront; moreover AWS Athena users compete for the same resources at the same time. While AWS provisions more resources as needed, it could mean that query performance fluctuates based on other users needs.

## Resources

- [Choosing an AWS database](https://www.jeffersonfrank.com/insights/choosing-an-aws-database)
- [Amazon Athena vs traditional databases](https://www.upsolver.com/blog/comparing-amazon-athena-traditional-databases)
- [CloudZero blog on Athena](https://www.cloudzero.com/blog/aws-athena)
- [AWS database comparison](https://www.justaftermidnight247.com/insights/rds-redshift-dynamodb-and-aurora-how-do-aws-managed-databases-compare/)

[^1]: can be run on both RDS and as Aurora _serverless_.
