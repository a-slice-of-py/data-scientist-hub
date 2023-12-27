---
date: 2022-02-02
categories:
  - Learning
---

# Open source databases

<!-- more -->

## Relational

A brief comparison between open source relational databases is available below (full credits to [Soufiane L](https://stackshare.io/stackups/mariadb-vs-mysql-vs-postgresql)).

|          Feature         | MariaDB[^1] | MySQL | PostgreSQL[^2] |
|--------------------------|:-----------:|:-----:|:--------------:|
| Materialized Views       |    ❌      |  ❌   |     ✔️         |
| Partial Indexes          |    ❌      |  ❌   |     ✔️         |
| Array Data Type          |    ❌      |  ❌   |     ✔️         |
| JSON Data Type           |    ✔️      |  ✔️   |     ✔️         |
| CHECK constraints        |    ✔️      |  ❌   |     ✔️         |
| Replication              |    ✔️      |  ✔️   |     ✔️         |
| Full-Text Search         |    ✔️      |  ✔️   |     ✔️         |
| UPSERT                   |    ✔️      |  ✔️   |     ✔️         |
| Common Table Expressions |    ✔️      |  ✔️   |     ✔️         |
| Sequences                |    ✔️      |  ❌   |     ✔️         |
| Table Partitioning       |    ✔️      |  ✔️   |     ❌         |

## Resources

- [MariaDB vs PostgreSQL](https://hevodata.com/learn/mariadb-vs-postgresql/)
- [Open source databases comparison](https://opensource.com/article/19/1/open-source-databases)

[^1]: based on MySQL and created after its acquisition by Oracle.
[^2]: PostgreSQL is generally considered to be the fastest one in terms of read/write speed.
