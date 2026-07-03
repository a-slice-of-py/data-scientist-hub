---
date: 2024-12-10
authors:
  - silvio
categories:
  - QFTB
---

# Quotes From The Book - part 5 - Fundamentals of Data Engineering

Over the past two years I had the chance to read a bunch of data-related books on the O'Reilly learning platform: what follows is a collection of quotes from _"Fundamentals of Data Engineering"_ by Joe Reis & Matt Housley that captured my attention or hit hard because they were highly relatable.

<!-- more -->

## Fundamentals of Data Engineering

### 1. Data Engineering Described

> _Business never sleeps, and business stakeholders often have a significant backlog of things they want to address and new initiatives they want to launch._

---

> _If data engineers do their job and collaborate successfully, data scientists shouldn’t spend their time collecting, cleaning, and preparing data after initial exploratory work. Data engineers should automate this work as much as possible._

---

> _Whereas data scientists are forward-looking, a data analyst typically focuses on the past or present._

---

> _A data analyst’s typical downstream customers are business users, management, and executives._

---

> _The need for production-ready data science is a significant driver behind the emergence of the data engineering profession. Data engineers should help data scientists to enable a path to production. In fact, we (the authors) moved from data science to data engineering after recognizing this fundamental need. Data engineers work to provide the data automation and scale that make data science more efficient._

---

> _The data engineer is a hub between data producers, such as software engineers, data architects, and DevOps or site-reliability engineers (SREs), and data consumers, such as data analysts, data scientists, and ML engineers_

---

> _An internal-facing data engineer typically focuses on activities crucial to the needs of the business and internal stakeholders (Figure 1-11). Examples include creating and maintaining data pipelines and data warehouses for BI dashboards, reports, business processes, data science, and ML models._

---

> _External-facing data engineering comes with a unique set of problems. External-facing query engines often handle much larger concurrency loads than internal-facing systems. Engineers also need to consider putting tight limits on queries that users can run to limit the infrastructure impact of any single user. In addition, security is a much more complex and sensitive problem for external queries, especially if the data being queried is multitenant (data from many customers and housed in a single table)._

---

> _In data science, there’s the notion of type A and type B data scientists.10 Type A data scientists—where A stands for analysis—focus on understanding and deriving insight from data. Type B data scientists—where B stands for building—share similar backgrounds as type A data scientists and possess strong programming skills. The type B data scientist builds systems that make data science work in production._

---

> _It’s known as “the second-best language at everything.” Python underlies popular data tools_

---

> _Data engineers remain software engineers, in addition to their many other roles_

### 2. The Data Engineering Lifecycle

> _Before data engineers begin engineering new internal tools, they would do well to survey the landscape of publicly available tools. Keep an eye on the total cost of ownership (TCO) and opportunity cost associated with implementing a tool. There is a good chance that an open source project already exists to address the problem they’re looking to solve, and they would do well to collaborate rather than reinventing the wheel._

---

> _DataOps has three core technical elements: automation, monitoring and observability, and incident response_

---

> _Whereas data’s ethical and privacy implications were once considered nice to have, like security, they’re now central to the general data lifecycle. Data engineers need to do the right thing when no one else is watching, because everyone will be watching someday.6_

---

> _Data destruction is straightforward in a cloud data warehouse. SQL semantics allow deletion of rows conforming to a where clause. Data destruction was more challenging in data lakes, where write-once, read-many was the default storage pattern. Tools such as Hive ACID and Delta Lake allow easy management of deletion transactions at scale. New generations of metadata management, data lineage, and cataloging tools will also streamline the end of the data engineering lifecycle_

---

> _To derive business insights from data, through business analytics and data science, the data must be in a usable form. The process for converting data into a usable form is known as data modeling and design. Whereas we traditionally think of data modeling as a problem for database administrators (DBAs) and ETL developers, data modeling can happen almost anywhere in an organization. Firmware engineers develop the data format of a record for an IoT device, or web application developers design the JSON response to an API call or a MySQL table schema—these are all instances of data modeling and design._

---

> _Data quality sits across the boundary of human and technology problems_

---

> _According to Data Governance: The Definitive Guide, data quality is defined by three main characteristics:_

---

> _Managing data quality is tough if no one is accountable for the data in question_

---

> _Managing data quality is tough if no one is accountable for the data in question._

---

> _In addition, the responsible person generally doesn’t have all the resources necessary to maintain data quality. Instead, they coordinate with all people who touch the data, including data engineers._

---

> _Data should conform to the expectations in the business metadata._

---

> _Data engineers must understand both data and access security, exercising the principle of least privilege. The principle of least privilege means giving a user or system access to only the essential data and resources to perform an intended function._

---

> _Imposing the principle of least privilege on ourselves can prevent accidental damage and keep you in a security-first mindset._

---

> _Data security is also about timing—providing data access to exactly the people and systems that need to access it and only for the duration necessary to perform their work._

---

> _Without a framework for managing data, data engineers are simply technicians operating in a vacuum_

---

> _The core categories of data governance are discoverability, security, and accountability.2 Within these core categories are subcategories, such as data quality, metadata, and privacy_

---

> _Reference metadata is data used to classify other data. This is also referred to as lookup data. Standard examples of reference data are internal codes, geographic codes, units of measurement, and internal calendar standards. Note that much of reference data is fully managed internally, but items such as geographic codes might come from standard external references._

---

> _Data has a social element; each organization accumulates social capital and knowledge around processes, datasets, and pipelines._

---

> _Data governance is, first and foremost, a data management function to ensure the quality, integrity, security, and usability of the data collected by an organization_

---

> _Reverse ETL takes processed data from the output side of the data engineering lifecycle and feeds it back into source systems_

---

> _Internal BI faces a limited audience and generally presents a limited number of unified views. Access controls are critical but not particularly complicated. Access is managed using a handful of roles and access tiers._
>
> _With embedded analytics, the request rate for reports, and the corresponding burden on analytics systems, goes up dramatically; access control is significantly more complicated and critical. Businesses may be serving separate analytics and data to thousands or more customers. Each customer must see their data and only their data. An internal data-access error at a company would likely lead to a procedural review. A data leak between customers would be considered a massive breach of trust, leading to media attention and a significant loss of customers._

---

> _operational analytics is focused on the present and doesn’t necessarily concern historical trends_

---

> _business logic is often applied to data in the transformation stage of the data engineering lifecycle, but a logic-on-read approach has become increasingly popular._

---

> _Data vanity projects are a major risk for companies. Many companies pursued vanity projects in the big data era, gathering massive datasets in data lakes that were never consumed in any useful way. The cloud era is triggering a new wave of vanity projects built on the latest data warehouses, object storage systems, and streaming technologies._

---

> _Data modeling is critical for obtaining a clear and current picture of business processes. A simple view of raw retail transactions might not be useful without adding the logic of accounting rules_

---

> _Logically, we treat transformation as a standalone area of the data engineering lifecycle, but the realities of the lifecycle can be much more complicated in practice. Transformation is often entangled in other phases of the lifecycle._

---

> _some questions to ask yourself when determining whether streaming ingestion is an appropriate choice over batch ingestion:_

---

> _batch versus streaming and push versus pull_

---

> _some primary questions about the ingestion stage:_

---

> _source systems and ingestion represent the most significant bottlenecks of the data engineering lifecycle_

---

> _a few key engineering questions to ask when choosing a storage system for a data warehouse, data lakehouse, database, or object storage_

---

> _a starting set of evaluation questions of source systems that data engineers must consider_

---

> _In general, the middle stages—storage, ingestion, transformation—can get a bit jumbled. And that’s OK. Although we split out the distinct parts of the data engineering lifecycle, it’s not always a neat, continuous flow. Various stages of the lifecycle may repeat themselves, occur out of order, overlap, or weave together in interesting and unexpected ways._

### 3. Choosing Technologies Across the Data Engineering Lifecycle

> _Bigger companies may still employ data architects, but those architects will need to be heavily in tune and current with the state of technology and data. Gone are the days of ivory tower data architecture. In the past, architecture was largely orthogonal to engineering. We expect this distinction will disappear as data engineering, and engineering in general, quickly evolves, becoming more agile, with less separation between engineering and architecture._
>
> _Ideally, a data engineer will work alongside a dedicated data architect. However, if a company is small or low in its level of data maturity, a data engineer might work double duty as an architect. Because data architecture is an undercurrent of the data engineering lifecycle, a data engineer should understand “good” architecture and the various types of data architecture._

---

> _the diversity of IoT systems and environments presents complications—e.g., late-arriving data, data structure and schema disparities, data corruption, and connection disruption—that engineers must account for in their architectures and downstream analytics._

---

> _An IoT gateway is a hub for connecting devices and securely routing devices to the appropriate destinations on the internet. While you can connect a device directly to the internet without an IoT gateway, the gateway allows devices to connect using extremely little power. It acts as a way station for data retention and manages an internet connection to the final data destination._

---

> _Any device capable of collecting data from its environment is an IoT device._
>
> _Devices should be minimally capable of collecting and transmitting data. However, the device might also crunch data or run ML on the data it collects before sending it downstream—edge computing and edge machine learning, respectively._

---

> _The philosophy of “batch as a special case of streaming” is now more pervasive._

---

> _As cloud data warehouses (and data lakes) mature, the line between the data warehouse and the data lake will continue to blur._

---

> _Data lake 1.0 started with HDFS. As the cloud grew in popularity, these data lakes moved to cloud-based object storage, with extremely cheap storage costs and virtually limitless storage capacity. Instead of relying on a monolithic data warehouse where storage and compute are tightly coupled, the data lake allows an immense amount of data of any size and type to be stored. When this data needs to be queried or transformed, you have access to nearly unlimited computing power by spinning up a cluster on demand, and you can pick your favorite data-processing technology for the task at hand—MapReduce, Spark, Ray, Presto, Hive, etc._
>
> _Despite the promise and hype, data lake 1.0 had serious shortcomings. The data lake became a dumping ground; terms such as data swamp, dark data, and WORN were coined as once-promising data projects failed. Data grew to unmanageable sizes, with little in the way of schema management, data cataloging, and discovery tools. In addition, the original data lake concept was essentially write-only, creating huge headaches with the arrival of regulations such as GDPR that required targeted deletion of user records._

---

> _Simple data manipulation language (DML) operations common in SQL—deleting or updating rows—were painful to implement, generally achieved by creating entirely new tables_

---

> _Processing data was also challenging. Relatively banal data transformations such as joins were a huge headache to code as MapReduce jobs._

---

> _Databricks introduced the notion of a data lakehouse. The lakehouse incorporates the controls, data management, and data structures found in a data warehouse while still housing data in object storage and supporting a variety of query and transformation engines. In particular, the data lakehouse supports atomicity, consistency, isolation, and durability (ACID) transactions, a big departure from the original data lake, where you simply pour in data and never update or delete it. The term data lakehouse suggests a convergence between data lakes and data warehouses._

---

> _The technical architecture of cloud data warehouses has evolved to be very similar to a data lake architecture._

---

> _The tight coupling of a monolith implies a lack of modularity of its components. Swapping out or upgrading components in a monolith is often an exercise in trading one pain for another. Because of the tightly coupled nature, reusing components across the architecture is difficult or impossible. When evaluating how to improve a monolithic architecture, it’s often a game of whack-a-mole: one component is improved, often at the expense of unknown consequences with other areas of the monolith._

---

> _Those who handle data must assume that they are ultimately responsible for securing it_

---

> _Bezos API Mandate_

---

> _Improving the development team’s ability gives an architect much greater leverage than being the sole decision-maker and thus running the risk of being an architectural bottleneck._

---

> _Data architects should be highly technically competent but delegate most individual contributor work to others._

