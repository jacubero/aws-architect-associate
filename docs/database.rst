Adding a database layer
#######################

Amazon RDS
**********

Amazon Ralational Database Service (RDS) is a manageed relational database with a choice of 6 popular database engines: Amazon Aurora, MySQL, PostgreSQL, MariaDB, Microsoft SQL Server and Oracle. This service has the following characteristics:

* **Easy to administer**. As Amazon RDS is a managed service, you manage application optimization tasks (schema design, query construction, query optimization) and AWS manages infrastructure tasks (power, HVAC, network, rack & stack, installation, routine maintenance, automated patching, scaling and monitoring, industry compliance, isolation & security, backup & recovery, High Availability).

* **Available and durable**. It provides automatic Multi-AZ data replication, automated backup, snapshots, and failover.

* **Highly scalable**. It scales DB compute and storage with a few clicks with no application downtime.

* **Fast and secure**. It provides SSD storage and guaranteed provisioned I/O; data encryption at rest and in transit.

`Amazon Relational Database Service (Amazon RDS) <https://www.youtube.com/watch?time_continue=3&v=igRfulrrYCo&feature=emb_logo>`_

Get started with RDS
====================

DB instances
------------

The basic building block of Amazon RDS is the DB instance. A DB instance is an isolated DB environment that can contain multiple user-created DBs and can be accessed by using the same tools and applications that you use with an standalone DB instance. The resources found in a DB instance are determined by its DB instance class, and the type of storage is dictated by the type of disks. DB instances and storage differ in performance characteristics and price, allowing you to tailor your performance and cost to the needs of your DB. When you choose to create a DB instance, you first have to specify which **DB engine** to run. Amazon RDS currently supports 2 commercial engines (MS SQL Server and Oracle), 3 open source (MySQL, PostgreSQL, and MariaDB) and 1 cloud native (Amazon Aurora). 

.. figure:: /database_d/rdsinstance.png
   :align: center

   Amazon RDS DB instance

DB instances with commercial and open source DB engines use Amazon Elastic Block Store (Amazon EBS) volumes for database and log storage. Depending on the amount of storage requested, Amazon RDS automatically stripes across multiple Amazon EBS volumes to enhance performance. Amazon Aurora, which is MSQL and PostgreSQL compatible, uses purpose-built distributed, log-structured storage system.

If you are developing a new application, then it is recommended to go with the newest DB engine version. If you are migrating an existing application, then it is necessary to check compatibility requirements.

You can run Amazon RDS on VMware through the Amazon RDS connector. It packages technologies at the core of Amazon RDS in AWS and deploys them on premises. You need connectivity to AWS via a dedicated VPN tunnel enables database management entirely within your private data center.

Instance types
--------------

Amazon RDS provides a selection of instance types optimized to fit different relational database use cases. Each instance type includes serveral instance sizes, allowing you to scale your database to the requirements of your target workload. Not every instance type is supported for every database engine, version, edition or region. The current Amazon RDS Instance Types are:

* General purpose: T3, T2, M5, M4.

* Memory optimized: R5, R4, X1e, X1, Z1d.

You can scale compute and memory vertically up or down. The new host is attaches to existing storage with minimal downtime. The endpoint will be the same, but you will have to reconnect to the new instance. 

Storage types
-------------

Amazon RDS provides three storage types: General Purpose SSD (also known as gp2), Provisioned IOPS SSD (also known as io1), and magnetic. The following list briefly describes the three storage types:

* **General Purpose SSD**. General Purpose SSD volumes offer cost-effective storage that is ideal for a broad range of workloads. These volumes deliver single-digit millisecond latencies and the ability to burst to 3,000 IOPS for extended periods of time. Baseline performance for these volumes is determined by the volume's size.

* **Provisioned IOPS**. Provisioned IOPS storage is designed to meet the needs of I/O-intensive workloads, particularly database workloads, that require low I/O latency and consistent I/O throughput.

* **Magnetic**. Amazon RDS also supports magnetic storage for backward compatibility. We recommend that you use General Purpose SSD or Provisioned IOPS for any new storage needs. The maximum amount of storage allowed for DB instances on magnetic storage is less than that of the other storage types. 

General Purpose SSD is a great choice, but you have to be aware of burst credits on volumes less than 1 TB. Hitting credit-depletion results in IOPS drop, latencry and queue depth metrics will sppike until credits are replenished. You have to monitor ``BurstBalance`` to see the percent of burst-bucket I/O credits available. You have to monitor read/write IOPS to see if average IOPS is greater than the baseline. You can think General Purpose SSD burst rate and PIOPS stated rate as maximum I/O rates.

You can scale up Amazon EBS storage with no downtime. Initial scaling operation may take longer, because storage is reconfigured on older instances. You can re-provision IOPS on the fly without any disruption in the storage. You are limited to scale up to once every 6 hours.

Managing High Availability, read replicas, and backups
======================================================

High Availability with Multi-AZ
-------------------------------

