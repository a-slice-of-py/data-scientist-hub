# Data Engineering

## Data Architecture

- [10 characteristics of a modern data architecture](https://www.eckerson.com/articles/ten-characteristics-of-a-modern-data-architecture)
- [Modern data architecture schema](https://s3.amazonaws.com/eckerson/assets/files/000/000/235/original/RackMultipart20180125-15584-mvyoc.jpg?1516917446)
- [Data pipelines](https://pub.towardsai.net/diving-into-data-pipelines-b2eb1b8a4923)
- [Data Engineering blog posts by Robin Linacre](https://www.robinlinacre.com/)
- [Databases and Data Modelling: a quick crash course](https://towardsdatascience.com/databases-and-data-modelling-a-quick-crash-course-546891a49b67)
- [System Design: ElasticSearch](https://towardsdatascience.com/system-design-cheatsheets-elasticsearch-673b98eebfff)
- [Architecture based on feedback loops](https://aws.amazon.com/it/blogs/architecture/establishing-feedback-loops-based-on-the-aws-well-architected-framework-review/)

## Basics

- [Python for Data Engineers](https://towardsdatascience.com/python-for-data-engineers-f3d5db59b6dd)
- [JSON Lines](https://medium.com/hackernoon/json-lines-format-76353b4e588d)
- [Modern Data Engineering](https://towardsdatascience.com/modern-data-engineering-e202776fb9a9)
- [Introduction to Streaming Frameworks](https://towardsdatascience.com/introduction-to-streaming-frameworks-d612583a3246)
- [Data Engineering Design Patterns](https://www.dedp.online/)
- [Airbyte Data Glossary](https://glossary.airbyte.com/)
- [Modern Data Engineering](https://moderndataengineering.substack.com/)

### Data Engineering Vault

- [Data Engineering Vault](https://www.ssp.sh/brain/data-engineering/)
- [The Data Engineering Toolkit: Essential Tools for Your Machine](https://www.ssp.sh/blog/data-engineering-toolkit/)
- [BI-as-Code and the New Era of GenBI](https://www.ssp.sh/blog/bi-as-code-and-genbi/)
- [Modern Data Stack: The Struggle of Enterprise Adoption](https://www.ssp.sh/blog/modern-data-stack-struggle-of-enterprise-adoption/)
- [Data Lake and Lakehouse Guide: Powered by Data Lake Table Formats (Delta Lake, Iceberg, Hudi)](https://www.ssp.sh/blog/data-lake-lakehouse-guide/)
- [Data Modeling – The Unsung Hero of Data Engineering: An Introduction to Data Modeling (Part 1)](https://www.ssp.sh/blog/data-modeling-for-data-engineering-introduction/)
- [Data Engineering Design Patterns (DEDP) book](https://www.dedp.online/about-this-book.html)
- [The Rise of the Declarative Data Stack](https://www.ssp.sh/blog/rise-of-declarative-data-stack/)
- [The Rise of the Semantic Layer](https://www.ssp.sh/blog/rise-of-semantic-layer-metrics/)

## Data catalog

- [lakekeeper: lakekeeper is an Apache-Licensed, secure, fast and easy to use Apache Iceberg REST Catalog written in Rust](https://github.com/lakekeeper/lakekeeper)

## Data Structures

- [Tensors vs Tables](https://earthmover.io/blog/tensors-vs-tables/)

## Database

- [TimescaleDB](https://github.com/timescale/timescaledb)
- [LanceDB: Developer-friendly, serverless vector database for AI applications](https://github.com/lancedb/lancedb)
- [sqlite-vec: a vector search SQLite extension that runs anywhere!](https://github.com/asg017/sqlite-vec/tree/main)
- [OpenDAL](https://github.com/apache/opendal)
- [JameSQL: an in-memory NoSQL database implemented in Python](https://github.com/capjamesg/jamesql)
- [icechunk: open-source, cloud-native transactional tensor storage engine](https://github.com/earth-mover/icechunk)
- [xarray: N-D labeled arrays and datasets in Python](https://github.com/pydata/xarray)
- [zarr-python: an implementation of chunked, compressed, N-dimensional arrays for Python](https://github.com/zarr-developers/zarr-python)
- [drawdb: free, simple, and intuitive online database diagram editor and SQL generator](https://github.com/drawdb-io/drawdb)

### DuckDB

- [DuckDB and Motherduck serverless analytics platform](https://motherduck.com/)
- [DuckDB: open source OLAP database](https://github.com/duckdb/duckdb)
- [QuackOSM: an open-source Python and CLI tool for reading OpenStreetMap PBF files using DuckDB](https://github.com/kraina-ai/quackosm)
- [DuckDB Doesn’t Need Data To Be a Database](https://www.nikolasgoebel.com/2024/05/28/duckdb-doesnt-need-data.html)
- [mosaic: an extensible framework for linking databases and interactive views](https://github.com/uwdata/mosaic)
- [Graph components with DuckDB](https://maxhalford.github.io/blog/graph-components-duckdb/)
- [Friendly SQL in DuckDB](https://duckdb.org/docs/sql/dialect/friendly_sql)
- [DuckDB blog: Friendly Lists and Their Buddies, the Lambdas](https://duckdb.org/2024/08/08/friendly-lists-and-their-buddies-the-lambdas)
- [DuckDB Tricks](https://duckdb.org/2024/08/19/duckdb-tricks-part-1)
- [Moving from Pandas to DuckDB](https://ai.gopubby.com/moving-from-pandas-to-duckdb-3ba10903ec13)
- [DuckERD: a CLI tool for generating ERD diagrams from DuckDB databases](https://github.com/tobilg/duckerd)
- [DuckDB in Python in the Browser with Pyodide, PyScript and JupyterLite](https://duckdb.org/2024/10/02/pyodide.html)
- [A Beginner's Guide to DuckDB's Python Client](https://github.com/mebauer/duckdb-python-basics)
- [Ducklake: A journey to integrate DuckDB with Unity Catalog](https://xebia.com/blog/ducklake-a-journey-to-integrate-duckdb-with-unity-catalog/)
- [15+ companies using duckdb in production: a comprehensive guide](https://motherduck.com/blog/15-companies-duckdb-in-prod/)
- [Mastering DuckDB when you're used to pandas or Polars](https://labs.quansight.org/blog/duckdb-when-used-to-frames)
- [Instant SQL is here: speedrun ad-hoc queries as you type](https://motherduck.com/blog/introducing-instant-sql/)

## ACID

- [deltabase: a lightweight, comprehensive solution for managing delta tables built on polars and deltalake](https://github.com/uname-n/deltabase)
- [strava-datastack: a modern Strava data pipeline fueled by dlt, duckdb, dbt, and evidence.dev](https://github.com/datadisciple/strava-datastack)

### Apache Iceberg

- [Apache Iceberg O'Reilly Training](https://github.com/wssbck/training-oreilly-iceberg)
- [AWS Apache Iceberg technical guide](https://aws.amazon.com/it/blogs/big-data/understanding-apache-iceberg-on-aws-with-the-new-technical-guide/)
- [Apache Polaris: the interoperable, open source catalog for Apache Iceberg](https://github.com/apache/polaris)
- [4 hours learning Apache Iceberg](https://vutr.substack.com/p/i-spent-8-hours-learning-apache-iceberg)
- [7 hours learning Apache Iceberg](https://vutr.substack.com/p/i-spent-7-hours-diving-deep-into)

### Apache DataFusion

- [Apache DataFusion in Python](https://datafusion.apache.org/python/user-guide/common-operations/basic-info.html)

## Monitoring

- [SLA, SLO and SLI for data teams](https://towardsdatascience.com/its-time-to-set-sla-slo-sli-for-your-data-team-only-3-steps-ed3c93009aa5)

## OS

- [Tech info about operating systems](https://towardsdatascience.com/all-you-should-know-about-operating-systems-in-technical-interviews-4dcc55210fea)

## Rest API

- [Intro](https://towardsdatascience.com/introduction-to-rest-apis-90b5d9676004)
- [How to (and how not to) design REST APIs](https://github.com/stickfigure/blog/wiki/How-to-(and-how-not-to)-design-REST-APIs)

## Tools

- [Luigi](https://luigi.readthedocs.io/en/stable/index.html)
- [d6t](https://github.com/d6t/d6t-python)
- [Metaflow](https://towardsdatascience.com/learn-metaflow-in-10-mins-netflixs-python-r-framework-for-data-scientists-2ef124c716e4)
- [Airflow](https://airflow.apache.org/docs/stable/start.html)
- [Dagster](https://dagster.io/)
- [GPU](https://towardsdatascience.com/the-ai-illustrated-guide-why-are-gpus-so-powerful-99f4ae85a5c3)
- [Observer pattern vs Pub Sub pattern](https://medium.com/towards-artificial-intelligence/observer-pattern-vs-pub-sub-pattern-7f467bcf5fe)
- [Prefect](https://docs.prefect.io/core/getting_started/why-not-airflow.html#overview)
- [Ray](https://github.com/ray-project/ray)
- [Splink: probabilistic data linkage at scale](https://moj-analytical-services.github.io/splink/index.html)
- [Haystack: an end-to-end framework for production-ready search pipelines](https://github.com/deepset-ai/haystack)
- [filequery: Query CSV and Parquet files using SQL](https://github.com/MarkyMan4/filequery)
- [dbt (data build tools): a command line tool to transform data more effectively](https://docs.getdbt.com/)
- [dlt: an open-source library to load data from various and often messy data sources into well-structured, live datasets](https://dlthub.com/docs/intro)
- [Trilogy Python Semantic Layers](https://trilogydata.dev/thesis/#python-semantic-layers)
- [yato: yet another transformation orchestrator](https://github.com/Bl3f/yato)
- [xorq: deferred computational framework for multi-engine pipelines](https://github.com/xorq-labs/xorq)

### Search engines

- [Approaching Relevance Challenges in Elasticsearch Query Construction](https://towardsdatascience.com/a-site-search-engineers-journal-approaching-relevance-challenges-in-elasticsearch-query-1eca29283da5)

## Unit testing

- [Test driven development and triangulation](https://www.programmersought.com/article/33612342389/)