---

> _key terms for evaluating failure scenarios_

---

> _these principles of data engineering architecture_

---

> _Agility is the foundation for good data architecture; it acknowledges that the world is fluid. Good data architecture is flexible and easily maintainable_

---

> _Architecture represents the significant design decisions that shape a system, where significant is measured by cost of change.”_

---

> _reversible decisions helps overcome this tendency by reducing the risk attached to a decision._

---

> _Enterprise architecture is the design of systems to support change in the enterprise, achieved by flexible and reversible decisions reached through careful evaluation of trade-offs._

### 4. Ingestion

> _The data-tool landscape has seen exponential growth over the last several years. Every day, new independent offerings arise for data tools. With the ability to raise funds from VCs flush with capital, these data companies can scale and hire great engineering, sales, and marketing teams. This presents a situation where users have some great product choices in the marketplace while having to wade through endless sales and marketing clutter._

---

> _This is a widespread trend: an OSS project becomes popular, an affiliated company raises truckloads of venture capital (VC) money to commercialize the OSS project, and the company scales as a fast-moving rocket ship._

---

> _A new generation of “cloud of clouds” services aims to facilitate multicloud with reduced complexity by offering services across clouds and seamlessly replicating data between clouds or managing workloads on several clouds through a single pane of glass_

---

> _This pattern of putting analytics in the cloud is beautiful because data flows primarily in one direction, minimizing data egress costs (Figure 4-3). That is, on-premises applications generate event data that can be pushed to the cloud essentially for free. The bulk of data remains in the cloud where it is analyzed, while smaller amounts of data are pushed back to on premises for deploying models to applications, reverse ETL, etc._

---

> _Data gravity is real: once data lands in a cloud, the cost to extract it and migrate processes can be very high._

---

> _The key to finding value in the cloud is understanding and optimizing the cloud pricing model._

---

> _the belief that cloud services are just like familiar on-premises servers is a widespread cognitive error that plagues cloud migrations and leads to horrifying bills. This demonstrates a broader issue in tech that we refer to as the curse of familiarity. Many new technology products are intentionally designed to look like something familiar to facilitate ease of use and accelerate adoption. But, any new technology product has subtleties and wrinkles that users must learn to identify, accommodate, and optimize._

---

> _Much like traders of financial derivatives, cloud vendors also deal in risk. In the case of archival storage, vendors are selling a type of insurance, but one that pays out for the insurer rather than the policy buyer in the event of a catastrophe. While data storage costs per month are extremely cheap, I risk paying a high price if I ever need to retrieve data. But this is a price that I will happily pay in a true emergency._

---

> _many cloud services are similar to financial derivatives_

---

> _you need to know how clouds make money_

---

> _Many people quibble with the term serverless; after all, the code must run somewhere. In practice, serverless usually means many invisible servers._

---

> _The early cloud era was dominated by infrastructure as a service (IaaS) offerings—products such as VMs and virtual disks that are essentially rented slices of hardware. Slowly, we’ve seen a shift toward platform as a service (PaaS), while SaaS products continue to grow at a rapid clip._

---

> _Today Versus the Future: Immutable Versus Transitory Technologies_

---

> _If it seems that FinOps is about saving money, then think again. FinOps is about making money. Cloud spend can drive more revenue, signal customer base growth, enable more product and feature release velocity, or even help shut down a data center._

---

> _If you choose data stack A, you’ve chosen the benefits of data stack A over all other options, effectively excluding data stacks B, C, and D. You’re committed to data stack A and everything it entails—the team to support it, training, setup, and maintenance. What happens if data stack A was a poor choice? What happens when data stack A becomes obsolete? Can you still move to other data stacks?_
>
> _How quickly and cheaply can you move to something newer and better? This is a critical question in the data space, where new technologies and products seem to appear at an ever-faster rate. Does the expertise you’ve built up on data stack A translate to the next wave? Or are you able to swap out components of data stack A and buy yourself some time and options?_

---

> _Total opportunity cost of ownership (TOCO) is the cost of lost opportunities that we incur in choosing a technology, an architecture, or a process.1 Note that ownership in this setting doesn_

---

> _We sometimes see small data teams read blog posts about a new cutting-edge technology at a giant tech company and then try to emulate these same extremely complex technologies and practices. We call this cargo-cult engineering, and it’s generally a big mistake that consumes a lot of valuable time and money, often with little to nothing to show in return. Especially for small teams or teams with weaker technical chops, use as many managed and SaaS tools as possible, and dedicate your limited bandwidth to solving the complex problems that directly add value to the business._

---

> _Perfect is the enemy of good. Some data teams will deliberate on technology choices for months or years without reaching any decisions. Slow decisions and output are the kiss of death to data teams. We’ve seen more than a few data teams dissolve for moving too slow and failing to deliver the value they were hired to produce._

---

> _Expenses fall into two big groups: capital expenses and operational expenses._

---

> _Always be aware of how simple it will be to connect your various technologies across the data engineering lifecycle. As mentioned in other chapters, we suggest designing for modularity and giving yourself the ability to easily swap out technologies as new practices and alternatives become available_

---

> _some considerations for choosing data technologies across the data engineering lifecycle_

---

> _A lot of people confuse architecture and tools. Architecture is strategic; tools are tactical. We sometimes hear, “Our data architecture are tools X, Y, and Z.” This is the wrong way to think about architecture. Architecture is the high-level design, roadmap, and blueprint of data systems that satisfy the strategic aims for the business. Architecture is the what, why, and when. Tools are used to make the architecture a reality; tools are the how._

---

> _We strongly advise against choosing technology before getting your architecture right. Architecture first, technology second._

### 5. Ingestion

> _data engineers need to weave themselves into the DevOps practices of stakeholders, and vice versa. Successful DataOps works when all people are on board and focus on making systems holistically work_

---

> _Message queues are a critical ingredient for decoupled microservices and event-driven architectures. Some things to keep in mind with message queues are frequency of delivery, message ordering, and scalability._

---

> _a common workflow to get data from a CRM, blend the CRM data through the customer scoring model, and then use reverse ETL to send that data back into CRM for salespeople to contact better-qualified leads._

---

> _The consumerization of technology means every company is essentially now a technology company._

---

> _Webhooks are a simple event-based data-transmission pattern. The data source can be an application backend, a web page, or a mobile app. When specified events happen in the source system, this triggers a call to an HTTP endpoint hosted by the data consumer. Notice that the connection goes from the source system to the data sink, the opposite of typical APIs. For this reason, webhooks are often called reverse APIs._

---

> _GraphQL was created at Facebook as a query language for application data and an alternative to generic REST APIs. Whereas REST APIs generally restrict your queries to a specific data model, GraphQL opens up the possibility of retrieving multiple data models in a single request._

---

> _In some cases, APIs are merely a thin wrapper over internals that provides the minimum functionality required to protect the system from user requests. In other examples, a REST data API is a masterpiece of engineering that prepares data for analytics applications and supports advanced reporting._

---

> _REST stands for representational state transfer. This set of practices and philosophies for building HTTP web APIs was laid out by Roy Fielding in 2000 in a PhD dissertation. REST is built around HTTP verbs, such as GET and PUT; in practice, modern REST uses only a handful of the verb mappings outlined in the original dissertation._

---

> _Measurement data is generated regularly, such as temperature or air-quality sensors. Event-based data is irregular and created every time an event occurs—for instance, when a motion sensor detects movement._

---

> _A time-series database is optimized for retrieving and statistical processing of time-series data_

---

> _Text search involves searching a body of text for keywords or phrases, matching on exact, fuzzy, or semantically similar matches. Log analysis is typically used for anomaly detection, real-time monitoring, security analytics, and operational analytics. Queries can be optimized and sped up with the use of indexes._

---

> _Graph databases support rich data models for both nodes and edges._

---

> _graph databases are a good fit when you want to analyze the connectivity between elements._

---

> _To run analytics on document stores, engineers generally must run a full scan to extract all data from a collection or employ a CDC strategy to send events to a target stream_

---

> _document stores are generally not ACID compliant,_

---

> _Document databases generally embrace all the flexibility of JSON and don’t enforce schema or types; this is a blessing and a curse. On the one hand, this allows the schema to be highly flexible and expressive. The schema can also evolve as an application grows. On the flip side, we’ve seen document databases become absolute nightmares to manage and query. If developers are not careful in managing schema evolution, data may become inconsistent and bloated over time._

---

> _One key difference between relational databases and document stores is that the latter does not support joins. This means that data cannot be easily normalized, i.e., split across multiple tables._

---

> _a document is a nested object; we can usually think of each document as a JSON object for practical purposes. Documents are stored in collections and retrieved by key. A collection is roughly equivalent to a table in a relational database_

---

> _key-value stores can also serve applications requiring high-durability persistence. An ecommerce application may need to save and update massive amounts of event state changes for a user and their orders._

---

> _in-memory key-value databases are popular for caching session data for web and mobile applications, where ultra-fast lookup and high concurrency are required._

---

> _There are numerous flavors of NoSQL database designed for almost any imaginable use case. Because there are far too many NoSQL databases to cover exhaustively in this section, we consider the following database types: key-value, document, wide-column, graph, search, and time series._

---

> _NoSQL, which stands for not only SQL, refers to a whole class of databases that abandon the relational paradigm_

---

> _RDBMS systems are typically ACID compliant. Combining a normalized schema, ACID compliance, and support for high transaction rates makes relational database systems ideal for storing rapidly changing application states. The challenge for data engineers is to determine how to capture state information over time._

---

> _Each relation in the table has the same schema (a sequence of columns with assigned static types such as string, integer, or float)._

---

> _Each relation in the table has the same schema (a sequence of columns with assigned static types such as string, integer, or float)._

---

> _Tables are typically indexed by a primary key, a unique field for each row in the table._

---

> _Tables can also have various foreign keys—fields with values connected with the values of primary keys in other tables, facilitating joins, and allowing for complex schemas that spread data across multiple tables._

---

> _Relational databases_

---

> _Major considerations for understanding database technologies_

---

> _Always include timestamps for each phase through which an event travels._

---

> _By contrast, a stream is an append-only log of event records. (Streams are ingested and stored in event-streaming platforms, which we discuss at greater length in “Message Queues and Event-Streaming Platforms”.) As events occur, they are accumulated in an ordered sequence (Figure 5-5); a timestamp or an ID might order events. (Note that events aren’t always delivered in exact order because of the subtleties of distributed systems.)_

---

> _A message is typically sent through a message queue from a publisher to a consumer, and once the message is delivered, it is removed from the queue._

---

> _Insert-only has a couple of disadvantages. First, tables can grow quite large, especially if data frequently changes, since each change is inserted into the table. Sometimes records are purged based on a record sunset date or a maximum number of record versions to keep table size reasonable. The second disadvantage is that record lookups incur extra overhead because looking up the current state involves running MAX​(cre⁠ated_timestamp)._

---

> _the insert-only pattern maintains a database log directly in the table itself, making it especially useful if the application needs access to history._

---

> _Change data capture (CDC) is a method for extracting each change event (insert, update, delete) that occurs in a database. CDC is frequently leveraged to replicate between databases in near real time or create an event stream for downstream processing._
>
> _CDC is handled differently depending on the database technology. Relational databases often generate an event log stored directly on the database server that can be processed to create a stream. (See “Database Logs”.) Many cloud NoSQL databases can send a log or event stream to a target storage location._

---

> _an online analytical processing (OLAP) system is built to run large analytics queries and is typically inefficient at handling lookups of individual records_

---

> _OLAP to refer to any database system that supports high-scale interactive analytics queries; we are not limiting ourselves to systems that support OLAP cubes (multidimensional arrays of data). The online part of OLAP implies that the system constantly listens for incoming queries, making OLAP systems suitable for interactive analytics_