Multi-AZ provides enterprise-grade fault-tolerance solution for production databases. Once configured, Amazon RDS automatically generates a standby copy of the primary instance in another AZ within the same Amazon VPC. Each DB instance manages a set of Amazon EBS volumes with a full copy of the data. After seeding the DB copy, transactions are synchronously replicated to the standby copy. Instances are monitored by an external observer to maintain consensus over quorum.

.. figure:: /database_d/RDSmultiAZ.png
   :align: center

   High Availability with Multi-AZ

Running a DB instance with Multi-AZ can enhance availability during planned system maintenance and help protect your DBs against DB instance failure and AZ disruption. If the master DB instance fails, Amazon RDS automatically brings the standby DB online as the new primary. Failover can be initiated by automation or through the Amazon RDS API. Because of the synchronous replication, there should be no data loss. As your applications reference the DB by name using RDS DNS endpoint, you don't need to change anything in your application code to use the standby copy for failover. A new DB instance in the AZ where it was located the failed previous primary DB instance is provisioned as the new secondary DB instance.

.. Note::

	It is important to have in mind that it detects infrastructure issues, not database engine problems.

Read scalability with Amazon RDS Read Replicas
----------------------------------------------

Amazon RDS can gain read scalability with the creation of read replicas for MySQL, MariaDB, and PostgreSQL. Updates made to the source DB instance are asynchronously copied to the read replica instance. You can reduce the load on your source DB instance by routing read queries from your applications to the read replica. Using read replicas, you can also scale out beyond the capacity constraints of a single DB instance for read-heavy DB workloads. It brings data close to your applications in different regions. 

.. figure:: /database_d/readreplicas.png
   :align: center

   Amazon RDS read replicas

You can create up to 5 replicas per source database. You can monitor replication lag in Amazon CloudWatch or Amazon RDS console. Read replicas can be created in a different region than the master DB. This feature can help satisfy DR requirements or cutting down on latency by directing reads to a read replica closer to the user. Single-region read replicas is supported for Oracle EE and is coming soon for SQL Server.

Read replicas can also be promoted to become the master DB instance, but due to the asynchronous replication, this requires manual action. You can do it for faster recovery in the event of a disaster. You can upgrade a read replica to a new engine version.

.. list-table:: Multi-AZ vs Read Replicas
   :widths: 50 50
   :header-rows: 1

   * - Multi-AZ
     - Read Replicas
   * - Synchronous replication:
       highly durable
     - Asynchronous replication:
       highly scalable
   * - Only primary instance is active
       at any point in time
     - All replicas are active and 
       can be used for read scaling
   * - Backups can be taken from secondary
     - No backups configured by default
   * - Always in 2 AZs within a region
     - It can be within an AZ, cross-AZ,
       or cross-region
   * - Database engine version upgrades
       happen on primary
     - Database engine version upgrades
       independently from source instance

Plan for DR
-----------

You can plan for disaster recovery by using automated backups and manual snapshots. You can use a cross-region read replica as a standby database for recovery in the event of a disaster. Read replicas can be configured for Multi-AZ to reduce recovery time. 

.. figure:: /database_d/rds_dr.png
   :align: center

   Disaster recovery with Multi-AZ and read replicas

This architecture is supported for MySQL, MariaDB and PostgreSQL. For Oracle and SQL Server, you can use cross-region backup copies.

.. Note::

	You can use delayed replication for MySQL to protect from self-inflicted disasters. 

Backups
-------

Amazon RDS can manage backups using one of these two options:

* You can do **manual snapshots**. These are storage level snapshots with no performance penalty for backups in multi-AZ configurations and only a brief pause in you I/O for single-AZ configurations. It leverages EBS snapshots stored in Amazon S3.

* **Automated backups** gives you a point-in-time restore capability. AWS will take snapshots once a day and capture transactions logs and store them every 5 minutes in S3.

Snapshots can be copied across regions or shared with other accounts.

Monitor 
-------

Amazon RDS comes with comprehensive monitoring built-in:

* **Amazon CloudWatch metrics and alarms**. It allows you to monitor core metrics: CPU, memory, storage, I/O, throughput, latency, replica lag. The monitoring interval is usually down to 1 minute. You can configure alarms on these metrics.

* **Amazon CloudWatch logs**. It allows publishing DB logs (errors, audit, slow queries) to a centralized log store (except SQL Server). You can access logs directly from RDS console and API for all engines.

* **Enhanced monitoring**. It is an agent-based monitoring system that allows you to have access to additional CPU, memory, file system, database engine, and disk I/O metrics. It is configurable to monitor up to 1 second intervals. They are automatically published to Amazon CloudWatch logs on your behalf.

* **Performance Insights** uses lightweight data collection methods that don’t impact the performance of your applications, and makes it easy to see which SQL statements are causing the load, and why. It requires no configuration or maintenance, and is currently available for Amazon Aurora (PostgreSQL- and MySQL-compatible editions), Amazon RDS for PostgreSQL, MySQL, MariaDB, SQL Server and Oracle. It provides an easy and powerful dashboard showing load on your database. It helps you identify source of bottlenecks: top SQL queries, wait statistics. It has an adjustable time frame (hour, day week, month). With 7 days of free performance history retention, it's easy to track down and solve a wide variety of issues. If you need longer-term retention, you can choose to pay for up to two years of performance history retention.

