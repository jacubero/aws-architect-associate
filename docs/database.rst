Adding a database layer
#######################

Database layer considerations
*****************************

Amazon RDS and Amazon DynamoDB
******************************

Amazon RDS
==========

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