---

> _OLTP databases work well as application backends when thousands or even millions of users might be interacting with the application simultaneously, updating and writing data concurrently. OLTP systems are less suited to use cases driven by analytics at scale, where a single query must scan a vast amount of data_

### 6. Storage

> _define your storage infrastructure as code and use ephemeral compute resources when it’s time to process your data. Because storage is increasingly distinct from compute, you can automatically spin resources up and down while keeping your data in object storage. This keeps your infrastructure clean and avoids coupling your storage and query layers._

---

> _Back in the early days of “big data,” there was a tendency to err on the side of accumulating every piece of data possible, regardless of its usefulness. The expectation was, “we might need this data in the future.” This data hoarding inevitably became unwieldy and dirty, giving rise to data swamps and regulatory crackdowns on data retention, among other consequences and nightmares. Nowadays, data engineers need to consider data retention: what data do you need to keep, and how long should you keep it?_

---

> _Data is an asset, so you should know the value of the data you’re storing._

---

> _New data is typically more valuable and frequently accessed than older data._

---

> _good engineering must consider the entropic nature of data by actively seeking to understand its characteristics and watching for major changes. Engineers can monitor data statistics, apply anomaly detection methods or simple rules, and actively test and validate for logical inconsistencies_

---

> _Data engineers should take the lead on FinOps (cost management), security monitoring, and access monitoring._

---

> _DataOps concerns itself with traditional operational monitoring of storage systems and monitoring the data itself, inseparable from metadata and quality._

---

> _Any data with privacy implications has a lifecycle that data engineers must manage. Data engineers must be prepared to respond to data deletion requests and selectively remove data as required. In addition, engineers can accommodate privacy and security through anonymization and masking._

---

> _Metadata management also significantly enhances data governance. Beyond simply enabling passive data cataloging and lineage, consider implementing analytics over these systems to get a clear, active picture of what’s happening with your data_

---

> _Data is enhanced by robust metadata. Cataloging enables data scientists, analysts, and ML engineers by enabling data discovery. Data lineage accelerates the time to track down data problems and allows consumers to locate upstream raw sources_

---

> _implement automatic data lifecycle management practices and move the data to cold storage if you don’t need the data past the required retention date. Or delete data if it’s truly not needed._

---

> _Certain regulations (e.g., HIPAA and Payment Card Industry, or PCI) might require you to keep data for a certain time. In these situations, the data simply needs to be accessible upon request, even if the likelihood of an access request is low. Other regulations might require you to hold data for only a limited period of time, and you’ll need to have the ability to delete specific information on time and within compliance guidelines. You’ll need a storage and archival data process—along with the ability to search the data—that fits the retention requirements of the particular regulation with which you need to comply._

---

> _Hot data has instant or frequent access requirements._

---

> _Warm data is accessed semi-regularly_

---

> _Cold data is mainly meant for long-term archival, when there’s little to no intention to access the data_

---

> _Depending on how frequently data is accessed, we can roughly bucket the way it is stored into three categories of persistence: hot, warm, and cold._

---

> _Cloud-based systems based around object storage support zero-copy cloning. This typically means that a new virtual copy of an object is created (e.g., a new table) without necessarily physically copying the underlying data. Typically, new pointers are created to the raw data files, and future changes to these tables will not be recorded in the old table. For those familiar with the inner workings of object-oriented languages such as Python, this type of “shallow” copying is familiar from other contexts._

---

> _multitier caching, we utilize object storage for long-term data retention and access but spin up local storage to be used during queries and various stages of data pipelines._

---

> _In practice, we constantly hybridize colocation and separation to realize the benefits of both approaches._

---

> _a dramatic shift toward ephemerality._

---

> _Cloud object stores significantly mitigate the risk of data loss and generally provide extremely high uptime (availability)._

---

> _The performance benefits of temporarily operating at ultra-high scale can outweigh the bandwidth limitations of object storage_

---

> _If colocation of compute and storage delivers high performance, why the shift toward separation of compute and storage? Several motivations exist._

---

> _colocation allows fast, low-latency disk reads and high bandwidth._

---

> _Colocation of compute and storage has long been a standard method to improve database performance._

---

> _The principal advantage of schema on write is that it enforces data standards, making data easier to consume and utilize in the future. Schema on read emphasizes flexibility, allowing virtually any data to be written. This comes at the cost of greater difficulty consuming data in the future._

---

> _schema on read, the schema is dynamically created when data is written, and a reader must determine the schema when reading the data. Ideally, schema on read is implemented using file formats that implement built-in schema information, such as Parquet or JSON._

---

> _Schema on write is essentially the traditional data warehouse pattern: a table has an integrated schema; any writes to the table must conform. To support schema on write, a data lake must integrate a schema metastore._

---

> _Note that schema need not be relational. Rather, data becomes more useful when we have as much information about its structure and organization. For images stored in a data lake, this schema information might explain the image format, resolution, and the way the images fit into a larger hierarchy_

---

> _Data catalogs make metadata easily available to systems. For instance, a data catalog is a key ingredient of the data lakehouse, allowing table discoverability for queries._
>
> _Organizationally, data catalogs allow business users, analysts, data scientists, and engineers to search for data to answer questions. Data catalogs streamline cross-organizational communications and collaboration._

---

> _Data catalogs also typically provide a human access layer through a web interface, where users can search for data and view data relationships._

---

> _cataloging systems typically need to rely on an automated scanning layer that collects metadata from various systems such as data lakes, data warehouses, and operational databases. Data catalogs can collect existing metadata and may also use scanning tools to infer metadata such as key relationships or the presence of sensitive data._

---

> _data applications are designed to integrate with catalog APIs to handle their metadata and updates directly_

---

> _cataloging systems typically need to rely on an automated scanning layer that collects metadata from various systems such as data lakes, data warehouses, and operational databases. Data catalogs can collect existing metadata and may also use scanning tools to infer metadata such as key relationships or the presence of sensitive data._

---

> _Data catalogs typically work across operational and analytics data sources, integrate data lineage and presentation of data relationships, and allow user editing of data descriptions._
>
> _Data catalogs are often used to provide a central place where people can view their data, queries, and data storage_

---

> _A data catalog is a centralized metadata store for all data across an organization_

---

> _the notion of the data platform frankly has yet to be fully fleshed out. However, the race is on to create a walled garden of data tools, both simplifying the work of data engineering and generating significant vendor lock-in_

---

> _It is important to emphasize that much of the data in a data lakehouse may not have a table structure imposed. We can impose data warehouse features where we need them in a lakehouse, leaving other data in a raw or even unstructured format._
>
> _The data lakehouse technology is evolving rapidly. A variety of new competitors to Delta Lake have emerged, including Apache Hudi and Apache Iceberg_

---

> _In a data lakehouse architecture, various tools can connect to the metadata layer and read data directly from object storage_

---

> _The key advantage of the data lakehouse over proprietary tools is interoperability. It’s much easier to exchange data between tools when stored in an open file format_

---

> _architecture of the data lakehouse is similar to the architecture used by various commercial data platforms, including BigQuery and Snowflake. These systems store data in object storage and provide automated metadata management, table history, and update/delete capabilities. The complexities of managing underlying files and storage are fully hidden from the user_

---

> _The data lakehouse is an architecture that combines aspects of the data warehouse and the data lake. As it is generally conceived, the lakehouse stores data in object storage just like a lake. However, the lakehouse adds to this arrangement features designed to streamline data management and create an engineering experience similar to a data warehouse. This means robust table and schema support and features for managing incremental updates and deletes. Lakehouses typically also support table history and rollback; this is accomplished by retaining old versions of files and metadata._
>
> _A lakehouse system is a metadata and file-management layer deployed with data management and transformation tools. Databricks has heavily promoted the lakehouse concept with Delta Lake, an open source storage management system._

---

> _the popularity of separating storage from compute means the lines between OLAP databases and data lakes are increasingly blurring. Major cloud data warehouses and data lakes are on a collision course. In the future, the differences between these two may be in name only since they might functionally and technically be very similar under the hood_

---

> _data engineers discovered that much of the functionality offered by MPP systems (schema management; update, merge and delete capabilities) and initially dismissed in the rush to data lakes was, in fact, extremely useful. This led to the notion of the data lakehouse_

---

> _The limitation is that cloud data warehouses cannot handle truly unstructured data, such as images, video, or audio, unlike a true data lake. Cloud data warehouses can be coupled with object storage to provide a complete data-lake solution._

---

> _cloud data warehouses are often used to organize data into a data lake, a storage area for massive amounts of unprocessed raw data_

---

> _The storage abstraction you require as a data engineer boils down to a few key considerations_

---

> _partition a table into multiple subtables by splitting it on a field. It is quite common in analytics and data science use cases to scan over a time range, so date- and time-based partitioning is extremely common_

---

> _arranging data by column packs similar values next to each other, yielding high-compression ratios with minimal compression overhead. This allows data to be scanned more quickly from disk and over a network._

---

> _Indexes provide a map of the table for particular fields and allow extremely fast lookup of individual records. Without indexes, a database would need to scan an entire table to find the records satisfying a WHERE condition._
>
> _In most RDBMSs, indexes are used for primary table keys (allowing unique identification of rows) and foreign keys (allowing joins with other tables)._

---

> _Replay allows a streaming system to return a range of historical stored data._

---

> _Streaming data has different storage requirements than nonstreaming data. In the case of message queues, stored data is temporal and expected to disappear after a certain duration. However, distributed, scalable streaming frameworks like Apache Kafka now allow extremely long-duration streaming data retention. Kafka supports indefinite data retention by pushing old, infrequently accessed messages down to object storage._

---

> _HDFS is a key ingredient of many current big data engines, such as Amazon EMR. In fact, Apache Spark is still commonly run on HDFS clusters._

---

> _The Hadoop Distributed File System is based on Google File System (GFS) and was initially engineered to process data with the MapReduce programming model. Hadoop is similar to object storage but with a key difference: Hadoop combines compute and storage on the same nodes, where object stores typically have limited support for internal processing._

---

> _Engineers also have the option of deploying storage lifecycle policies. Lifecycle policies allow automatic deletion of old object versions when certain conditions are met (e.g., when an object version reaches a certain age or many newer versions exist)_

---

> _Keep in mind that we’re talking about brute-force object versioning. Object storage systems generally store full object data for each version, not differential snapshots._

---

> _The principal overhead that engineers need to consider with object versioning is the cost of storage. Historical versions of objects generally have the same associated storage costs as current versions. Object version costs may be nearly insignificant or catastrophically expensive,_

---

> _The consistency issue still exists when a client requests the “default” or “latest” version of an object._

---

> _If we reference an object with a version, the consistency issue with some object storage systems disappears: the key and version metadata together form a unique reference to a particular, immutable data object._

---

> _an object reader sees a strongly consistent object store at the cost of higher latency for object access._

---

> _to impose strong consistency on an object store for various reasons, and standard methods are used to achieve this. One approach is to add a strongly consistent database (e.g., PostgreSQL) to the mix._

---

> _Object stores may be eventually consistent or strongly consistent. For example, until recently, S3 was eventually consistent; after a new version of an object was written under the same key, the object store might sometimes return the old version of the object. The eventual part of eventual consistency means that after enough time has passed, the storage cluster reaches a state such that only the latest version of the object will be returned. This contrasts with the strong consistency model we expect of local disks attached to a server: reading after a write will return the most recently written data_

---

> _This might seem like a minor technical detail, but engineers need to understand that certain “directory”-level operations are costly in an object store. To run aws ls S3://oreilly-data-engineering-book/project-data/11/ the object store must filter keys on the key prefix project-data/11/. If the bucket contains millions of objects, this operation might take some time, even if the “subdirectory” houses only a few objects._