Events
------

Amazon RDS event notifications let you know when important things happen. You can leverage built-in notifications via Amazon SNS. Events are published to Amazon CloudWatch Events, where you can create rules to respond to the events. It supports cross-account event delivery. There are 6 different source types: DB instance, DB parameter group, DB security group, DB snapshot, DB cluster, DB cluster snapshot. There are 17 different event categories, such as availability, backup, deletion, configuration change, etc.

Security controls
=================

Data Protection
---------------

Identity and Access Management
------------------------------

IAM Database Authentication for MySQL and PostgreSQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can authenticate to your DB instance using AWS Identity and Access Management (IAM) database authentication. IAM database authentication works with MySQL and PostgreSQL. With this authentication method, you don't need to use a password when you connect to a DB instance. Instead, you use an authentication token.

An *authentication token* is a unique string of characters that Amazon RDS generates on request. Authentication tokens are generated using AWS Signature Version 4. Each token has a lifetime of 15 minutes. You don't need to store user credentials in the database, because authentication is managed externally using IAM. You can also still use standard database authentication.

IAM database authentication provides the following benefits:

1. Network traffic to and from the database is encrypted using Secure Sockets Layer (SSL).

2. You can use IAM to centrally manage access to your database resources, instead of managing access individually on each DB instance.

3. For applications running on Amazon EC2, you can use profile credentials specific to your EC2 instance to access your database instead of a password, for greater security

`IAM Database Authentication for MySQL and PostgreSQL <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html>`_

Use cases
=========

Amazon RDS is ideal for:

* **Web and mobile applications** that need a DB with high throughput, massive storage scalability, and HA. Since RDS does not have any licensing contraints, it perfectly fits the variable usage pattern of these applications.

* For **E-commerce applications**, RDS provides a flexible, secured, and low-cost DB solution for online sales and retailing. 

* **Mobile and online games** require a DB platform with high throughput and HA. RDS manages the DB infrastructure so game developers don't have to worry about provisioning, scaling or monitoring DB servers.

Costs
=====

To estimate the cost of using RDS, you need to consider the following factors:

* **Clock hours of server time**, from the time you launch a DB instance until you terminate it.

* **Database characteristics**. Engine, size, and memory class impacts costs.

* **Database purchase type**. On-demand DB instances are charged by the hour. Reserved DB instances require upfront payment for DB instances reserved.

* **Number of database instances**, to handle peak loads.

* **Provisioned storage**. There is no additional charge for backup storage of up to 100% of your provisioned DB storage for an active DB instance. After the DB instance is terminated, backup storage is billed per GB/month.

* **Additional storage**. The amount of backup storage in addition to the provisioned storage amount is billed per GB/month.

* **Requests**. The number of input and output requests to the DB.

* **Deployment type**. You can deploy the DB to a single AZ or multiple AZs.

* **Outbound data transfer** is tiered and inbound data transfer is free.

In order to reduce costs you can stop and start a DB instance from the console, AWS CLIs and SDKs. There are no charges for DB instance hours while it is stopped. The backup retention window is maintained while stopped. However, instances are started automatically after 7 days and you cannot stop DB instances that have read replicas or are read replicas. If you want to stop a DB instance for more than 7 days, a possible strategy is to take an snasphot.

You can also save money by using Reverved Instances (RIs) that provide a discount over on-demand prices. You have to match region, instance family and engine of on-demand usage to apply benefit. There is size flexibility available for open source and Oracle BYOL engines. By default, RIs are shared among all accounts in consolidated billing. You can use the RI utilization and coverage reports to determine how your RIs are being used. Amazon RDS RI recommendations report uses historical data to recommend which RIs to buy.

Amazon Aurora
*************

Amazon Aurora is a fully managed, relational DBaaS that combines the speed and reliability of high-end commercial DBs, with the simplicity and cost-effectiveness of open source databases. It is designed to be compatible with MySQL and PostgreSQL, so existing applications and tools, can run against it without modification.

It is part of Amazon RDS and it tightly integrated with an SSD-backend virtualized storage layer purposefully built to accelerate DB workloads. It delivers up to 5 times the throughput of standard MySQL and up to 3 times the throughput of standard PostgreSQL.

It can scale automatically an non-disruptively, expanding up to 64 TB and rebalancing storage I/O to provide consistent performance, without the need for over-provisioning. Aurora storage is also fault-tolerant and self-healing, so any storage failures are repaired transparently. 

It is a regional service that offers greater than 99.99% availability. The service is designed to automatically detect DB crashes and restart the DB without the need for crash recovery or DB rebuilds. If the entire instance fails, Amazon Aurora automatically fails over to one of up to 15 read replicas.

Amazon DynamoDB
***************






Migrating data into your AWS databases
**************************************
