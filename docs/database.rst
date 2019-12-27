Adding a database layer
#######################

Database layer considerations
*****************************

Amazon RDS and Amazon DynamoDB
******************************

Amazon RDS
==========

With Amazon RDS you manage Application optimization and AWS manages: OS installation and patches, DB software install and patches, DB backups, HA, Scaling, Power and rack & stack, server maintenance.

The basic building block of Amazon RDS is the DB instance. A DB instance is an isolated DB environment that can contain multiple user-created DBs and can be accessed by using the same tools and applications that you use with an standalone DB instance. The resources found in a DB instance are determined by its DB instance class, and the type of storage is dictated by the type of disks. DB instances and storage differ in performance characteristics and price, allowing you to tailor your performance and cost to the needs of your DB. When you choose to create a DB instance, you first have to specify which DB engine to run. Amazon RDsS currently supports MySQL, Amazon Aurora, MS SQL Server, PostgreSQL, MariaDB and Oracle. 

.. figure:: /database_d/rds.png

	Amazon RDS DB instance

High Availability with Multi-AZ
-------------------------------

One of the most powerful features of Amazon RDS is the ability to configure your DB instance for HA with a multi-AZ deployment. Once configured, Amazon RDS automatically generates a standby copy of the DB instance in another AZ within the same Amazon VPC. After seeding the DB copy, transactions are synchronously replicated to the standby copy. Running a DB instance with Multi-AZ can enhance availability during planned system maintenance and help protect your DBs against DB instance failure and AZ disruption. If the master DB instance fails, Amazon RDS automatically brings the standby DB online as the new master. Because of the synchronous replication, there should be no data loss. Because your applications reference the DB by name using RDS DNS endpoint, you don't need to change anything in your application code to use the standby copy for failover.

.. figure:: /database_d/multiAZ.png

	High Availability with Multi-AZ

Amazon RDS Read Replicas
------------------------

Amazon RDS also supports the creation of read replicas for MySQL, MariaDB, PostgreSQL and Amazon Aurora. Updates made to the source DB instance are aynchronously copied to the read replica instance. You can reduce the load on your source DB instance by routing read queries from your applications to the read replica. Using read replicas, you can also scale out beyond the capacity constraints of a single DB instance for read-heavy DB workloads. Read replicas can also be promoted to become the master DB instance, but due to the asynchronous replication, this requires manual action.

.. figure:: /database_d/read.png

	Amazon RDS read replicas

Read replicas can be created in a different region than the master DB. This feature can help satisfy DR requirements or cutting down on latency by directing reads to a read replica closer to the user. 

Use cases
---------

Amazon is ideal for:

* **Web and mobile applications** that need a DB with high throughput, massive storage scalability, and HA. Since RDS does not have any licensing contraints, it perfectly fits the variable usage pattern of these applications.

* For **E-commerce applications**, RDS provides a flexible, secured, and low-cost DB solution for online sales and retailing. 

* **Mobile and online games** require a DB platform with high throughput and HA. RDS manages the DB infrastructure so game developers don't have to worry about provisioning, scaling or monitoring DB servers.

Cost factors
------------

To estimate the cost of using RDS, you need to consider the following:

* **Clock hours of server time**, from the time you launch a DB instance until you terminate it.

* **Database characteristics**. Engine, size, and memory class impacts costs.

* **Database purchase type**. On-demand DB instances are charged by the hour. Reserved DB instances require upfront payment for DB instances reserved.

* **Number of database instances**, to handle peak loads.

* **Provisioned storage**. There is no additional charge for backup storage of up to 100% of your provisioned DB storage for an active DB instance. After the DB instance is terminated, backup storage is billed per GB/month.

* **Additional storage**. The amount of backup storage in addition to the provisioned storage amount is billed per GB/month.

* **Requests**. The number of input and output requests to the DB.

* **Deployment type**. You can deploy the DB to a single AZ or multiple AZs.

* **Outbound data transfer** is tiered and inbound data transfer is free.

Amazon Aurora
-------------

Amazon Aurora is a fully managed, relational DBaaS that combines the speed and reliability of high-end commercial DBs, with the simplicity and cost-effectiveness of open source databases. It is designed to be compatible with MySQL and PostgreSQL, so existing applications and tools, can run against it without modification.

It is part of Amazon RDS and it tightly integrated with an SSD-backend virtualized storage layer purposefully built to accelerate DB workloads. It delivers up to 5 times the throughput of standard MySQL and up to 3 times the throughput of standard PostgreSQL.

It can scale automatically an non-disruptively, expanding up to 64 TB and rebalancing storage I/O to provide consistent performance, without the need for over-provisioning. Aurora storage is also fault-tolerant and self-healing, so any storage failures are repaired transparently. 

It is a regional service that offers greater than 99.99% availability. The service is designed to automatically detect DB crashes and restart the DB without the need for crash recovery or DB rebuilds. If the entire instance fails, Amazon Aurora automatically fails over to one of up to 15 read replicas.

Amazon DynamoDB
===============


Security controls for Amazon RDS and DynamoDB
*********************************************

Migrating data into your AWS databases
**************************************