---

> _Although cloud object stores may appear to support directory tree semantics, no true directory hierarchy exists_

---

> _object stores are key-value stores. What does this mean for engineers? It’s critical to understand that, unlike file stores, object stores do not utilize a directory tree to find objects._

---

> _In the early days of data lakes, write once, read many (WORM) was the operational standard, but this had more to do with the complexities of managing data versions and files than the limitations of HDFS and object stores. Since then, systems such as Apache Hudi and Delta Lake have emerged to manage this complexity, and privacy regulations such as GDPR and CCPA have made deletion and update capabilities imperative. Update management for object storage is the central idea behind the data lakehouse concept_

---

> _Object storage was arguably one of the first “serverless” services; engineers don’t need to consider the characteristics of underlying server clusters or disks._

---

> _data engineering folklore says that object stores are not good for updates, but this is only partially true. Object stores are an inferior fit for transactional workloads with many small updates every second; these use cases are much better served by transactional databases or block storage systems. Object stores work well for a low rate of update operations, where each operation updates a large volume of data._

---

> _Blocks on magnetic disks are geometrically arranged on a physical platter. Two blocks on the same track can be read without moving the head, while reading two blocks on separate tracks requires a seek. Seek time can occur between blocks on an SSD, but this is infinitesimal compared to the seek time for magnetic disk tracks._

---

> _block storage is the type of raw storage provided by SSDs and magnetic disks. In the cloud, virtualized block storage is the standard for VMs._

---

> _Dynamic RAM stores data as charges in capacitors. These capacitors leak over time, so the data must be frequently refreshed (read and rewritten) to prevent data loss._

---

> _Cloud filesystems should not be confused with standard storage attached to VMs—generally, block storage with a filesystem managed by the VM operating system. Cloud filesystems behave much like NAS solutions, but the details of networking, managing disk clusters, failures, and configuration are fully handled by the cloud vendor._

---

> _Network-attached storage (NAS) systems provide a file storage system to clients over a network._

---

> _Local filesystems generally support full read after write consistency; reading immediately after a write will return the written data. Operating systems also employ various locking strategies to manage concurrent writing attempts to a file._

---

> _File storage systems organize files into a directory tree_

---

> _The filesystem stores each directory as metadata about the files and directories that it contains. This metadata consists of the name of each entity, relevant permission details, and a pointer to the actual entity. To find a file on disk, the operating system looks at the metadata at each hierarchy level and follows the pointer to the next subdirectory entity until finally reaching the file itself._

---

> _Eventual consistency is a common trade-off in large-scale, distributed systems. If you want to scale horizontally (across multiple nodes) to process data in high volumes, then eventually, consistency is often the price you’ll pay. Eventual consistency allows you to retrieve data quickly without verifying that you have the latest version across all nodes._
>
> _The opposite of eventual consistency is strong consistency. With strong consistency, the distributed database ensures that writes to any node are first distributed with a consensus and that any reads against the database return consistent values. You’ll use strong consistency when you can tolerate higher query latency and require correct data every time you read from the database._

---

> _distributed systems pose a dilemma for storage and query accuracy. It takes time to replicate changes across the nodes of a system; often a balance exists between getting current data and getting “sorta” current data in a distributed database_

---

> _BASE, which stands for basically available, soft-state, eventual consistency. Think of it as the opposite of ACID. BASE is the basis of eventual consistency_

---

> _The core idea of caching is to store frequently or recently accessed data in a fast access layer. The faster the cache, the higher the cost and the less storage space available. Less frequently accessed data is stored in cheaper, slower storage_

---

> _10 gigabits per second (Gbps) of bandwidth, a 10:1 compression ratio increases effective network bandwidth to 100 Gbps._

---

> _Highly efficient compression has three main advantages in storage systems. First, the data is smaller and thus takes up less space on the disk. Second, compression increases the practical scan speed per disk. With a 10:1 compression ratio, we go from scanning 200 MB/s per magnetic disk to an effective rate of 2 GB/s per disk._
>
> _The third advantage is in network performance. Given_

---

> _Data stored in system memory by software is generally not in a format suitable for storage on disk or transmission over a network. Serialization is the process of flattening and packing data into a standard format that a reader will be able to decode. Serialization formats provide a standard of data exchange. We might encode data in a row-based manner as an XML, JSON, or CSV file and pass it to another user who can then decode it using a standard library_

---

> _balance the durability and availability achieved by spreading out data geographically versus the performance and cost benefits of keeping storage in a small geographic area and close to data consumers or writers_

---

> _CPUs handle the details of servicing requests, aggregating reads, and distributing writes. Storage becomes a web application with an API, backend service components, and load balancing. Network device performance and network topology are key factors in realizing high performance._

---

> _Availability zones are a standard cloud construct consisting of compute environments with independent power, water, and other resources._

---

> _redundant arrays of independent disks (RAID) parallelize on a single server, cloud object storage clusters operate at a much larger scale, with disks distributed across a network and even multiple data centers and availability zones._

---

> _SSDs are not currently the default option for high-scale analytics data storage. Again, this comes down to cost. Commercial SSDs typically cost 20–30 cents (USD) per gigabyte of capacity, nearly 10 times the cost per capacity of a magnetic drive._

---

> _Solid-state drives (SSDs) store data as charges in flash memory cells._

---

> _magnetic disks are still prized in data centers for their low data-storage costs. In addition, magnetic drives can sustain extraordinarily high transfer rates through parallelism. This is the critical idea behind cloud object storage: data can be distributed across thousands of disks in clusters. Data-transfer rates go up dramatically by reading from numerous disks simultaneously, limited primarily by network performance rather than disk transfer rate_

---

> _SSDs can deliver data with significantly lower latency, higher IOPS, and higher transfer speeds, partially because there is no physically rotating disk or magnetic head to wait for_

---

> _A fourth limitation is input/output operations per second (IOPS), critical for transactional databases_

---

> _A second major limitation is seek time. To access data, the drive must physically relocate the read/write heads to the appropriate track on the disk. Third, in order to find a particular piece of data on the disk, the disk controller must wait for that data to rotate under the read/write heads. This leads to rotational latency._

---

> _First, disk transfer speed, the rate at which data can be read and written, does not scale in proportion with disk capacity._

---

> _Magnetic disks utilize spinning platters coated with a ferromagnetic film (Figure 6-3). This film is magnetized by a read/write head during write operations to physically encode binary data. The read/write head detects the magnetic field and outputs a bitstream during read operations_

### 7. Ingestion

> _orchestration, we mean a system capable of scheduling complete task graphs rather than individual tasks._

---

> _many data-quality issues can be handled by respecting basic best practices in software engineering, such as logs to capture the history of data changes, checks (nulls, etc.), and exception handling (try, catch, etc.)._

---

> _DevOps engineers are typically able to detect problems by using binary conditions. Has the request failure rate breached a certain threshold? How about response latency? In the data space, regressions often manifest as subtle statistical distortions_

---

> _One of the inherent differences between DevOps and DataOps is that we expect software regressions only when we deploy changes, while data often presents regressions independently because of events outside our control._

---

> _using bad data to make decisions is much worse than having no data._

---

> _one stage in the data engineering lifecycle where monitoring is critical, it’s in the ingestion stage_

---

> _Generally, we don’t see encryption problems but data access problems_

---

> _put a broken-glass process in place: require at least two people to approve access to sensitive data in the production environment. This access should be tightly scoped to a particular issue and come with an expiration date_

---

> _Touchless production is an ideal that engineers should strive for, but situations inevitably arise that cannot be fully solved in development and staging environments._

---

> _Where it is truly necessary to keep track of sensitive identities, it is common practice to apply tokenization to anonymize identities in model training and analytics. But engineers should look at where this tokenization is used. If possible, hash data at ingestion time._

---

> _They will inevitably encounter sensitive data; the natural tendency is to ingest it and forward it to the next step in the pipeline. But if this data is not needed, why collect it at all? Why not simply drop sensitive fields before data is stored? Data cannot leak if it is never collected._

---

> _Clients often ask for our advice on encrypting sensitive data in databases, which generally leads us to ask a fundamental question: do you need the sensitive data you’re trying to encrypt?_

---

> _One may quite easily maintain multiple versions of a table with different schemas and even different upstream transformations. Teams can support various “development” versions of a table by using orchestration tools such as Airflow; schema changes, upstream transformation, and code changes can appear in development tables before official changes to the main table._

---

> _One possible solution, which we, the authors, have meditated on for a while, is an approach pioneered by Git version control._

---

> _Schema changes (such as adding, changing, or removing columns in a database table) remain, from our perspective, an unsettled issue in data management. The traditional approach is a careful command-and-control review process. Working with clients at large enterprises, we have been quoted lead times of six months for the addition of a single field. This is an unacceptable impediment to agility._

---

> _Moving data introduces security vulnerabilities because you have to transfer data between locations._

---

> _Moving data introduces security vulnerabilities because you have to transfer data between locations._

---

> _View data engineering as a business, and recognize who your customers are. Often basic automation of ingestion processes has significant value, especially for departments like marketing that control massive budgets and sit at the heart of revenue for the business. Basic ingestion work may seem tedious, but delivering value to these core parts of the company will open up more budget and more exciting long-term data engineering opportunities._

---

> _A significant disconnect often exists between those responsible for generating data—typically, software engineers—and the data engineers who will prepare this data for analytics and data science. Software engineers and data engineers usually sit in separate organizational silos;_

---

> _Data sharing is growing as a popular option for consuming data (see Chapters 5 and 6). Data providers will offer datasets to third-party subscribers, either for free or at a cost. These datasets are often shared in a read-only fashion, meaning you can integrate these datasets with your own data (and other third-party datasets), but you do not own the shared dataset._

---

> _For massive quantities of data (100 TB or more), transferring data directly over the internet may be a slow and costly process. At this scale, the fastest, most efficient way to move data is not over the wire but by truck_

---

> _web pages constantly change their HTML element structure, making it tricky to keep your web scraper updated. Ask yourself, is the headache of maintaining these systems worth the effort?_

---

> _ask yourself if you should be web scraping or if data is available from a third party. If your decision is to web scrape, be a good citizen. Don’t inadvertently create a denial-of-service (DoS) attack, and don’t get your IP address blocked._

---

> _Web scraping is widespread, and you may encounter it as a data engineer. It’s also a murky area where ethical and legal lines are blurry._

---

> _Webhook-based data ingestion architectures can be brittle, difficult to maintain, and inefficient._

---

> _With a webhook (Figure 7-15), the data provider defines an API request specification, but the data provider makes API calls rather than receiving them; it’s the data consumer’s responsibility to provide an API endpoint for the provider to call. The consumer is responsible for ingesting each request and handling data aggregation, storage, and processing._

---

> _Accessing and sending data both from secure FTP (SFTP) and secure copy (SCP) are techniques you should be familiar with, even if data engineers do not typically use these regularly (IT or security/secOps will handle this)._
>
> _Engineers rightfully cringe at the mention of SFTP (occasionally, we even hear instances of FTP being used in production). Regardless, SFTP is still a practical reality for many businesses. They work with partner businesses that consume or provide data using SFTP and are unwilling to rely on other standards. To avoid data leaks, security analysis is critical in these situations._
>
> _SCP is a file-exchange protocol that runs over an SSH connection. SCP can be a secure file-transfer option if it is configured correctly_

---

> _Application databases should never be directly exposed on the internet. Instead, engineers can set up a bastion host—i.e., an intermediate host instance that can connect to the database in question. This host machine is exposed on the internet, although locked down for minimal access from only specified IP addresses to specified ports. To connect to the database, a remote machine first opens an SSH tunnel connection to the bastion host and then connects from the host machine to the database_

---

> _The disadvantage of these newer formats is that many of them are not natively supported by source systems. Data engineers are often forced to work with CSV data and then build robust exception handling and error detection to ensure data quality on ingestion_

---

> _columnar formats (Parquet, Arrow, ORC) allow more efficient data export because columns can be directly transcoded between formats. These formats are also generally more optimized for query engines. The Arrow file format is designed to map data directly into processing engine memory, providing high performance in data lake environments._

---

> _More robust and expressive export formats include Parquet, Avro, Arrow, and ORC or JSON._

---

> _CSV is still ubiquitous and highly error prone at the time of this writing. Namely, CSV’s default delimiter is also one of the most familiar characters in the English language—the comma! But it gets worse._
>
> _CSV is by no means a uniform format. Engineers must stipulate the delimiter, quote characters, and escaping to appropriately handle the export of string data. CSV also doesn’t natively encode schema information or directly support nested structures. CSV file encoding and schema information must be configured in the target system to ensure appropriate ingestion._

---

> _object storage is the most optimal and secure way to handle file exchange_

---

> _suggest using managed connector platforms instead of creating and managing your connectors._

---

> _object storage is the most optimal and secure way to handle file exchange._

---

> _an essential difference between batch and streaming ingestion. Whereas batch usually involves static workflows (ingest data, store it, transform it, and serve it), messages and streams are fluid. Ingestion can be nonlinear, with data being published, consumed, republished, and reconsumed._

---

> _Don’t reinvent the wheel when data sharing is not an option and direct API access is necessary. While a managed service might look like an expensive option, consider the value of your time and the opportunity cost of building API connectors when you could be spending your time on higher-value work._

---

> _many vendors provide API client libraries for various programming languages that remove much of the complexity of API access._

---

> _no proper standard exists for data exchange over APIs._

---

> _The advantage of synchronous replication is that the secondary database can offload work from the primary database by acting as a read replica; read queries can be redirected to the replica. The query will return the same results that would be returned from the primary database._

---

> _CDC can be used to replicate between databases: events are buffered into a stream and asynchronously written into a second database._

---

> _Continuous CDC captures all table history and can support near real-time data ingestion, either for real-time database replication or to feed real-time streaming analytics. Rather than running periodic queries to get a batch of table changes, continuous CDC treats each write to the database as an event._

---

> _This issue can be mitigated by utilizing an insert-only schema, where each account transaction is recorded as a new record in the table_

---

> _This issue can be mitigated by utilizing an insert-only schema, where each account transaction is recorded as a new record in the table_

---

> _If the database table in question has an updated_at field containing the last time a record was written or updated, we can query the table to find all updated rows since a specified time. We set the filter timestamp based on when we last captured changed rows from the tables. This process allows us to pull changes and differentially update a target table._
>
> _This form of batch-oriented CDC has a key limitation: while we can easily determine which rows have changed since a point in time, we don’t necessarily obtain all changes that were applied to these rows._

---

> _JDBC and ODBC were long the gold standards for data ingestion from databases, but these connection standards are beginning to show their age for many data engineering applications. These connection standards struggle with nested data, and they send data as rows. This means that native nested data must be reencoded as string data to be sent over the wire, and columns from columnar databases must be reserialized as rows._

---

> _JDBC is conceptually remarkably similar to ODBC. A Java driver connects to a remote database and serves as a translation layer between the standard JDBC API and the native network interface of the target database. It might seem strange to have a database API dedicated to a single programming language, but there are strong motivations for this. The Java Virtual Machine (JVM) is standard, portable across hardware architectures and operating systems, and provides the performance of compiled code through a just-in-time (JIT) compiler. The JVM is an extremely popular compiling VM for running code in a portable manner._

---

> _JDBC provides extraordinary database driver portability. ODBC drivers are shipped as OS and architecture native binaries; database vendors must maintain versions for each architecture/OS version that they wish to support. On the other hand, vendors can ship a single JDBC driver that is compatible with any JVM language (e.g., Java, Scala, Clojure, or Kotlin) and JVM data framework (i.e., Spark.) JDBC has become so popular that it is also used as an interface for non-JVM languages such as Python; the Python ecosystem provides translation tools that allow Python code to talk to a JDBC driver running on a local JVM._

---

> _JDBC is conceptually remarkably similar to ODBC. A Java driver connects to a remote database and serves as a translation layer between the standard JDBC API and the native network interface of the target database. It might seem strange to have a database API dedicated to a single programming language, but there are strong motivations for this. The Java Virtual Machine (JVM) is standard, portable across hardware architectures and operating systems, and provides the performance of compiled code through a just-in-time (JIT) compiler. The JVM is an extremely popular compiling VM for running code in a portable manner._

---

> _ODBC uses a driver hosted by a client accessing the database to translate commands issued to the standard ODBC API into commands issued to the database. The database returns query results over the wire, where the driver receives them and translates them back into a standard form to be read by the client._

---

> _Data can be pulled from databases for ingestion by querying and reading over a network connection. Most commonly, this connection is made using ODBC or JDBC._

---

> _use a dead-letter queue to diagnose why event ingestions errors occur and solve data pipeline problems, and might be able to reprocess some messages in the queue after fixing the underlying cause of errors_

---

> _Events that cannot be ingested need to be rerouted and stored in a separate location called a dead-letter queue_

---

> _a dead-letter queue (described in “Error Handling and Dead-Letter Queues”) can help you investigate issues with events that are not properly handled._

---

> _For example, an IoT device gets a firmware update that adds a new field to the event it transmits, or a third-party API introduces changes to its event payload or countless other scenarios. All of these potentially impact your downstream capabilities._

---

> _Schema evolution is common when handling event data;_

---

> _many tools are available to automate various types of data migrations. Especially for large and complex migrations, we suggest looking at these options before doing this manually or writing your own migration solution._

---

> _while it is common to insert one row at a time in a transactional database, this is a bad pattern for many columnar databases, as it forces the creation of many small, suboptimal files and forces the system to run a high number of create object operations._

---

> _Batch-oriented systems often perform poorly when users attempt to perform many small-batch operations rather than a smaller number of large operations_

---

> _Data is quite often moved between databases and systems using files. Data is serialized into files in an exchangeable format, and these files are provided to an ingestion system. We consider file-based export to be a push-based ingestion pattern. This is because data export and preparation work is done on the source system side._
>
> _File-based ingestion has several potential advantages over a direct database connection approach. It is often undesirable to allow direct access to backend systems for security reasons. With file-based ingestion, export processes are run on the data-source side, giving source system engineers complete control over what data gets exported and how the data is preprocessed. Once files are done, they can be provided to the target system in various ways. Common file-exchange methods are object storage, secure file transfer protocol (SFTP), electronic data interchange (EDI), or secure copy (SCP)._

---

> _Changes in schema frequently occur in source systems and are often well out of data engineers’ control._

---

> _implement strategies to respond to changes automatically and alert on changes that cannot be accommodated automatically._

---

> _Even if automation can accommodate a change, the new schema may adversely affect the performance of reports and models. Communication between those making schema changes and those impacted by these changes is as important as reliable automation that checks for schema changes._

---

> _In streaming data, every message has a schema, and these schemas may evolve between producers and consumers. A schema registry is a metadata repository used to maintain schema and data type integrity in the face of constantly changing schemas. Schema registries can also track schema versions and history._

---

> _Metadata is data about data. Metadata can be as critical as the data itself. One of the significant limitations of the early approach to the data lake—or data swamp, which could become a data superfund site—was a complete lack of attention to metadata_

---

> _Data engineers must choose whether to capture full snapshots of a source system or differential (sometimes called incremental) updates. With full snapshots, engineers grab the entire current state of the source system on each update read. With the differential update pattern, engineers can pull only the updates and changes since the last read from the source system. While differential updates are ideal for minimizing network traffic and target storage usage, full snapshot reads remain extremely common because of their simplicity._

---

> _Time-interval batch ingestion is widespread in traditional business ETL for data warehousing. This pattern is often used to process data once a day, overnight during off-hours, to provide daily reporting, but other frequencies can also be used._
>
> _Size-based batch ingestion (Figure 7-11) is quite common when data is moved from a streaming-based system into object storage; ultimately, you must cut the data into discrete blocks for future processing in a data lake. Some size-based ingestion systems can break data into objects based on various criteria, such as the size in bytes of the total number of events._

---

> _Batch ingestion, which involves processing data in bulk, is often a convenient way to ingest data. This means that data is ingested by taking a subset of data from a source system, based either on a time interval or the size of accumulated data_

---

> _Schema is not only for databases. As we’ve discussed, APIs present their schema complications._

---

> _The great engineering challenge is understanding the underlying schema. Applications organize data in various ways, and engineers need to be intimately familiar with the organization of the data and relevant update patterns to make sense of it. The problem has been somewhat exacerbated by the popularity of object-relational mapping (ORM), which automatically generates schemas based on object structure in languages such as Java or Python. Natural structures in an object-oriented language often map to something messy in an operational database. Data engineers may need to familiarize themselves with the class structure of application code._

---

> _The size of the data describes the number of bytes of a payload_

---

> _shape that describes its dimensions._

---

> _ML models are typically trained on a batch basis, although continuous online training is becoming more prevalent._

---

> _Once data reaches a batch process, the batch frequency becomes a bottleneck for all downstream processing._

---

> _In IoT applications, the typical pattern is for each sensor to write events or measurements to streaming systems as they happen._

---

> _In theory, your ingestion should never be a bottleneck. In practice, ingestion bottlenecks are pretty standard._

---

> _Data generation rarely happens at a constant rate and often ebbs and flows. Built-in buffering is required to collect events during rate spikes to prevent data from getting lost. Buffering bridges the time while the system scales and allows storage systems to accommodate bursts even in a dynamically scalable system._
>
> _Whenever possible, use managed services that handle the throughput scaling for you_

---

> _Data throughput and system scalability become critical as your data volumes grow and requirements change. Design your systems to scale and shrink to flexibly match the desired data throughput._

---

> _Reliability and durability are vital in the ingestion stages of data pipelines. Reliability entails high uptime and proper failover for ingestion systems. Durability entails making sure that data isn’t lost or corrupted._

---

> _Some data sources (e.g., IoT devices and caches) may not retain data if it is not correctly ingested. Once lost, it is gone for good. In this sense, the reliability of ingestion systems leads directly to the durability of generated data. If data is ingested, downstream processes can theoretically run late if they break temporarily._

---

> _Kind consists of type and format. Data has a type—tabular, image, video, text, etc. The type directly influences the data format or the way it is expressed in bytes, names, and file extensions. For example, a tabular kind of data may be in formats such as CSV or Parquet, with each of these formats having different byte patterns for serialization and deserialization. Another kind of data is an image, which has a format of JPG or PNG and is inherently unstructured_

---

> _A payload is the dataset you’re ingesting and has characteristics such as kind, shape, size, schema and data types, and metadata._

---

> _asynchronous ingestion, dependencies can now operate at the level of individual events, much as they would in a software backend built from microservices_

---

> _synchronous workflow is common in older ETL systems, where data extracted from a source system must then be transformed before being loaded into a data warehouse. Processes downstream of ingestion can’t start until all data in the batch has been ingested. If the ingestion or transformation process fails, the entire process must be rerun_

---

> _Even with a streaming data-ingestion process, batch processing downstream is relatively standard._

---

> _The near real-time pattern generally does away with an explicit update frequency; events are processed in the pipeline either one by one as they arrive or in micro-batches (i.e., batches over concise time intervals)._

---

> _because no ingestion system is genuinely real-time. Any database, queue or pipeline has inherent latency in delivering data to a target system. It is more accurate to speak of near real-time_

---

> _Ingestion processes can be batch, micro-batch, or real-time_

---

> _streaming ingestion systems are simply a tool for preserving the unbounded nature of data so that subsequent steps in the lifecycle can also process it continuously_

---

> _All data is unbounded until it’s bounded_

---

> _Whereas data ingestion is data movement from point A to B, data integration combines data from disparate sources into a new dataset._

### 8. Queries, Modeling, and Transformation

> _With queries and transformations, DataOps has two areas of concern: data and systems. You need to monitor and be alerted for changes or anomalies in these areas. The field of data observability is exploding right now, with a big focus on data reliability. There’s even a recent job title called data reliability engineer. This section emphasizes data observability and data health, which focuses on the query and transformation stage._

---

> _If there’s a data-quality issue in the transformation, you should have the ability to flag this issue, roll back the changes, and investigate the root cause._

---

> _what impact does regulatory compliance have on your data model and transformations? Are sensitive fields data masked or obfuscated if necessary? Do you have the ability to delete data in response to deletion requests? Does your data lineage tracking allow you to see data derived from deleted data and rerun transformations to remove data downstream of raw sources?_

---

> _As we transform data, data lineage tools become invaluable._

---

> _As we transform data, data lineage tools become invaluable._

---

> _the notion of a semantic or metrics layer that sits independent of transformations is becoming popular. Instead of enforcing business logic within the transformation at runtime, why not keep these definitions as a standalone stage before your transformation layer?_

---

> _a view is just a query that references other tables_

---

> _views can serve a security role. For example, views can select only specific columns and filter rows, thus providing restricted data access. Various views can be created for job roles depending on user data access._

---

> _a view might be used to provide a current deduplicated picture of data._

---

> _views can be used to present common data access patterns_

---

> _A materialized view does some or all of the view computation in advance_

---

> _Federated queries are a database feature that allows an OLAP database to select from an external data source, such as object storage or RDBMS._

---

> _Data virtualization is closely related to federated queries, but this typically entails a data processing and query system that doesn’t store data internally_

---

> _The most significant considerations with data virtualization are supported external sources and performance_

---

> _Query pushdown aims to move as much work as possible to the source databases._

---

> _Data virtualization can be viewed as a tool that expands the data lake to many more sources by abstracting away barriers used to silo data between organizational units._

---

> _This fits closely with the notion of a data mesh (discussed in Chapter 3), wherein small teams are responsible for preparing their data for analytics and sharing it with the rest of the company; virtualization can serve as a critical access layer for practical sharing._

---

> _Data virtualization is a good solution for organizations with data stored across various data sources._

---

> _Micro-batching is a way to take a batch-oriented framework and apply it in a streaming situation. A micro-batch might run anywhere from every two minutes to every second._

---

> _A long-running battle has been ongoing between micro-batch and true streaming approaches. Fundamentally, it’s important to understand your use case, the performance requirements, and the performance capabilities of the framework in question._

---

> _When it comes to transformations, upstream stakeholders can be broken into two broad categories: those who control the business definitions and those who control the systems generating data._

---

> _Transformations are where data starts providing utility to downstream stakeholders. Your downstream stakeholders include many people, including data analysts, data scientists, ML engineers, and “the business.”_

---

> _One interesting alternative is to push business logic into a metrics layer,17 but still leverage the data warehouse or other tool to do the computational heavy lifting. A metrics layer encodes business logic and allows analysts and dashboard users to build complex analytics from a library of defined metrics. The metrics layer generates queries from the metrics and sends these to the database_

---

> _derived data—data computed from other data stored in a data system. Derived data critics will point out that it is challenging for the ETL to maintain consistency in the derived metrics.16 For example, if the company updates its attribution model, this change may need to be merged into many ETL scripts for reporting. (ETL scripts are notorious for breaking the DRY principle.) Updating these ETL scripts is a manual and labor-intensive process, involving domain expertise in processing logic and previous changes. Updated scripts must also be validated for consistency and accuracy._

---

> _One of the most common use cases for transformation is to render business logic._

---

> _Data wrangling takes messy, malformed data and turns it into useful, clean data. This is generally a batch transformation process._

---

> _SELECT * rather than using explicit column selection? This is generally bad practice in columnar databases.)_

---

> _One advantage of columnar systems over row-based systems is that while updating the data is more difficult, updating the schema is easier. Columns can typically be added, deleted, and renamed._

---

> _the original data lake concept didn’t really account for updating data. This now seems nonsensical for several reasons. Updating data has long been a key part of handling data transformation results, even though the big data community dismissed it. It is silly to rerun significant amounts of work because we have no update capabilities. Thus, the data lakehouse concept now builds in updates. Also, GDPR and other data deletion standards now require organizations to delete data in a targeted fashion, even in raw datasets._

---

> _Insert-only patterns can be used to maintain a current view of data—for example, if new versions of records are inserted without deleting old records. A query or view can present the current data state by finding the newest record by primary key. Note that columnar databases don’t typically enforce primary keys. The primary key would be a construct used by engineers to maintain a notion of the current state of the table. The downside to this approach is that it can be extremely computationally expensive to find the latest record at query time. Alternatively, we can use a materialized view (covered later in the chapter), an insert-only table that maintains all records, and a truncate-and-reload target table that holds the current state for serving data._

---

> _Upsert/merge_

---

> _A hard delete permanently removes a record from a database, while a soft delete marks the record as “deleted.” Hard deletes are useful when you need to remove data for performance reasons (say, a table is too big), or if there’s a legal or compliance reason to do so. Soft deletes might be used when you don’t want to delete a record permanently but also want to filter it out of query results._
>
> _A third approach to deletes is closely related to soft deletes: insert deletion inserts a new record with a deleted flag without modifying the previous version of the record. This allows us to follow an insert-only pattern but still account for deletions. Just note that our query to get the latest table state gets a little more complicated. We must now deduplicate, find the latest version of each record by key, and not show any record whose latest version shows deleted._

---

> _When embracing Spark, data engineering teams need to actively engage with the problems of Spark optimization, especially for expensive, long-running jobs. This means building optimization expertise on the team and teaching individual engineers how to optimize._

---

> _it is possible to recycle SQL in two ways. First, we can easily reuse the results of a SQL query by committing to a table or creating a view. This process is often best handled in an orchestration tool such as Airflow so that downstream queries can start once the source query has finished. Second, Data Build Tool (dbt) facilitates the reuse of SQL statements and offers a templating language that makes customization easier._

---

> _one of the major limitations of SQL is that it doesn’t include a natural notion of libraries or reusable code._

---

> _When you’re determining whether to use native Spark or PySpark code instead of Spark SQL or another SQL engine, ask yourself the following questions:_
>
> _How difficult is it to code the transformation in SQL?_
>
> _How readable and maintainable will the resulting SQL code be?_
>
> _Should some of the transformation code be pushed into a custom library for future reuse across the organization?_

---

> _SQL dismissed because it is “not procedural.” This is technically correct. SQL is a declarative language: instead of coding a data processing procedure, SQL writers stipulate the characteristics of their final data in set-theoretic language; the SQL compiler and optimizer determine the steps required to put data in this state._
>
> _People sometimes imply that because SQL is not procedural, it cannot build out complex pipelines. This is false. SQL can effectively be used to build complex DAGs using common table expressions, SQL scripts, or an orchestration tool._
>
> _To be clear, SQL has limits, but we often see engineers doing things in Python and Spark that could be more easily and efficiently done in SQL._

---

> _A now-popular evolution of ETL is ELT. As data warehouse systems have grown in performance and storage capacity, it has become common to simply extract raw data from a source system, import it into a data warehouse with minimal transformation, and then clean and transform it directly in the warehouse system. (See our discussion of data warehouses in Chapter 3 for a more detailed discussion of the difference between ETL and ELT.)_
>
> _A second, slightly different notion of ELT was popularized with the emergence of data lakes. In this version, the data is not transformed at the time it’s loaded. Indeed, massive quantities of data may be loaded with no preparation and no plan whatsoever. The assumption is that the transformation step will happen at some undetermined future time. Ingesting data without a plan is a great recipe for a data swamp._

---

> _A transformation differs from a query. A query retrieves the data from various sources based on filtering and join logic. A transformation persists the results for consumption by additional transformations or queries. These results may be stored ephemerally or permanently._

---

> _A transformation differs from a query. A query retrieves the data from various sources based on filtering and join logic. A transformation persists the results for consumption by additional transformations or queries. These results may be stored ephemerally or permanently._

---

> _Transformations critically rely on one of the major undercurrents in this book: orchestration. Orchestration combines many discrete operations, such as intermediate transformations, that store data temporarily or permanently for consumption by downstream transformations or serving. Increasingly, transformation pipelines span not only multiple tables and datasets but also multiple systems._

---

> _a second aspect that differentiates transformations from queries is complexity._

---

> _anticipate changes in the source data and keep a flexible schema. This means there’s no rigid data model in the analytical database. Instead, assume the source systems are providing the correct data with the right business definition and logic, as it exists today. And because storage is cheap, store the recent streaming and saved historical data in a way they can be queried together. Optimize for comprehensive analytics against a dataset with a flexible schema_

---

> _the shape of the data in these streams is semistructured, such as JSON. The challenge with modeling streaming data is that the payload’s schema might change_

---

> _the Data Vault as an option for streaming data modeling_

---

> _There isn’t (yet) a consensus approach on streaming data modeling._

---

> _The world is evolving from batch to streaming and from on premises to the cloud._

---

> _Wide denormalized tables_

---

> _in a Data Vault, the business logic is created and interpreted when the data from these tables is queried. Please be aware that the Data Vault model can be used with other data modeling techniques. It’s not unusual for a Data Vault to be the landing zone for analytical data, after which it’s separately modeled in a data warehouse, commonly using a star schema. The Data Vault model also can be adapted for NoSQL and streaming data sources._

---

> _A slowly changing dimension (SCD) is necessary to track changes in dimensions. The preceding example is a Type 2 SCD: a new record is inserted when an existing record changes._

---

> _Type 1_
> _Overwrite existing dimension records. This is super simple and means you have no access to the deleted historical dimension records._
>
> _Type 2_
> _Keep a full history of dimension records. When a record changes, that specific record is flagged as changed, and a new dimension record is created that reflects the current status of the attributes_

---

> _a Data Vault simply loads data from source systems directly into a handful of purpose-built tables in an insert-only manner. Unlike the other data modeling approaches you’ve learned about, there’s no notion of good, bad, or conformed data in a Data Vault._

---

> _The goal of this methodology is to keep the data as closely aligned to the business as possible, even while the business’s data evolves._

---

> _Satellites are descriptive attributes that give meaning and context to hubs. Satellites can connect to either hubs or links. The only required fields in a satellite are a primary key consisting of the business key of the parent hub and a load date._

---

> _A link table tracks the relationships of business keys between hubs. Link tables connect hubs, ideally at the lowest possible grain. Because link tables connect data from various hubs, they are many to many. The Data Vault model’s relationships are straightforward and handled through changes to the links. This provides excellent flexibility in the inevitable event that the underlying data changes. You simply create a new link that ties business concepts (or hubs) to represent the new relationship. That’s it!_

---

> _how do users commonly look for data?_

---

> _Hash key_
> _The primary key used to join data between systems. This is a calculated hash field (MD5 or similar)._
>
> _Load date_
> _The date the data was loaded into the hub._
>
> _Record source_
> _The source from which the unique record was obtained._
>
> _Business key(s)_
> _The key used to identify a unique record._
>
> _It’s important to note that a hub is insert-only, and data is not altered in a hub. Once data is loaded into a hub, it’s permanent._

---

> _A hub is the central entity of a Data Vault that retains a record of all unique business keys loaded into the Data Vault._

---

> _A Data Vault model consists of three main types of tables: hubs, links, and satellites (Figure 8-15). In short, a hub stores business keys, a link maintains relationships among business keys, and a satellite represents a business key’s attributes and context. A user will query a hub, which will link to a satellite table containing the query’s relevant attributes._

---

> _Because a star schema has one fact table, sometimes you’ll have multiple star schemas that address different facts of the business. You should strive to reduce the number of dimensions whenever possible since this reference data can potentially be reused among different fact tables. A dimension that is reused across multiple star schemas, thus sharing the same fields, is called a conformed dimension._

---

> _The star schema represents the data model of the business. Unlike highly normalized approaches to data modeling, the star schema is a fact table surrounded by the necessary dimensions. This results in fewer joins than other data models, which speeds up query performance. Another advantage of a star schema is it’s arguably easier for business users to understand and use._

---

> _Type 1 is the default behavior of most data warehouses, and Type 2 is the one we most commonly see used in practice._

---

> _In a Kimball data model, dates are typically stored in a date dimension, allowing you to reference the date key (DateKey) between the fact and date dimension table._

---

> _Dimension tables provide the reference data, attributes, and relational context for the events stored in fact tables. Dimension tables are smaller than fact tables and take an opposite shape, typically wide and short. When joined to a fact table, dimensions can describe the events’ what, where, and when. Dimensions are denormalized, with the possibility of duplicate data. This is OK in the Kimball data model._

---

> _Instead, the fact table has keys that reference dimension tables containing their respective attributes, such as the customer and date information_

---

> _data types in the fact table are all numbers (integers and floats); there are no strings._

---

> _Avoid aggregating or deriving data within a fact table. If you need to perform aggregations or derivations, do so in a downstream query, data mart table, or view. Finally, fact tables don’t reference other fact tables; they reference only dimensions._

---

> _the fact table, which contains factual, quantitative, and event-related data. The data in a fact table is immutable because facts relate to events. Therefore, fact tables don’t change and are append-only. Fact tables are typically narrow and long, meaning they have not a lot of columns but a lot of rows that represent events. Fact tables should be at the lowest grain possible._

---

> _In Kimball’s approach, data is modeled with two general types of tables: facts and dimensions. You can think of a fact table as a table of numbers, and dimension tables as qualitative data referencing a fact. Dimension tables surround a single fact table in a relationship called a star schema_

---

> _Whereas Inmon integrates data from across the business in the data warehouse, and serves department-specific analytics via data marts, the Kimball model is bottom-up, encouraging you to model and serve department or business analytics in the data warehouse itself (Inmon argues this approach skews the definition of a data warehouse). The Kimball approach effectively makes the data mart the data warehouse itself. This may enable faster iteration and modeling than Inmon, with the trade-off of potential looser data integration, data redundancy, and duplication._

---

> _three main data models are conceptual, logical, and physical._

---

> _When creating a conceptual model, it’s often helpful to visualize it in an entity-relationship (ER) diagram, which is a standard tool for visualizing the relationships among various entities in your data_

---

> _Data from key business source systems is ingested and integrated into a highly normalized (3NF) data warehouse that often closely resembles the normalization structure of the source system itself; data is brought in incrementally, starting with the highest-priority business areas. The strict normalization requirement ensures as little data duplication as possible, which leads to fewer downstream analytical errors because data won’t diverge or suffer from redundancies._

---

> _The Inmon data warehouse must strictly adhere to all four of these critical parts in support of management’s decisions. This is a subtle point, but it positions the data warehouse for analytics, not OLTP._

---

> _A data warehouse is a subject-oriented, integrated, nonvolatile, and time-variant collection of data in support of management’s decisions. The data warehouse contains granular corporate data. Data in the data warehouse is able to be used for many different purposes, including sitting and waiting for future requirements which are unknown today._

---

> _The goal of the data warehouse was to separate the source system from the analytical system_

---

> _data modeling for data lakes or data warehouses, you should assume that the raw data takes many forms (e.g., structured and semistructured), but the output is a structured data model of rows and columns._

---

> _data modeling for data lakes or data warehouses, you should assume that the raw data takes many forms (e.g., structured and semistructured), but the output is a structured data model of rows and columns._

---

> _some denormalization presents performance advantages. Although denormalization may seem like an antipattern, it’s common in many OLAP systems that store semistructured data._

---

> _Additional normal forms exist (up to 6NF in the Boyce-Codd system), but these are much less common than the first three. A database is usually considered normalized if it’s in third normal form,_

---

> _partial dependencies can occur only when the primary key is composite_

---

> _A unique primary key is a single field or set of multiple fields that uniquely determines rows in the table. Each key value occurs at most once; otherwise, a value would map to multiple rows in the table. Thus, every other value in a row is dependent on (can be determined from) the key. A partial dependency occurs when a subset of fields in a composite key can be used to determine a nonkey column of the table. A transitive dependency occurs when a nonkey field depends on another nonkey field._

---

> _The goal of normalization is to remove the redundancy of data within a database and ensure referential integrity. Basically, it’s don’t repeat yourself (DRY) applied to data in a database._

---

> _it’s often accompanied by a date or timestamp for increased fidelity._

---

> _the grain of the data, which is the resolution at which data is stored and queried. The grain is typically at the level of a primary key in a table_

---

> _watermark (Figure 8-8) is a threshold used by a window to determine whether data in a window is within the established time interval or whether it’s considered late._

---

> _Sliding windows_

---

> _Fixed-time windows_

---

> _batch is a special case of streaming._

---

> _Session windows may also make a provision for late-arriving data. Allowing data to arrive up to five minutes late to account for network conditions and system latency, the system will open the window if a late-arriving event indicates activity less than five minutes after the last event._

---

> _The system accumulates data per user. If a five-minute gap with no activity occurs, the system closes the window, sends its calculations, and flushes the data. If new events arrive for the user, the system starts a new session window._

---

> _A session window groups events that occur close together, and filters out periods of inactivity when no events occur. We might say that a user session is any time interval with no inactivity gap of five minutes or more_

---

> _One fundamental limitation of traditional batch queries is that this paradigm generally treats the query engine as an external observer. An actor external to the data causes the query to run—perhaps an hourly cron job or a product manager opening a dashboard._
>
> _Most widely used streaming systems, on the other hand, support the notion of computations triggered directly from the data itself. They might emit mean and median statistics every time a certain number of records are collected in the buffer or output a summary when a user session closes._

---

> _Production databases generally aren’t equipped to handle production workloads and simultaneously run large analytics scans across significant quantities of data. Running such queries can slow the production application or even cause it to crash.3 The basic CDC query pattern allows us to serve real-time analytics with a minimal impact on the production system_

---

> _sets up an analytics database as a fast follower to a production database. One of the longest-standing streaming query patterns simply entails querying the analytics database, retrieving statistical results and aggregations with a slight lag behind the production database._

---

> _materialized views provide another form of query caching_

---

> _deleting dead database records is important for a few reasons. First, it frees up space for new records, leading to less table bloat and faster queries. Second, new and relevant records mean query plans are more accurate; outdated records can lead the query optimizer to generate suboptimal and inaccurate plans. Finally, vacuuming cleans up poor indexes, allowing for better index performance._

---

> _transactions incur the overhead of creating new records during certain operations, such as updates, deletes, and index operations, while retaining the old records as pointers to the last state of the database. As these old records accumulate in the database filesystem, they eventually no longer need to be referenced. You should remove these dead records in a process called vacuuming._

---

> _A database commit is a change within a database, such as creating, updating, or deleting a record, table, or other database objects. Many databases support transactions—i.e., a notion of committing several operations simultaneously in a way that maintains a consistent state. Please note that the term transaction is somewhat overloaded; see Chapter 5. The purpose of a transaction is to keep a consistent state of a database both while it’s active and in the event of a failure. Transactions also handle isolation when multiple concurrent events might be reading, writing, and deleting from the same database objects. Without transactions, users would get potentially conflicting information when querying a database._

---

> _In addition to using EXPLAIN to understand how your query will run, you should monitor your query’s performance, viewing metrics on database resource consumption._

---

> _When you execute a SQL query, here’s a summary of what happens:_

---

> _transaction control language (TCL) supports commands that control the details of transactions. With TCL, we can define commit checkpoints, conditions when actions will be rolled back, and mor_

---

> _Data control language (DCL) allows you to control access to the database objects or the data by using SQL_

---

> _add and alter data within these objects, which is the primary purpose of data manipulation language (DML)_

---

> _data definition language (DDL) commands to perform operations on database objects, such as the database itself, schemas, tables, or users; DDL defines the state of objects in your database_

### 9. Serving Data for Analytics, Machine Learning, and Reverse ETL

> _The rise of analytics and ML IaC means the role of writing code is moving toward building the systems that support data scientists and analysts. Data engineers might be responsible for setting up the CI/CD pipelines and building processes for their data team. They would also do well to train and support their data team in using the Data/MLOps infrastructure they’ve built so that these data teams can be as self-sufficient as possible._

---

> _Data scientists are notorious for doing most development on their local machines. As discussed earlier, encourage them to migrate these workflows to common systems in a cloud environment, where data teams can collaborate in dev, test, and production environments and create proper production architectures. Facilitate your analysts and data scientists by supporting tools for publishing data insights with little encumbrance._

---

> _you should view access control and security not as impediments to serving but as key enablers._

---

> _A good approach is to mediate access through filtered views, thus alleviating the security risks inherent in sharing access to a common table. Another suggestion is to use data sharing in your workflows, which allows for read-only granular controls between you and people consuming your data._

---

> _Of all the lifecycle stages, serving presents the largest security surface._

---

> _A big consideration for data engineers in the serving stage of the lifecycle is the separation of duties and concerns. If you’re at an early-stage company, the data engineer may also be an ML engineer or data scientist; this is not sustainable. As the company grows, you need to establish a clear division of duties with other data team members._

---

> _While you can roll your reverse ETL solution, many off-the-shelf reverse ETL options are available. We suggest using open source, or a commercial managed service. That said, the reverse ETL space is changing extremely quickly. No clear winners have emerged, and many reverse ETL products will be absorbed by major clouds or other data product vendors. Choose carefully_

---

> _Reverse ETL inherently creates feedback loops._

---

> _the data engineer operates in a support role for these stakeholders and is not necessarily responsible for the end uses of data._

---

> _Any data exchange between organizations or units within a larger organization can be viewed as data sharing. Still, we mean specifically sharing through massively multitenant storage systems in a cloud environment. Data sharing generally turns data serving into a security and access control problem._

---

> _the boundary between ML, data science, data engineering, and ML engineering is increasingly fuzzy, and this boundary varies dramatically between organizations. In some organizations, ML engineers take over data processing for ML applications right after data collection or may even form an entirely separate and parallel data organization that handles the entire lifecycle for all ML applications. Data engineers handle all data processing in other settings and then hand off data to ML engineers for model training. Data engineers may even handle some extremely ML-specific tasks, such as featurization of data_

---

> _the boundary between ML, data science, data engineering, and ML engineering is increasingly fuzzy, and this boundary varies dramatically between organizations_

---

> _Users want low data latency. Second, users of data apps expect fast query performance. When they adjust parameters in an analytics dashboard, they want to see refreshed results appear in seconds. Third, data apps must often support extremely high query rates across many dashboards and numerous customers. High concurrency is critical._

---

> _you’ll need to understand the speed and latency requirements for embedded analytics._
>
> _Performance for embedded analytics encompasses three problems. First, app users are not as tolerant of infrequent batch processing as internal company analysts_

---

> _Whereas business and operational analytics are internally focused, a recent trend is external-facing or embedded analytics. With so much data powering applications, companies increasingly provide analytics to end users. These are typically referred to as data applications, often with analytics dashboards embedded within the application itself. Also known as embedded analytics, these end-user-facing dashboards give users key metrics about their relationship with the application_

---

> _An example of operational analytics is real-time application monitoring. Many software engineering teams want to know how their application is performing; if issues arise, they want to be notified immediately_

---

> _The big difference between operational and business analytics is time. Data used in business analytics takes a longer view of the question under consideration. Up-to-the-second updates are nice to know but won’t materially impact the quality or outcome. Operational analytics is quite the opposite, as real-time updates can be impactful in addressing a problem when it occurs_

---

> _operational analytics uses data to take immediate action:_

---

> _It is common to have mixed data update frequencies to serve use cases appropriately but remember that the frequency of ingestion sets a ceiling on downstream frequency. If streaming applications exist for the data, it should be ingested as a stream even if some downstream processing and serving steps are handled in batches._

---

> _Good analysts constantly engage with the business and dive into the data to answer questions and uncover hidden and counterintuitive trends and insights. They also work with data engineers to provide feedback on data quality, reliability issues, and requests for new datasets. The data engineer is responsible for addressing this feedback and providing new datasets for the analyst to use._

---

> _The analyst was asked to dig into a potential issue and come back with insights. This represents an example of ad hoc analysis. Reports typically start as ad hoc requests. If the results of the ad hoc analysis are impactful, they often end up in a report or dashboard._

---

> _Analysts are often tasked by business stakeholders with creating a report._

---

> _you might use BI platforms to create dashboards, such as Tableau, Looker, Sisense, Power BI, or Apache Superset/Preset._

---

> _A dashboard concisely shows decision makers how an organization is performing against a handful of core metrics, such as sales and customer retention. These core metrics are presented as visualizations (e.g., charts or heatmaps), summary statistics, or even a single number. This is similar to a car dashboard, which gives you a single readout of the critical things you need to know while driving a vehicle._

---

> _Business analytics typically falls into a few big areas—dashboards, reports, and ad hoc analysis. A business analyst might focus on one or all of these categories._

---

> _Business analytics uses historical and current data to make strategic and actionable decisions. The types of decisions tend to factor in longer-term trends and often involve a mix of statistical and trend analysis, alongside domain expertise and human judgment. Business analysis is as much an art as it is a science_

---

> _Second, each team potentially runs its dashboards and analytics for self-service_

---

> _Data mesh fundamentally changes the way data is served within an organization. Instead of siloed data teams serving their internal constituents, every domain team takes on two aspects of decentralized, peer-to-peer data serving._
>
> _First, teams are responsible for serving data to other teams by preparing it for consumption._

---

> _Using a semantic layer, you consolidate business definitions and logic in a reusable fashion. Write once, use anywhere. This paradigm is an object-oriented approach to metrics, calculations, and logic_

---

> _Frequently, we see data definitions and logic taken for granted, often passed around the organization in the form of institutional knowledge. Institutional knowledge takes on a life of its own, often at the expense of anecdotes replacing data-driven insights, decisions, and actions. Instead, formally declaring data definitions and logic both in a data catalog and within the systems of the data engineering lifecycle goes a long way to ensuring data correctness, consistency, and trustworthiness._

---

> _Data logic stipulates formulas for deriving metrics from data_

---

> _the correctness of data goes beyond faithful reproduction of event values from source systems. Data correctness also encompasses proper data definitions and logic;_

---

> _Data definition refers to the meaning of data as it is understood throughout the organization_

---

> _attempts at self-service data begin with great intentions but ultimately fail_

---

> _seeking use cases, always ask, “What action will this data trigger, and who will be performing this action?,” with the appropriate follow-up question, “Can this action be automated?_

---

> _Regardless of its form, an SLA tells users what to expect from your data product; it is a contract between you and your stakeholders. An example of an SLA might be, “Data will be reliably available and of high quality.” An SLO is a key part of an SLA and describes the ways you’ll measure performance against what you’ve agreed to. For example, given the preceding example SLA, an SLO might be, “Our data pipelines to your dashboard or ML workflow will have 99% uptime, with 95% of data free of defects.” Be sure expectations are clear and you have the ability to verify you’re operating within your agreed SLA and SLO parameters._

### 10. Security and Privacy

> _In principle, network security should be left to security experts at your company. (In practice, you may need to assume significant responsibility for network security in a small company.)_

---

> _sometimes hardened perimeter security still makes sense; we find some solace in the knowledge that nuclear missile silos are air gapped (not connected to any networks). Air-gapped servers are the ultimate example of a hardened security perimeter._

---

> _Here are some areas you should monitor_

---

> _Some data must be retained but should be accessed only in an emergency. Put this data behind a broken glass process: users can access it only after going through an emergency approval process to fix a problem, query critical historical information, etc. Access is revoked immediately once the work is done._

---

> _Treat humans and machines the same way: give them only the privileges and data they need to do their jobs, and only for the timespan when needed._

---

> _Security needs to be simple and effective enough to become habitual throughout an organization. We’re amazed at the number of companies with security policies in the hundreds of pages that nobody reads, the annual security policy review that people immediately forget, all in checking a box for a security audit. This is security theater, where security is done in the letter of compliance (SOC-2, ISO 27001, and related) without real commitment._

---

> _With our corporate clients, we see a pervasive focus on compliance (with internal rules, laws, recommendations from standards bodies), but not enough attention to potentially bad scenarios. Unfortunately, this creates an illusion of security but often leaves gaping holes that would be evident with a few minutes of reflection._

---

> _When people follow regular security processes, security becomes part of the job. Make security a habit, regularly practice real security, exercise the principle of least privilege, and understand the shared responsibility model in the cloud._

---

> _You are also the first line of defense in respecting privacy and ethics. Are you uncomfortable with sensitive data you’ve been tasked to collect? Do you have ethical questions about the way data is being handled in a project? Raise your concerns with colleagues and leadership. Ensure that your work is both legally compliant and ethical._

---

> _Data engineers should actively think through the scenarios for data utilization and collect sensitive data only if there is an actual need downstream. The best way to protect private and sensitive data is to avoid ingesting this data in the first place._
>
> _Data engineers should think about the attack and leak scenarios with any data pipeline or storage system they utilize. When deciding on security strategies, ensure that your approach delivers proper security and not just the illusion of safety._

---

> _In a world obsessed with positive thinking, negative thinking is distasteful_

---

> _Take a defensive posture with everything you do online and offline. Exercise the power of negative thinking and always be paranoid._

---

> _The weakest link in security and privacy is you._

---

> _Security is a key ingredient for privacy._

---

> _security is the first thing a data engineer needs to think about in every aspect of their job and every stage of the data engineering lifecycle_

### 11. The Future of Data Engineering

> _While the data warehouse and data lake are great for housing large amounts of data and performing ad hoc queries, they are not so well optimized for low-latency data ingestion or queries on rapidly moving data. The live data stack will be powered by OLAP databases that are purpose-built for streaming. Today, databases like Druid, ClickHouse, Rockset, and Firebolt are leading the way in powering the backend of the next generation of data applications._

---

> _Real-time analytical databases enable both fast ingestion and subsecond queries on this data_

---

> _Just as the MDS took advantage of the cloud and brought on-premises data warehouse and pipeline technologies to the masses, the live data stack takes real-time data application technologies used at elite tech companies and makes them available to companies of all sizes as easy-to-use cloud-based offerings_

---

> _In many cases, analytics (BI and operational analytics) will be replaced by automation. Presently, most dashboards and reports answer questions concerning what and when. Ask yourself, “If I’m asking a what or when question, what action do I take next?” If the action is repetitive, it is a candidate for automation. Why look at a report to determine whether to take action when you can instead automate the action based on events as they occur?_

---

> _the MDS is basically a repackaging of old data warehouse practices using modern cloud and SaaS technologies;_

---

> _One possibility is a role that sits between ML engineering and data engineering. As ML toolsets become easier to use and managed cloud ML services grow in capabilities, ML is shifting away from ad hoc exploration and model development to become an operational discipline._
>
> _This new ML-focused engineer who straddles this divide will know algorithms, ML techniques, model optimization, model monitoring, and data monitoring. However, their primary role will be to create or utilize the systems that automatically train models, monitor performance, and operationalize the full ML process for model types that are well understood. They will also monitor data pipelines and quality, overlapping into the current realm of data engineering._

---

> _the boundaries between software engineering, data engineering, data science, and ML engineering are increasingly fuzzy. In fact, like the authors, many data scientists are transformed into data engineers through an organic process; tasked with doing “data science” but lacking the tools to do their jobs, they take on the job of designing and building systems to serve the data engineering lifecycle._

---

> _some of the good things that larger companies do with data—management, operations, governance, and other “boring” stuff. We’re presently living through the golden age of “enterprisey” data management tools. Technologies and practices once reserved for giant organizations are trickling downstream. The once hard parts of big data and streaming data have now largely been abstracted away, with the focus shifting to ease of use, interoperability, and other refinements._
>
> _This allows data engineers working on new tooling to find opportunities in the abstractions of data management, DataOps, and all the other undercurrents of data engineering. Data engineers will become “enterprisey._

---

> _We will also see significant improvements in the scaffolding that manages cloud data services. Apache Airflow has emerged as the first truly cloud-oriented data orchestration platform, but we are on the cusp of significant enhancement. Airflow will grow in capabilities, building on its massive mindshare. New entrants such as Dagster and Prefect will compete by rebuilding orchestration architecture from the ground up._

---

> _Another critical ingredient of a data API ecosystem is a metadata catalog that describes schemas and data hierarchies. Currently, this role is largely filled by the legacy Hive Metastore. We expect that new entrants will emerge to take its place._

---

> _data engineering will gradually coalesce around a handful of data interoperability standards._

---

> _The simplified data services that we’ve mentioned throughout this book (e.g., Google Cloud BigQuery, Azure Blob Storage, Snowflake, and AWS Lambda) resemble operating system services, but at a much larger scale, running across many machines rather than a single server._

---

> _Another significant trend is the growth in popularity of off-the-shelf data connectors (at the time of this writing, popular ones include Fivetran and Airbyte). Data engineers have traditionally spent a lot of time and resources building and maintaining plumbing to connect to external data sources. The new generation of managed connectors is highly compelling, even for highly technical engineers, as they begin to recognize the value of recapturing time and mental bandwidth for other projects. API connectors will be an outsourced problem so that data engineers can focus on the unique issues that drive their businesses._

---

> _managed open source is just as easy to use as its proprietary service competitors. Companies with highly specialized needs can also deploy managed open source, then move to self-managed open source later if they need to customize the underlying code._

---

> _The cloud is responsible for a significant shift in the usage of open source tools._

---

> _Simplified, easy-to-use tools continue to lower the barrier to entry for data engineering. This is a great thing, especially given the shortage of data engineers we’ve discussed. The trend toward simplicity will continue. Data engineering isn’t dependent on a particular technology or data size. It’s also not just for large companies. In the 2000s, deploying “big data” technologies required a large team and deep pockets. The ascendance of SaaS-managed services has largely removed the complexity of understanding the guts of various “big data” systems. Data engineering is now something that all companies can do._

---

> _While data science has received the bulk of the attention in recent years, data engineering is rapidly maturing into a distinct and visible field. It’s one of the fastest-growing careers in technology, with no signs of losing momentum. As companies realize they first need to build a data foundation before moving to “sexier” things like AI and ML, data engineering will continue growing in popularity and importance. This progress centers around the data engineering lifecycle._
