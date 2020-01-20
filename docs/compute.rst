Adding a compute layer
######################

Resources
*********

Instances
=========

Inside AWS physical servers, there are hypervisors on which guest virtual machines live, called Elastic Compute Cloud (EC2) instances. AWS provides various configurations of CPU, memory, storage, and networking capacity for your instances, known as *instance types*. In 2007, AWS provide only one instance type called M1, since then a lot of instances types have been launched by AWS (175 instances type since 2007 to 2018). This continued rapid pace of innovation has been possible thanks to the `AWS Nitro System <https://aws.amazon.com/ec2/nitro/>`_.

.. figure:: /compute_d/ec2.png
   :align: center

	 Amazon EC2

Amazon EC2 instance types
-------------------------

An exammple of an API name of an EC2 instance type is ``M5d.xlarge``.  The first character (in this example ``M``) identifies the instance family. Each instance family is designed for an specific workload needs in terms of CPU, memory, storage and network performance. Amazon EC2 families define different ratios among CPU, memory, storage and network performance. Below you an find the current instance families together with the letters associated with them, and the meaning of each of the letters:

* **General Purpose**: ``A`` : ARM, ``T``: Turbo(Burstable), ``M``: Most Scenarios.

* **Compute Optimized**: ``C``: Compute.

* **Memory Optimized**: ``R``: Random-access memory, ``X``: Extra-large memory (approx 4 TB DRAM), ``U``: High memory (purpose built to run large in-memory databases), ``z``: High frequency.

* **Accelerated Computing**: ``P``: GPU optimized for machine learning, ``G``: GPU optimized for graphics, ``F``: FPGA, ``Inf``: Inferentia chips.

* **Storage Optimized**: ``I``: I/O (NVMe local), ``D``: Dense storage (48 TB local), ``H``: HDD (16 TB local).

The second character represents the instance generation (in this example ``5``). Sometimes, there is an additional characters between the instance generation and the dot. This characters can be one of the following:

* **a**: AMD CPUs.

* **e**: Extra Capacity (Storage or RAM).

* **n**: Network optimized.

* **d**: Direct-attached instance storage (NVMe).

* **g**: ARM-based AWS Graviton CPUs.

After the dot, you have the instance size (in this example ``xlarge``). From nano to large sizes the number of vCPUs is 2 and the number of GiB in memory starts from 0.5 and doubles in the immediate higher instance size. For instance sizes greater than ``large``, you should multiply the CPU and memory by the number that is before ``x``. If there is no number, ``1`` is considered. The instance size called ``metal`` corresponds with Bare metals instance and usually has the same amount of vCPU and memory as the biggest virtual instance size. The following table illustrates instance sizes characteristics:

.. list-table:: Instance sizes characteristics.
    :widths: 60 20 20
    :header-rows: 1

    * - Instance Size

      - vCPU

      - Memory (GiB)

    * - nano

      - 2

      - 0.5

    * - micro

      - 2

      - 1

    * - small

      - 2

      - 2

    * - medium

      - 2

      - 4

    * - large

      - 2

      - 8

    * - xlarge

      - 4

      - 16

    * - 2xlarge

      - 8

      - 32

    * - :math:`\cdots`

      - :math:`\cdots`

      - :math:`\cdots`

    * - :math:`y` xlarge

      - :math:`y \times 2`

      - :math:`y \times 8`

.. figure:: /compute_d/nomenclature.png
   :align: center

	 Amazon EC2 instance types nomenclature

`Amazon EC2 instance types <https://aws.amazon.com/ec2/instance-types/>`_ 

`Introducing Elastic Fabric Adapter <https://aws.amazon.com/about-aws/whats-new/2018/11/introducing-elastic-fabric-adapter/>`_

`EC2 Instance Types & Pricing <http://ec2pricing.net/>`_

Amazon Machine Images (AMIs)
----------------------------

AMI is the software required to launch an EC2 instance. There are 3 different types:

* **Amazon maintained** AMIs which offer a broad set of Linux and Windows images.

* **Marketplace maintained** AMIs managed and maintained by AWS Marketplace partners.

* **Your machine images** are AMIs you have created from Amazon EC2 instances. You can maintain them as private in your account, shared with other accounts and even made them public to the community.  

`Amazon Machine Images (AMI) <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html>`_

`How do I create an Amazon Machine Image (AMI) from my EBS-backed EC2 instance? <https://www.youtube.com/watch?time_continue=5&v=vSKWBBrEbNQ&feature=emb_logo>`_

The appropriate user names for connecting to a newly created Amazon EC2 instance are as follows:

* For an Amazon Linux AMI, the user name is ``ec2-user``.

* For a RHEL AMI, the user name is ``ec2-user`` or ``root``.

* For an Ubuntu AMI, the user name is ``ubuntu`` or ``root``.

* For a Centos AMI, the user name is ``centos``.

* For a Debian AMI, the user name is ``admin`` or ``root``.

* For a Fedora AMI, the user name is ``ec2-user``.

* For a SUSE AMI, the user name is ``ec2-user`` or ``root``.

Processors and architectures
----------------------------

There are mainly 3 types of processors:

* **Intel** Xeon processors.

* **AMD** EPYC processors.

* AWS **Graviton** processor based on 64-bit Arm architecture.

Additionally, there are multiple GPUs and FPGAs for compute acceleration.

Storage
=======

Instance store
--------------

The data in an instance store persists only during the lifetime of its associated instance. If an instance reboots (intentionally or unintentionally), data in the instance store persists. However, data in the instance store is lost under any of the following circumstances:

* The underlying disk drive fails

* The instance stops

* The instance terminates

The data is not replicated by default and no snapshot is supported. There are SSD or HDD disks configurations.

`Amazon EC2 Instance Store <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html>`_

Amazon EBS
----------

See section :ref:`secEBS`.

Networking
==========

**Virtual Private Cloud (VPC)** provision a logically isolated cloud where you can launch AWS resources into a virtual network. More information in :ref:`secVPC`.

You can use **security groups** and **ACLs** to restrict inboud and outbound traffic. **NAT Gateways** to allow an instance within a private subnet to talk to Internet. You can enable Flow Logs in any of the network interfaces, and allow you to monitor the traffic in and out these interfaces.

Within a VPN, you can add VPC endpoints to provide private and secure connectivity to S3 and DynamoDB.

Shared VPC allows multiple accounts to launch applications into a VPC.

AWS privatelink allows you the ability to have an endpoint from any VPC to share services privately to any VPC and on-premises networks. You can also use AWS privatelinks to exchange data between a VPC and a SaaS solution (for instance: Salesforce, Heroku) using AWS Direct Connect.

When you have many VPCs in your application, you can simplify the network with AWS Transit Gateway. It provides hub and spoke for managing VPCs. You essentially connect each of your VPCs to the AWS Transit Gateway, as well as the AWS Direct connect gateway and the customer gateway, all talking to each other via the AWS Transit Gateway. 

Availability
************

Regions and AZs
===============

AWS global infrastructure provides an SLA of 99.99% availability on EC2. See :ref:`secGlobalInfrastructure`

Placement groups
================

Placement groups enable you to influence AWS selection of capacity for member instances, optimizing the experience for a workload. The selection could be to make the instances fall together or fall apart.

**Cluster** placement groups. EC2 places instances closely in order to optimize the performance of inter-instance network traffic. The use case is when you want to minimize the latency among instances.

**Spread** placement groups. EC2 places instances on distinct HW in order to help reduce correlated failures. A use case could be when deploying a NoSQL database cluster in EC2, spread placement will ensure the instances in your cluster are on distinct HW, helping to insulate a single HW failure to a single node.

Elastic Load Balancing
======================

A Load Balancer is used to route incoming requests to multiple Amazon EC2 instances, containers, or IP addresses in your VPC. Elastic Load Balancing provides HA by utilizing multiple AZs.

Auto Scaling
============

Amazon EC2 Auto scaling dynamically react to changing demans, optimizing cost. 

Fleet management
----------------

A common use case is to put the EC2 instances in an auto scaling group that allows to have a health check. If one of the health checks fail, it automatically brings up a new instance to replace it.

Dynamic scaling
---------------

Another common use case is via an scaling policy that is monitoring a parameter (such as CPU utilization). If it detects a spike, it brings additional instances onboard and it will terminate those when that spike subsides.

Predictive scaling looks at the patterns of application cycles on your application and the set of applications that run on AWS and uses machine learning techniques to predict when you are going to need to scale ahead of demanda and when you need to scale down ahead of seeing drops in demand.

Management
**********

Deployment
==========

Launch templates
----------------

When you launch an instance you can specify a lot of parameters: Instance type, EBS volume, AMI ID, Network interface, tags, user data, block device mapping, placement. Some of them are mandatory and others are not. 

You can encapsulate all these parameters in a template, called **Launch template**. These templates can be useful to ensure a *consistent experience* in the organization. You can define *simple permissions*: the EC2 instances you want to launch, what are the AMIs I want them to use, what are the subnets and security group rules, and you can prevent to launch anything outside this template. Launch templates provides you with the ability to define *governance and best practices*, for instance, you can choose what can be overriden. These templates increase productivity, a common use case is using it in conjunction with Auto Scaling groups.

Launching Amazon EC2 instances with user data
---------------------------------------------

`Instance Metadata and User Data <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html>`_

Administration
==============

AWS Systems Manager
-------------------

AWS Systems Manager allows you to operate cloud and on-premises Linux and Windows workloads safely at scale in the following way:

* Stay patch and configuration compliant.

* Automate across accounts and regions.

* Connect to EC2 instances via browser and CLI.

* Track SW inventory across accounts.

* Install agents safely across instances with rate control.

AWS Resource Access Manager
---------------------------

AWS Resource Access Manager allows you to securely share AWS resources with other accounts or AWS organizations. It offers the following features:

* Reduces need to provision duplicate resources.

* Efficiently uses resources across different departments.

* AWS Identity and Access Management policies govern consumption of shared resources.

* Integration with Amazon CloudWatch and AWS CloudTrail.

* Supports resource sharing for License Manager Configs, Route 53 Resolver Rules, Subnets, and Transit Gateways.

AWS License Manager
-------------------

AWS License Manager offers a simplified license management for on premises and cloud (even if it is AWS). It offers the following features:

* More easily manage licenses from software vendors (SAP, Windows, Oracle).

* Define licensing rules, discover usage, manage access.

* Gain single view of license across AWS and on-premises.

* Discover non-compliant software and help prevent misuse.

* Seamless integration with AWS Systems Managet and AWS Organizations.

* Free service for all customers.

Monitoring
==========


.. _secEC2pricing:

Amazon EC2 pricing options
**************************

AWS offers 3 core purchasing options: On-Demand, Reserved Instances, Spot Instances. Each purchasing model launches the same underlying EC2 instances.

Using **On-demand Instances** is often where customers begin their Amazon EC2 journey, because they need to define teir needs and support spikey workloads.

Then, once customers have identified what is steady state and what is predictable, **Reserved Instances** come into play. Reserved Instances are instances that require a 1 to 3-year commitment, and in exchange, customers get a significatn discount off of On-Demand prices. This is ideals for customers' committed and more predictable, steady state use.

**Spot instances** are the most inexpensive and flexible way to access Amazon EC2 instances. 

With all these pricing models, the key is striking a balance. Use RIs for known, steady-state, predictable or always-on workloads. On-Demand, for unknown spiky workloads. Scale using Spot Instances for faul-tolerant, flexible, stateless workloads.

Cost Factors
============

To estimate the cost of using EC2, you need to consider the following:

* **Clock seconds/hours of server Time**. Resources incur charges when they are running. For example, from the time EC2 instances are launched until they are terminated, or from the time elastic IPs are allocated until the time they are de-allocated.

* **Instance configuration**. Consider the physical capacity of the EC2 instance you choose. Instance pricing varies with the AWS region, OS, instance type and instance size.

* **Number of instances**. You can provision multiple instances to handle peak loads.

* **Load balancing**. An elastic load balancer can be used to distribute traffic among EC2 instances. The number of hours the ELB runs and the amount of data it processes contribute to the monthly cost.

The product options are the following:

* **Detailed monitoring**. You can use Amazon CloudWatch to monitor your EC2 instances. By default, basic monitoring is enabled and available at no additional cost. However, for a fixed monthly rate, you can opt for detailed monitoring, which includes 7 preselected metrics recorded once a minute. Partial months are charge on an hourly prorated basis, at a per instance-hour rate.

* **Auto scaling** automatically adjusts the number of EC2 instances in your deployment according to conditions you define. This service is available at no additional charge beyond CloudWatch fees.

* **Elastic IP addresses**. You can have one Elastic IP address associated with a running instance at no charge.

Operating systems and Software packages:

* **Operating system** prices are included in the instance prices.

* **Software packages**. AWS has partnerships with Microsoft, IBM, etc. to simplify running certain commercial software packages on your EC2 instances, for example: MS SQL Server on Windows. For commercial software packages tht AWS does not provide, such as nonstandard OS, Oracle applications, Windows Server applications such as MS SharePoint and MS Exchange, you need to obtain a license from the vendors. You can bring your existing license to the cloud through specific vendor programs such as Microsoft License Mobility through Software Assurance Program.

`How AWS Pricing Works <https://d0.awsstatic.com/whitepapers/aws_pricing_overview.pdf>`_

`AWS Free Tier <https://aws.amazon.com/free/>`_

Reserved Instances
==================

`Introduction to Amazon EC2 Reserved Instances <https://www.youtube.com/watch?time_continue=1&v=XrmdkRQZhUQ&feature=emb_logo>`_

`Amazon EC2 Reserved Instances and Other Reservation Models <https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/introduction.html>`_

Using Reserved Instances can have a significant impact on savings compared to on-demand, in some cases up to 75%. Typically, Reserved Instances are used for workloads that need to run most or all of the time, such as production environments. The commitment level could be 1 year or 3 years. AWS services offering RIs are: Amazon EC2, ECS, RDS, DynamoDB, Redshift, ElastiCache, Reserved Transcode Slots and Reserved Queues (AWS Elemental MediaConvert). It offers payment flexibility with 3 upfront payment options (all, partial, none). RI types are Standard, Convertible and Scheduled.

While using RIs, in certain cases, customers can take advantage of regional benefits. Regional benefits can simplify reserved instance optimization by allowing a reserved instance to be applied for the whole AWS Region, rather than just a specific Availability Zone, which can simplify capacity planning.

.. figure:: /compute_d/regional.png
	:align: center

	Regional RIs simplify optimization

AWS Cost Explorer generates RI recommendations for AWS services including Amazon EC2, RDS, ElastiCache and Elasticsearch. You can use the *Recommendations* feature to perform "what-if" scenarios comparing costs and savings related to different RI types (standard versus convertible RIs), and RIs term lengths (1 versus 3 years).

Customers can combine regional RIs with on-demand capacity reservations to benefit from billing discounts. On-demand capacity reservations means:

* Reserving capacity for Amazon EC2 instances in a specific Availability Zone for any duration. This ensures access to EC2 capacity when needed, for as long as needed.

* Capacity reservations can be created at any time, without entering into a 1-year or 3-year term commitment, and the capacity is available immediately.

* Capacity reservations can be cancelled at anytime to stop incurring charges.

Capacity reservation is charged the equivalent on-demand rate, regardless of whether the instances are run. Customers can combine regional RIs with capacity reservatins to get billing discounts. If customers do not use a reservation, it is shown as an unused reservation on the customer's EC2 bill.

Zonal RI billing discounts do not apply to capacity reservations. Capacity reservations can't be created in placement groups. Capacity reservations can't be used with dedicated hosts.

Convertible RIs give customers the ability to modify reservations across families, sizes, operating system, and tenancy. The only aspect customer cannot modify is the Region. So, as long as the customer stays in the same Region, they can continue to modify the RIs. Convertibles give customers the opportunity to maximize flexibility and increase savings.

The only time customers cannot convert RIs is between the time the request to exchange is submitted and the time the request to exchange is fulfilled. Typically requests take only a matter of hours to fulfill but could take a up to 2 days.

.. figure:: /compute_d/convertible.png
	:align: center

	Standard and convertible RI payments

Some guidelines for exchanging convertible RIs are the following:

* Customers can exchange to the same value or higher of convertible RIs.

* Converted RIs retain the expiration data of the original RIs.

* Converted RIs have the same term as the original RIs.

* When exchanging a group of convertible RIs:

  * Converted RIs have the latest expiration data of the whole group.

  * In the case of multiple terms, converted RIs will be a 3-year RIs.

For complete set of conversion rules, see `Exchanging Convertible Reserved Instances <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-convertible-exchange.html>`_.

Scheduled RIs are reserved for specific times like for a few hours every weekend.

Spot Instances
==============

Spot is spare, on-demand capacity that is available for discounts of up to 90% off On-Demand prices. Some of the differences with Spot compared to Reserved Instances and On-Demand Instances is the deep discount, no commitment requirement, and customers can pay for Linux instances by the second and Windows instances by the hour. One last key difference with Sot is spare, on-demand capacity. If AWS has a spike in requests in the on-demand space, AWS reclaims Spot instances with a 2-minute notification. The best workloads for Spot instances are fault-tolerant, flexible, and stateless. With Amazon EC2 instances, there are 3 simple rules to remember:

1. **Spot infrastructure**, or Spot Instances, are the exact same instances that customers would purchase with on-demand and RIs. The only difference in terms of the price points and the fact that it can be reclaimed by AWS. But otherwise, it functions the exact same way as on-demand instances.

2. **Spot pricing** is set based on long-term trends and supply and demand. This is typically an average discount of 70-90% off the on-demand price point. AWS eliminated the bidding model in 2017 in order to simplify the access model for customers and not require them to worry about pricing strategy anymore. This change has made things much simpler for the customer. To get Spot instances, customers simply request them, and if they're available, they will pay the current market rate, and they will hold on to them unless AWS needs to reclaim them for capacity reasons. There is no need to stress over situations where other customers can reclaim them because they were willing to bid or pay more for the instances. The price point is a lot smoother, so customers no longer have lots of fluctuation throughout the day. Prices can fluctuate slowly over time, but customers can take a look at the 90-day price history API and see that the price points are vey stable and much more predictable.

3. For customers to **diversify** their instance fleet, is especially important when it comes to overall Spot capacity availability. Diversifying is having the flexibility to use multiple instance types and Availability Zones for their workloads. The importance of flexibility is that Spot is spare on-demand capacity; so there may be times when there is a pike in demand, for particular instance type, and those instances may become unavailable on Spot. But if the customer has flexibility an have specified additional capacity pools, then it just increases the total pool of available Spot capacity that is available for their requests. This increases the likelihood that the requested capacity will be fulfilled. If there is spike in demand for a particular instance, and AWS has to reclaim some of those instances, it minimizes the overall impact of losing some of those instances.

Interruptions are important to understand when it comes to Spot, because Spot is an interruptible product. Over 95% of the instances were not interrupted in the last 3 months. The workloads on Spot should be stateless, fault tolerant, loose coupled and flexible. Any application that can have part or all the work paused and resumed or restarted can use Spot. Anything containerized is generally a good target workload for Spot. But more specifically, other areas where there is a lot of adoption is big data analysis, CI/CD, web services, and HPC.

What happens when AWS needs to reclaim an instance is that they will give you a 2-minute warning, either through a CloudWatch event, or customers can pull the metadata on the local instance and then they will have 2 minutes to take action and gracefully move off of the instance. There are different strategies that can be taken, for instance:

* Implementing a check-pointing strategy so that if an instance is interrupted, customers won't have to start the job over from scratch.

* AWS can provide example scripts triggering a Lambda function when the CloudWatch event is received, to automatically bring the workload up on another instance in their fleet. You can see `AWS Instance Scheduler <https://aws.amazon.com/solutions/instance-scheduler/>`_ for more information.

* AWS also has capabiities called stop-start and hibernate. Stop-start means customers would be able to persist an EBS volume if an instance is interrupted and when that instances becomes available again, it will re-attach to that EBS volume and continue on with the work where the customer left off. Hibernate takes that a step further and allows customers to flush in-state memory to disk.

* Spot blocks, which allows you reserve spot instances up to 6 hours in the spot market.

In 2018, AWS announced the integration of EC2 fleet with EC2 Auto Scaling. This means customers can now launch a single auto scaling group. This includes a mix of all the Spot instances that will work for customers across all of these, plus teir on-demand instances and RIs in a single auto scaling group. Customers can set different target capacities for what their requirements are and it will scale amongst that.

With the integration of EC2 fleet, customers also get all the benefits of fleet, such as being able to automatically replace a Spot instance, if it is interrupted, with another instance in the fleet, or taking advantage of different strategies within the fleet, such as launching in the cheapest capacity pools or diversifying across all the Spot instances that they have specified.

The integration of EC2 Auto Scaling and EC2 fleet helps customers to drive down costs, optimize performance, and eliminate operational overhead.

Amazon EC2 Spot instances integrate natively with a number of other AWS services, such as: AWS Batch, Data Pipeline and CloudFormation, Amazon EMR, ECS and EKS.

`Spot Instance Advisor <https://aws.amazon.com/ec2/spot/instance-advisor/>`_

`Amazon EC2 Spot Instances Pricing <https://aws.amazon.com/ec2/spot/pricing/>`_ 

`Amazon EC2 Spot Instances workshops website <https://ec2spotworkshops.com/>`_

`New -? Hibernate Your EC2 Instances <https://aws.amazon.com/es/blogs/aws/new-hibernate-your-ec2-instances/>`_

`AWS ANZ Webinar Series - Spot Instances: Benefits and Best Practices Explained <https://www.youtube.com/watch?v=PKvss-RgSjI&feature=emb_title>`_

Amazon EC2 fleet
================

Amazon EC2 Fleet is a new feature that simplifies the provisioning of Amazon EC2 capacity across different Amazon EC2 instance types, Availability Zones and across On-Demand, Amazon EC2 Reserved Instances (RI) and Amazon EC2 Spot purchase models. With a single API call, you can provision capacity across EC2 instance types and across purchase models to achieve desired scale, performance and cost.

It uses all 3 purchase options to optimize costs. It is integrated with Amazon EC2 Auto Scaling, Amazon ECS, Amazon EKS, and AWS Batch.


Amazon EC2 dedicated options
============================

`Amazon EC2 Dedicated Hosts <https://aws.amazon.com/ec2/dedicated-hosts/>`_

`Introducing AWS License Manager <https://aws.amazon.com/about-aws/whats-new/2018/11/announcing-aws-license-manager/>`_

`Changing the Tenancy of an Instance <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html#dedicated-change-tenancy>`_

AWS tagging strategies
======================

`AWS Tagging Strategies <https://aws.amazon.com/answers/account-management/aws-tagging-strategies/>`_

* **Cost Allocation Tags** only eases the organization of your resource costs on your cost allocation report, to make it easier for you to categorize and track your AWS costs.

`AWS re:Invent 2018: [REPEAT 1] Amazon EC2 Foundations (CMP208-R1) <https://www.youtube.com/watch?time_continue=1&v=vXBeO9vQAI8&feature=emb_logo>`_

Amazon EC2 considerations
*************************


`Instance Lifecycle <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html>`_


`Resource Locations <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resources.html>`_


For all new AWS accounts, 20 instances are allowed per region. However, you can increase this limit by requesting it via AWS support.

Instances within a VPC with a public address have that address released when it is stopped and are reassigned a new IP when restarted.

All EC2 instances in the default VPC have both a public and private IP address.


.. _secEBS:

Amazon EBS
**********

Overview
========

EBS is block storage as a service. With an API call, you create an EBS volume, which is a configurable amount of raw block storage with configurable performance characteristics. With another API call, you can attacj a volume to an EC2 instance when you need access to that data. Access to the volume os over the network. Once attached, you can create a file system on top of a volume, run a database on it, or use it in any other way you would use block storage. 

An EBS volume is not a single physical disk. It is a logical volume. EBS is a distributed system an each EBS volume is made up of multiple, physical devices. By distributing a volume across many devices EBS provides added performance and durability that you can't get from a single disk device.

EBS volumes are created in a specific AZ, and can then be attached to any instances in that same AZ. To make a volume available outside of the AZ, you can create a snapshot and restore that snapshot to a new volume anywhere in that region.

Data on an EBS volume persists independently from the life of an EC2 instance. As a result, you can detach your volume from one instance and attach it to another instance in the same AZ as the volume. If an EC2 instance fails, EBS storage persists independently from the EC2 instance. Because the system has failed, and has not been terminated by calling an PI, the volume is still available. In this case, you can re-attach the EBS volume to a new EC2 instance.

An EBS volume can be attached to only one instance at a time, but many volumes can attach to a single instance. For example, you might separate boot volume from application-specific data volumes.

EBS is designed to give a high level of volume availability and durability. Each volume is designed for five 9s of service availability. That's an average down time of about 5 minutes per year. For durability, the Annualized Failure Rate (AFR) is between 0.1% and 0.2%, nearly 20 times more reliable than a typical HDD at 4% AFR. To recover from a volume failure, you can use EBS to create snapshots of volumes, which are point-in-time copies of your data that is stored in S3 buckets. 

Block storage offerings
-----------------------

AWS addresses the block storage market in 3 categories to align with different customer workloads: 

* EC2 instance store provides SSD and HDD-based local instance store that targets high IOPS workloads that require low microsecond latency.

* EBS SSD storage offers General Purpose (gp2) and Provisioned IOPS (io1) volume types.

* EBS HDD storage offers Throughput Optimized (st1) and Cold HDD (sc1) volume types.

An instance store provides temporary block-level storage for your instance. This storage is located on disks that are physically attached to the host computer. Instance store is ideal for temporary storage of information that changes frequently, such as buffers, caches, scratch data, an other temporary content, or for data that is replicated across a fleet of instances, such as load-balanced pool of web servers.

An instance store consists of one or more instance store volumes exposed as block devices. The size of an instance store and the number of devices available varies by instance type. Although an instance store is dedicated to a particular instance, the disk subsystem is shared among instances on a host computer.

The EC2 instance and EBS have some similarities:

* Both are presented as block storage to EC2.

* Both are available as either SSD or HDD, depending on the EC2 instance type.

Their differences are:

* EC2 instance store is ephemeral. Data stored on the instance store does not persist beyond the life of the EC2 instance, consider it as being temporary storage.

* By default, data on EC2 instance store volumes is not replicated as a part of the EC2 service. However, you can set up replication yourself by setting up a RAID volume on the instance or replicating that data to another EC2 instance.

* Snapshots of an EC2 instance store volume are not supported, so you would have to implement your own mechanism to back up data stored on an instance store volume.

Use Cases
---------

**Relational Databases** such as Orable, Microsoft SQL Server, MySQL, and PostgreSQL are widely deployed on EBS.

EBS meets the diverse needs of reliable block storage to run **mission-critical applications** such as Oracle, SAP, Microsoft Exchange, and Microsoft SharePoint.

EBS enables your organization to be more agile and responsive to customer needs. Provision, duplicate, scale, or archive your **development, test, and production** environment with a few clicks.

EBS volumes provide the consistent and low-latency performance your application needs when running **NoSQL databases**.

**Business Continuity**. Minimize data loss and recovery time by regularly backing up your data and log files across different geographic regions. Copy AMIs and EBS snapshots to deploy applications in new AWS Regions.

`AWS re:Invent 2018: [REPEAT 1] Deep Dive on Amazon Elastic Block Storage (Amazon EBS) (STG310-R1) <https://www.youtube.com/watch?v=BuJa6Vl8cn8>`_

`Introduction to Amazon Elastic Block Store (EBS) <https://www.qwiklabs.com/focuses/370?parent=catalog>`_

`Amazon Elastic Block Store (Amazon EBS) <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html>`_

Types of Amazon EBS volumes
===========================

Comparison of EBS volume types
------------------------------

EBS provides the following volume types, which differ in performance characteristics and price, so that you can tailor your storage performance and cost to the needs of your applications. The volume types fall into 2 categories: Solid state drives and Hard disk drives.

Solid state drive, or SSD-backed volumes are optimized for transactional workloads that involve frequent read/write operations with small size and random I/O. For SSD-backed volumes, the dominant performance attribute is I/O operations per second, or IOPS. These volumes provide low latency.

Hard disk drive, or HDD-backed volumes are optimized for large streaming workloads where throughput (measured in MiB/s) is a better performance measure than IOPS. These volumes work best when the workload is sequential. For example, back up operations and writing SQL transaction log files. The more sequential a workload is, the less time spent in read operations. Therefore, the faster disk response leads to higher throughput rates.

There are 2 types of SSD-backed volumes: General Purpose (gp2) and Provisioned IOPS (io1). There are 2 types of HDD-backed volumes: Throughput Optimized (st1) and Cold HDD (sc1). This table describes and compares the 4 volume types.

.. figure:: /compute_d/ebs-types.png
   :align: center

	 Comparison of SSD and HDD volumes

The General Purpose SSD volume can handle most workloads, such as boot volumes, virtual machines, interactive applications, and development environments. The Provisiones IOPS SSD volume can handle critical business applications that require nearly continuous IOPS performance. This type of volume is used for large database workloads.

The Throughput Optimized HDD volume can handle streaming workloads that require consistent and fast throughput at a low price. For example, big data, data warehouses, and log processing. The Colod HDD volume can handle throughput-oriented storage for large amounts of data that are infrequently accessed. Use this type of volume for scenarios in which achieving the lowest storage cost is important.

`Amazon EBS features <https://aws.amazon.com/ebs/features/?nc1=h_ls>`_

`Amazon EBS Volume Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html>`_

Choosing an EBS volume type
---------------------------

How do you determine which volume type to use? Begin be asking: Which storage best aligns with the performance and cost requirements of my applications? Each has benefits and limitations that work with or against certain workloads. 

**What is more important IOPS or Throughput?**

* If IOPS is more important, **how many IOPS do you need?**

	* If the answer is more than 80000, choose an EC2 instance store. 

	* If you need 80000 or fewer, **what are your latency requirements?**

		* If your latency is in microseconds, the choice is an EC2 instance store. EC2 instance stores provide the lowest latency that you can achieve.

		* If your latency is in the single-digit millisecond category, decide **what's more important? Cost or performance?**

			* If cost is more important, choose General purpose (gp2).

			* If performance is the main driver for your workload, choose SSD volume type, Provisioned IOPS (io1). Compared to gp2, io1 provides more consistent latency (less jitter) and an order of magnitude more of IOPS consistency. 

* If Throughput is the defining characteristic of your workload, **Waht type of I/O do you have? Small, random I/O or large, sequential I/O?**

	* If you have small random I/O, re-evaluate the SSD categories.

	* If you have large sequential I/O, **what is your aggregate throughput?**

		* If you need more than 1750-MB/s throughput, consider D2 or H1 optimized instance types. D2 is dense storage instance type, which enables you to take advantage of the low cost, high disk throughput, and high sequential I/O access rates. D2 has up to 48 TB of local spinning hard disk, and it can do upwards of 3 GB/s of sequential throughput. H1 instances are storage-optimized instances, which are designed for applications that require low-cost, high-disk throughput, and high sequential disk I/O access to large datasets.

		* If your throughput requirement is less than 1750 MB/s, **Which is more important? Cost or performance?**

			* If it's performance, consider the HDD volume type throughput optimied HDD (st1). 

			* If the most important factor is cost, choose the Cold HDD (sc1) volume.

.. figure:: /compute_d/choosing.png
   :align: center

	 Choosing an EBS volume

When you are not sure what your workload is, choose General Purpose SSD (gp2) as it satisfies almost all workloads. However, this volume type works well for boot volumes, low-latency applications, and the bursty databases where the data transmission is interrupted at intervals.

EBS-Optimized instances
-----------------------

A non-EBS optimized instances has a shared network pipe. As a result, Amazon EBS traffic is on the same pipe as the network traffic to other EC2 instances, AWS services, such as Amazon S3, and the Internet. A shared network pipe is used because EBS storage is network-attaches storage and not attached directly to the EBS instance. The sharing of network traffic can caouse increased I/O latency to your EBS volumes.

EBS-optimized instances have dedicated network bandwidth for Amazon EBS i/O that is not shared. This optimization provides the best performance for your EBS volumes by minimizing contention between EBS i/O and other traffic from your instance. The size of an EBS-optimized instance, for example 2xlarge or 16xlarge, defines the amount of dedicated network bandwidth that is allocated yo your instance for the attached EBS volumes.

It is important to choose the right size EC2 that can support the bandwidth to your EBS volume. Choosing the right size helps you achieve the required IOPS and throughput.

EBS-optimized instances deliver dedicated bandwidth to EBS, with options between 425 Mbps and 14000 Mbps, depending on the instance type that you use. When attached to and EBS-optimized instance, General Purpose SSD (gp2) volumes are designed to deliver within 10% of their baseline and burst performance 99.9% of the time in a given year. Both Throughput Optimized HDD (st1) and Cold HDD (sc1) are designed for performance consistency of 90% of burst throughtput 99% of the time.

EBS-Optimized burst
-------------------

C5 instance types provide EBS-optimized burst. The C5 instance types can support maximum performance for 30 minutes at least once every 24 hours. For example, c5.large instances can deliver 275 MB/s for 30 minutes at least once every 24 hours. If you have a workload that requires sustained maximum performance for longer than 30 minutes, choose an instance type based on the baseline performancee listed for each C5 instance.

`Amazon EBS-?Optimized Instances <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html>`_

Managing Amazon EBS snapshots
=============================

An EBS snapshot is a point-in-time backup copy of an EBS volume that is stored in S3. S3 is a regional service that is not tied to a specific AZ. It is designed for 11 9s of durability, which is several orders of magnitude greater than the volume itself.

Snapshots are incremental backups, which means that only the blocks on the device that have changed after your most recent snapshot are saved. The incremental backups minimize the time required to create the snapshot and save on storage costs by not duplicating data. When you delete a snapshot, only the data that's unique to that snapshot is removed. Each snapshot contains all the information needed to restore your data (from the moment when the snapshot was taken) to a new EBS volume.

When you create an EBS volume from a snapshot, the new volume begins as an exact replica of the original volume that was used to create the snapshot. The replicated volume loads data lazily, that is, loads data when it's needed, in the background so that you can begin using it immediately.

How does a snapshot work?
-------------------------

When you execute the first snapshot, all blocks on the volume that have been modified (let's call them A,B,C) are marked as a snapshot copy to S3. Empty blocks are not part of the snapshot. The volume is useable again as soon as the CreateSnapshot API returns successfully, usually within a few seconds. You do not have to wait for the actual data transfer to complete before using the volume.

Snapshots are incremental backups so the second snapshot contains only new blocks or blocks that were modified since the first snapshot. For snapshot 2, block C has been modified to C1. A second snapshot is taken. Because the snapshot is incremental, C1 is the only block saved to the second snapshot. None of the data from the snapshot 1 is included in the new snapshot. Snapshot 2 contains only references to snapshot 1 for any unchanged data.

Before snapshot 3 is taken, two new blocks, D and E, are added, and the file system has deleted the file that contained block B. From a block perspective, block B was modified. Snapshot 3 contains any new or changed data since snapshot 2, but the new snapshot only references the blocks in snapshots 1 and 2 that are unchanged.

If you delete the first 2 snapshots, the deletion process is designed so that you retain only the most recent snapshot to restore the volume. The state of the original B block is now gone and A is still restorable from the latest snapshot even though it was not part of the original change set.

Active snapshots contain all the necessary information to restore the volume to the instant at which that snapshot was taken. When you create a new volume from a snapshot, data is lazily loaded in the background so that the volume is immediately available. You don't have to wait for all the data to be transferred to the new volume. If you access a piece of data that hasn't been loaded to the volume yet, that piece immediately moves to the front of the queue of data that flows from the snapshot data in S3 to your new volume.

Creating snapshots
------------------

1. You can use snapshots as an easy way to back up and share data on EBS volumes among multiple AZs within the same region. 

2. Another possible scenario is that you want to use snapshots in a different region or share with a different account. You can use copy-snapshot API operation, or the snapshot copy action from the AWS management console to copu snapshots to different regions. You can share sanpshots by modifying the permissions of the snapshot and granting different AWS accounts permission to use that snapshot. From that snapshot, others can create EBS volumes and get access to a copy of the snapshot data. The copy of snapshots to a different regions can be part of your disaster recovery strategy.

Amazon Data Lifecycle Manager (DLM)
-----------------------------------

When you must back up a large number of volumes or manage a large number of snapshots, you can use Amazon Data Lifecycle Manager (DLM). DLM automates the backup of EBS volumes and the retention of those backups for as long as needed. This feature uses policies to define backup schedules that specify when you want a snapshot to be taken and how often DLM creates the snapshots when you define the policies.

You also specify how many snapshots you want to retain, and Amazon DLM automatically manages the expiration of snapshots. This is an important feature if you need to retain snapshots for a certain period of time, or need to retain a certain number of snapshots for compliance and auditing reasons. Retention rules also help you to keep snapshot costs under control by removing snapshots that are no longer needed.

When you define a DLM policy, you specify volume tags to identify which EBS volumes should be backed up. This allows a single policy to be applied to multiple volumes. You can also use IAM to fully control access to DLM policies. There's no additional cost to using DLM. You pay only for the cost of the snapshots.

An example of DLM policy that satisfies the customer requirement: *All EC2 instance root volumes must be backed up once per day, and that backups should be retained for 7 days*. It is necessary to define a data lifecycle policy by specifying the EBS volume type to use. In this example, the tag name is *voltype* with a value of *root*. As we want to take one snapshot per day, so you specify to take a snapshot every 24 hours at 0700 UTC. Then, you retain the latest 7 snapshots.

DLM enables you to take snapshots every 12 hours or every 24 hours. If you need to take snapshots more often than this, you can use multiple tags on the same volume. For example, suppose that you want to create a snapshot every 8 hours and retain 7 days of snapshots. You add 3 tags to your volume for backup. The tag key-value pairs can be anything that makes sense for your organization. you then define 3 separate policies, one for each tag, running once per day for each policy. You stagger the start time so that it is offset by 8 hours from the other policies. 

Here are some considerations to take into account when using DLM for EBS snapshots:

* When specifying multiple tags in a policy, the policy applies to any of the tags specified. A snapshot is generated for each volume with a matching tag.

* You can use a volume tag in only one DLM policy. You cannot create a policy with a volume tag that has been already assigned to an existing policy.

* Snapshots are taken within one hour of the specified start time. The snapshot may not generally be taken exactly at the time specified in the policy.

* To improve the manageability of snapshots, DLM automatically applies AWS tags to each snapshot that is generates. Alternatively, you can specify custom tags to be applied to the snapshot.

Tagging EBS snapshots
---------------------

AWS supports tagging both EBS volumes and snapshots during creation. Tagging snapshots during creation is an atomic operation, that is, the snapshot must be created and the tags must be applied for the successful creation of snapshots. This functionality facilitates the proper tracking of snapshots from the moment that they are created. It also means that any IAM policies that apply to snapshots tags are enforced immediately.

You can add up to 50 tags to your snapshot when it's created. AWS provides resource-level permissions to control access to EBS snapshots through IAM policies. You can use tags to enforce tighter security policies. The ``CreateSnapshot``, ``DeleteSnapshot``, and ``ModifySnapshotAttribute`` are API operations that support IAM resource-level permissions.

The IAM policies give you precise control over access to resources. For example, you can require that a certain set of tags is applied when the snapshot is created, or you can restrict which IAM users can take snapshots on specific volumes. You can also control who can also control who can delete snapshots.

`Amazon EBS Snapshots <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html>`_ 

`Automating the Amazon EBS Snapshot Lifecycle <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html>`_

Managing Amazon EBS volumes
===========================

EBS volume management actions
-----------------------------

The actions that you can perform on a volume are the following:

* **Create**: New EBS volumes are created from large amounts of available space. They can have a size from 1 GiB to TiB.

* **Attach**: An EBS volume can be attached to an instance. After attachment, it becomes visible to the operating system as a regular block device. Each EBS volume can be a single EC2 instance at a time.

* **Create snapshot**. Snapshots can be created from a volume at any time while the volume is in the in-use state.

* **Detach**. When the operating system no longer uses the volume, it can be detached from the instance. Data remains stored on the EBS volume, and the volume remains available for attachment to any other instance within the same AZ.

* **Delete**. When the volume and its contents are no longer needed, the EBS can be deleted.

Creating a volume
-----------------

You can create an EBS volume and attach it to any EC2 instance within the same AZ. You can create an encrypted EBS volume, but you can attach an encrypted volume only to supported EC2 instance types. When a volume is created, its state is *available*. When the volume is attached to an instance, its state changes to *in-use*. 

To create an encrypted volume with the AWS Management console, you must select the *Encrypted* box, and choose the master key you want to use when encrypting the volume. You can choose the default master key for your account, or use AWS KMS to choose any customer master (CMK) that you have previously created. 

If you create the volume from a snapshot and do not specify a volume size, the default size is the snapshot size.

The states of a volume are Creating, Deleting, Available, and In-use. A volume in the *available* state can be attached to an EC2 instance. 

`Creating an Amazon EBS Volume <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html>`_

Attaching an EBS volume
-----------------------

To attach a volume to an EC2 instance, the volume must be in the *available* state. After the volume is attached, you must connect to the EC2 instance and make the volume available. You can view the attachment information on the volume's Description tab in the console. The information provides an instance ID and an instance device, which are required to make the volume available on its EC2 instance. 

To attach an EBS volume to a running or stopped instance, use the ``attach-volume`` command. After you attach an EBS volume to your instance, it is exposed as a block device. You can format the volume with any file system and then mount it. After you make the EBS volume available for use, you can access it in the same ways that you access any other volume. Any data written to this file system is written to the EBS volume and is transparent to applications that use the device.

After connecting to an EC2 instance, the steps to make the volume available for use in Linux are the following:

1. List volumes.

.. code-block:: console

	$ lsblk
	NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
	xvda    202:0    0    8G  0 disk
	-xvda1  202:1    0    8G  0 part /
	xvdf    202:80   0   10G  0 disk	

2. Check that there is no file system on the device.

.. code-block:: console

	$ sudo file -s /dev/svdf
	/dev/svdf: data

3. Create and ext4 (a journaling file system that the Linux kernel commonly uses) file system on the new volume.

.. code-block:: console

	$ sudo mkfs -t ext4 /dev/xvdf
	mke2fs 1.43.4 (31-Jan-2017)
	Creating filesystem with 261888 4k blocks and 65536 inodes
	Filesystem UUID: 15d8146f-bcb3-414c-864f-5100bb4b0bf8
	Superblock backups stored on blocks:
	        32768, 98304, 163840, 229376

	Allocating group tables: done
	Writing inode tables: done
	Creating journal (4096 blocks): done
	Writing superblocks and filesystem accounting information: done

4. Create a directory for mounting the new volume.

.. code-block:: console

	$ sudo mkdir /mnt/data-store

5. Mount the new volume.

.. code-block:: console

	$ sudo mount /dev/xvdf /mnt/data-store

6. Check that the volume is mounted.

.. code-block:: console

	$ df -hT
	Filesystem		Type    Size  Used Avail Use% Mounted on
	/dev/xvdf		ext4    197G   61M  187G   1% /data-store

`Making an Amazon EBS Volume Available for Use on Linux <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html>`_

`Making an Amazon EBS Volume Available for Use on Windows <https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-using-volumes.html>`_

Detaching an EBS volume
-----------------------

You can detach an EBS volume from an EC2 instance explicitly or by terminating the instance. If the instance is running, you must first unmount the volume from the instance. If an EBS volume is the root device of an instance, you must stop the EC2 instance before you can detach the volume.

The command to unmount the ``/dev/xvdf`` device on a Linux instance is

.. code-block:: console

	sudo umount -d /dev/xvdf

Deleting an EBS volume
----------------------

After volume deletion, the data is physically gone, and the volume cannot be attached to any instance. However, before deletion, it is good practicce to create a snapshot of the volume, which you can use to re-create the volume later if needed. To delete a volume, it must be in the available state (that is, not attached to an instance).

Modifying Amazon EBS volumes
============================

You can modify your volumes as the needs of your applications change. You can perform certain dynamic operations on existing volumes with no downtime or negative effects on performance:

* Increase capacity.

* Change the volume type.

* Increase or decrease provisioned IOPS.

You can easily right-size your deployment and adapt to performance changes. Use Amazon CloudWatch with AWS Lambda to automate volume changes to meet the changing needs of your applications, without establishing planning cycles to implement the changes.

In general, you must follow 3 major steps when modifying an EBS volume:

1. Use AWS Management console or the AWS CLI to issue ``modify`` volume command.

2. Use AWS Management console or the AWS CLI to monitor the progress of the modification.

3. If the size of the volume was modified, extend the volume's file system to take advantage of the increased storage capacity, by using OS commands for your EC2 instances.

`Amazon EBS Update – New Elastic Volumes Change Everything <https://aws.amazon.com/blogs/aws/amazon-ebs-update-new-elastic-volumes-change-everything/>`_

Modify a volume
---------------

You can modify volumes that are in the *in-use* state (attached to an EC2 instance) or the available state (not attaches to an EC2 instance). Minimum and maximum values for size depend on the volume type. For example, for a General Purpose SSD volume, the minimum size is 1 GiB, and the maximum size is 16384 GiB. Though the size of a volume can be changed, it can only be increased, not decreased.

You can change the IOPS value only for the Provisioned IOPS SSD volume type. This setting is the requested number of I/O operations per second that the volume can support. For provisioned IOPS volumes, you can provision up to 50 IOPS per GiB depending on what level of performance your applications require.

Monitor the progress
--------------------

During modifications, you can view the status of the volume in the AWS Management Console. An EBS volume that is being modified moves through a sequence of progress states: ``Modifying``, ``Optimizing``, and ``Complete``. You can resize your file system as soon as the volume enters the ``Optimizing`` state. Size changes usually take a few seconds to complete and take effect after a volume is in the ``Optimizing`` state. The ``Optimizing`` state requires the most time to complete.

Extend the file system
----------------------

To take advantage of the larger EBS volume, you must extend the file system on your local operating system. Use a file system-specific command to resize the file system to the larger size of the volume. These commands work even if the volume to extend is the root volume. For ext2, ext3, and ext4 file systems, the comand is ``resize2fs``.  XFS file systems, the command is ``xfs_growfs``. 

`Extending a Linux File System After Resizing a Volume <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html>`_

Securing Amazon EBS
===================

Access to EBS volumes is integrated with AWS IAM. IAM enables access control to your EBS volumes and snapshots. For example, you can use an IAM policy to allow specified EC2 instances to attach and detach volumes. You can also encrypt data that is written to EBS volumes.

EBS encryption
--------------

Amazon EBS encryption offers a simple encryption solution for EBS volumes without the need for you to build maintain, and secure your own key management infrastructure. When you create an encrypted EBS volume and attach it to a supported instance type, the following types of data are encrypted:

* Data at rest inside the volume.

* All data moving between the volume and the instance.

* All snapshots that were created from the volume.

Encryption is supported by all EBS volume types (General Purpose SSD, Provisioned IOPS SSD, Throughput Optimized HDD, Cold HDD and Magnetic[standard]). You can expect the same IOPS performance on encrypted volumes as you would with unencrypted volumes, with only a minimal effect on latency.

You can access encrypted volumes the same way that you access unencrypted volumes. Encryption and decryption are handled transparently, and they require no additional action from the user, the EC2 instances, or the applications.

EBS encryption uses a customer master key (CMK) from the AWS KMS when creating encrypted volumes. The CMK is also used for any snapshots that are created from the volumes. The first time you create an encrypted volume in a region, a default CMK is created automatically. This key is used for EBS encryption unless you select a CMK that you created separately with AWS KMS.

Encrypting a new volume
-----------------------

If you are not using a snapshot to create a volume, you can choose whether to encrypt the volume. Use the default key or select your own custom key. Creating your own CMK gives you more flexibility, including the ability to create, rotate, and disable keys. By using your own CMK, it is easier to define access controls, and to audit the encryption keys that are used to protect your data.

It is a best practice to create your own master key. By creating your own master key, you gain flexibility over the key. For example, you can have one team of users control encryption and another team of users control decryption. You can have separate master keys per application, or per data classification level. You can:

* Define the key rotation policy.

* Enable AWS CloudTrail auditing.

* Control who can use the key.

* Control who can administer the key.

EBS encryption is integrated into the AWS KMS, and AWS KMS is integrated with the IAM console. You have to access IAM console in order to create a key. Configuration options include:

* Adding tags.

* Defining key administrative permissions.

* Defining key usage permissions.

As part of the process for launching a new EC2 instance, you can use custom keys to encrypt EBS volumes at launch time by using the EC2 console or by executing the ``run-instances`` command.

How EBS encryption works
------------------------

EBS applies a strategy called envelope encryption that uses a two-tier hierarchy of keys. The customer master key (CMK) is at the top of the hierarchy and encrypts and decrypts data keys that are used outside of AWS KMS to encrypt data. CMKs never leave the AWS KMS. 

Each newly created EBS volume is encrypted with a unique 256-bit data key. The CMK is called to wrap the data key with a second layer, or second tier, of encryption. EBS stores the encrypted data key with the volume metadata. Any snapshots created from this volume will also be encrypted with this data key.

When a volume is attached to an EC2 instance, the CMK unlocks the volume data key and stores it in the memory of the server that hosts your instance. When the data key is stored in memory, it can decrypt and encrypt data to and from the volume. If the volume is detached, the data key is purged from memory. The data key is never saved to disk. The data key is stored in memory because:

1. If one resource is compromised, exposure is limited. Only one data key is exposed (and not all volumes).

2. The encryption key is in the memory of the system doing the encryption, thus limiting any performance degradation. You are not required to bulk-load large amounts of EBS data over the network to encrypt it.

3. Small number of master keys are used to protect potentially a large number of data keys.

There is no direct way to encrypt an existing unencrypted volume, or to remove encryption from an encrypted volume. Similarly, you cannot remove encryption from an encrypted snapshot.

However, you can migrate data between encrypted and unencrypted volumes. You can also apply a new encryption status while copying a snapshot. While copying an unencrypted snapshot of an unencrypted volume, you an encrypt the copy. Volumes restored from this encrypted copy are also encrypted. 

While copying an encrypted snapshot of an encrypted volume, you can re-encrypt the copy bu using a different CMK. Volumes that are restored from the encrypted copy are accesible only by using the newly applied CMK.

Encrypted snapshots
-------------------

Snapshots that are created from encrypted volumes are automatically encrypted. Volumes that are created from encrypted snapshots are also automatically encrypted. EBS encryption is available only on certain EC2 instance types. You can attach both encrypted and unencrypted volumes to a supported instance type.

The first snapshot copy to another region is generally a full copy. Each subsequent snapshot copy is incremental (which makes the copy process faster), meaning that only the blocks in the snapshot that have changed since your last snapshot copy to the same destination are transferred.

Support for incremental snapshots is specific to a cross-region pair, where a previous complete snapshot copy of the source volume is already available in the destination region. For example, if you copy an unencrypted snapshot from the US East (Ohio) region to the US West (Oregon) region, the first snapshot copy of the volume is a full copy. Subsequent snapshot copies of the same volume transferred between the same regions are incremental.

Similarly, the first encrypted snapshot copied to another region is always a full copy, an each subsequent snapshot copy is incremental. Support for incremental snapshots is specific to a cross-region pair, whereby a previous complete snapshot copy o the source volume is already available in the destination region.

When you copy a snapshot, if the original snapshot was not encrypted, you can choose to encrypt the copy. However, changing the encryption status usually results in a full (not incremental) copy, which may incur greater data transfer an storage charges.

Suppose that an encrypted snapshot is shared with you. It is recommended that you create a copy of the shared snapshot using a different CMK that you control. This protects your access to the volume if the original CMK is compromised, or if the owner revokes the CMK for any reason. You can specify a CMK that is different from the original one, and the resulting copied snapshot uses the new CMK. However, using a custom EBS CMK during a copy operation always results in a full (not incremental) copy, which may incur increased data transfer and storage charges.

By modifying the permissions of the snapshot, you can share your unencrypted snapshots with others in the AWS community by selecting *Private* and providing a user's account number. When you share an unencrypted snapshot, you give another account permission to both copy the snapshot and create a volume from it.

You can share an encrypted snapshot with specific AWS accounts, but you cannot make it public. Be aware that sharing the snapshot provides other accounts access to all the data. For others to use the snapshot, you must also share the custome CMK key used to encrypt it. Users with access cna copy your snapshot an create their own EBS volumes based on your snapshot while your original snapshot remains unaffected. Cross-account permissions can be applied to a CMK either when it is created or later.

To create a copy of an encrypted EBS snapshot in another account, complete these 4 steps:

1. Share the custom key associated with the snapshots with the target account. You can do it from the IAM console:
  
  	1.1. Under *External Account*, click *Add and External account*.

  	1.2. Specify which external accounts can use this key to encrypt and decrypt data. Administrators of the specified accounts are responsible for managing the permissions that allow their IAM users and roles to use this key.

2. Share the encrypted EBS snapshot with the target account.

	2.1. Select the snapshot.

	2.2. From the actions menu, click *Modify Permissions*.

3. From the target account, locate the shared snapshot and create a copy of it.

	3.1. Select the shared snapshot.

	3.2. Expand the Actions menu.

	3.3. Click *Copy*. To select the master key:

		3.3.1. In the Destination Region box, select the target region.

		3.3.2. In the Description box, enter a description that is used to easily identify the snapshot.

		3.3.3. In the Master Key box, select your master key, and click *Copy*.

4. Verify your copy of the snapshot.

EBS performance and monitoring
==============================

Many factors can affect the peformance of EBS, including:

* The I/O characteristics of your applications.

* The type and configuration of your EC2 instances.

* The type and configuration of your volumes.

EBS performance tips
--------------------

These tips represent best practices for getting optimal performanace from your EBS volumes in various user scenarios:

* *Understand how performance is calculated*. Know which units of measure are involved in calculating the performance metrics. For example, kilobytes per second for bandwidth, input/output operations per second (IOPS) for throughput, milliseconds per operation for latency, etc.

* *Understand your workload*. Know the relationship between the maximum performance of your EBS volumes, the size and number of I/O operations, and the time for each action to complete.

* *Use EBS-optimized instances*. Network traffic can contend with traffic between your EC2 instance and your EBS volumes. On EBS-optimized instances, the two types of traffic are kept separate.

* *Certain factors can degrade HDD performance*. For example, when you create a snapshot of a Throughput Optimized HDD (st1) or Cold HDD (sc1) volume, performance can drop to the volume's baseline value while the snapshot is in progress. Also, driving more throughput than the instance can support can limit performances. Performance also degrades when you initialize volumes that are restored from a snapshot*. Your performance can also be affected if your application does not send enough I/O requests.

* *Be aware of performance behavior when initializing volumes from snapshots*. You can experience a significant increase in latency when you first access blocks of data on a new EBS volume that was restored from a snapshot. This behavior is a tradeoff since, in this case, EBS volumes were designed for availability over performance. You can avoid this effect on performance by accessing each block beore moving the volume into production.

* *Use a modern Linux kernel* with support for indirect descriptors. By using indirect descriptors, you can queue more buffers. Indirect descriptors support block devices by making sure that large requests do not exhaust the ring buffer and increase the queue depth. Linux kernel 3.11 and later includes support for indirect descriptors, as do nay current-generation EC2 instances.

* *Increase read-ahead for high-throughput, read heavy workloads on Throughput Optimized HDD and Cold HDD volumes*. Some read-heavy workloads access the block device through the operating system page cache. To achieve the maximum throughput, configure the read-ahead setting to 1 MiB.

.. Note:: Linux performance tuning.

	Some workloads are read-heavy and access he block device through the operating system page cache (for example, from a file system). In this case, to achieve the maximum throughput, the default buffer size for Amazon Linux AMI is 128 KB (256 sectors). AWS recommends that you configure the read-ahead setting to 1 MiB. Apply this per-block-device setting only to your HDD volumes. For example: ``sudo blockdev -setra 2048 /dev/xvdf``

Initializing EBS volumes
------------------------

New EBS volumes receive their maximum performance the moment that they are available and do not require *initialization* )formerly known as pre-warming). However, storage blocks or volumes that were restored from snapshots must be initialized before you can access the block. Initialization involves pulling down data from S3 and writing it to the EBS volume.

This preliminary action takes time and can cause a significan increase in the latency of an I/O operation the first time each block is accessed. For most applications, amortizing this cost over the lifetime of the volume is acceptable. Performance is restore after the data is accessed once.

You can avoid this performance degradation in a production environment by reading from all of the blocks on your volume before you use it; this process is called *initialization*. For a new volume created from a snapshot, read all the blocks that have data before using the volume.

Deciding when to use RAID
-------------------------

You can join multiple EBS volumes, in a redundant array of independent disks (RAID) 0 stripping configuration to use the available bandwidth for these instances. With RAID 0 striping of multiple volumes, IOPS is distributed among the volumes of a stripe. As a result, you gain faster I/O performance. RAID is a data storage virtualization technology that combines multiple physical disk drive components into a single logical unit for the purposes of data redundancy, performance improvement, or both. Use RAID 0 when:
 
* Your storage requirement is greater than 16 TB.

* Your throughput requirement is greater than 500 MB/s.

* Your IOPS requirement is greater than 32000 IOPS at 16 K.

Avoid RAID for redundancy because:

* Amazon EBS data is already replicated.

* RAID 1 cuts available EBS bandwidth in half.

* RAID 5 and 6 lose 20% to 30% of usable I/O to parity.

Monitoring performance using Amazon CloudWatch
----------------------------------------------

Amazon CloudWatch monitors in real time your AWS resources and the applications that you run. CloudWatch metrics are statistical data that you can use to view, analyze, and set alarms on the operational behavior of your volumes. Types of monitoring data that are available for your Amazon EBS volumes:

* Basic data is available automatically in 5-minute periods. Data for the root device volumes of EBS-backed instances is also provided.

* Detailed data is provided by Provisioned IOPS SSD volumes that automatically send one-minute metrics to CloudWatch.

.. figure:: /compute_d/metrics.png
   :align: center

	 Amazon EBS metrics

`Monitoring the Status of Your Volumes <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-volume-status.html>`_

A number of performance metrics are available for Amazon EBS. The CloudWatch window in the Amazon EC2 console shows some of the graphs that are created from various EBS metrics. For example:

* The *Write Bandwith* graph shows the sum of the *VolumeWriteBytes* metric per second. The *VolumeWriteBytes* metric measures the number of bytes that are written to the volume. 

* The *Write Throughput* graph shows the *VolumeWriteOps* metric. This metric measures the total number of write operations in a specified period of time. 

* The *Average Queue Length* graph shows the *VolumeQueueLength* metric. This metric measures the number of read and write operation requests waiting to be completed in a specified period of time.

* The *Average Write* graph uses the *VolumeWriteBytes* metric to measure the average size of each write operation during the specified period.

.. figure:: /compute_d/cloudwatch.png
   :align: center

	 EBS metrics graphs in EC2 console

You can retrieve data from CloudWatch by using either the CloudWatch API or the Amazon EC2 console. Use the ``get-metric-data`` API to retrieve as many as 100 different metrics in a single request and ``get-metric-statistics`` for getting statistics for the specified metric. The console uses the raw data that the CloudWatch API  return to display a series of graphs that represent the data. Data is reported to CloudWatch only when the volume is active. If the volume is not attached to an EC2 instance, no data is reported.

Tracking Amazon EBS usage and costs
===================================

EBS pricing model
-----------------

To estimate the cost of using EBS, you need to consider the following:

* **Volumes**. Volumes storage for all EBS volume types is charged by the amount you provision in GB per month, until you release the storage.

* Provisioned **IOPS** SSD volumes. The throughput amount billed in a month is based on the average provisioned throughput for the month. Your throughput is measured in MB/s-month, which are added up at the end of the month to generate your monthly charges.

* **Snapshots**. Snapshot storage is based on the amount of space your data consumes in S3. Because EBS does not save empty blocks, it is likely that the snapshot size is considerably less than your volume size. Copying EBS snapshots is charged based on the volume of data transferred across regions. For the first snapshot of a volume, EBS saves a full copy of your data to S3. For each incremental snapshot, only the changed part of your EBS volume is saved. After the snapshot is copied, standard EBS snapshot charges apply for storage in the destination region.

* Outbound **Data transfer** is tiered and inbound data is free.

Tracking costs using tags
-------------------------

Tagging is an important feature that enables you to better manage your AWS resources. Use tags to assign simple key-value pair to resources, like EC2 instances, EBS volumes, and EBS sanpshots. With tagging, you can logically group resources to help visualize, analyze, and manage resources. By activating user-defined tags for cost allocation, AWS makes the associated cost data for these tags available throughout the billing pipeline.

`Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_

You can activate tags as *cost allocation* tags in the Amazon S3 Billing dashboard. By activating cost allocation tags, you can generate reports on cost and usage, broken down by tag values, such as dev, test, or backup. The same dataset that is used to generate AWS Cost and Usage reports is visible in the Cost Explorer for additional visualization. In Cost Explorer, you can view patterns in how much you spend on EBS snapshots. Cost Explorer is enabled from the Billing and Cost Management console in the AWS Management Console.

Amazon EFS
**********

Overview
========

Amazon EFS has a simple web service interface that allows you to create and configure file systems quickly and easily. EFS manages all the file storage infrastructure for you which allows tou to avoid the complexity of deploying, patching, and maintaining complex file system deployments. EFS provides simple, scalable file storage for use with Amazon EC2.

EFS file systems store data and metadata across multiple AZs to prevent data loss from the failure of any single component. With EFS, storage capacity is elastic, growing and shrinking automatically as you add or remove files, so your applications have the storage they need, when they need it. Since capacity is elastics, there is no provisioning necessary and you will only be billed for the capacity used. 

Choose EFS as a solution for the following scenarios:

* Applications running on EC2 instances that require a file system. 

* On-premises file systems that require multi-host attachments.

* High throughput application requirements.

* Applications that require multiple AZs for HA and durability.

It is important to understand your file workload requirements to determine whether EFS is a proper fit for your storage needs.

Use cases
---------

Some common EFS use cases are:

* *Web serving*. The need for shared file storage for web-serving applications can be challenge when integrating backend applications. Typically, multiple web servers deliver a website's contant, with each web server needing access to the same set of files.

* *Big data analytics*. Big data requires storage that can handle large amounts of data while scaling, to keep up with growth, and providing the performance necessary to deliver data to analytics tools. Many analytics workloads interact with data by means of a file interface, rely on file semantics, such as file locks, and require the ability to write to portions of a file. EFS provies the scale and performance required for big data applications that require high throughput to compute nodes coupled with read-after-write consistency and low-latency file operations. EFS can provide storage for organizations taht have many users that need to access and share common datasets.

* *Media and entertainment*. Digital media and entertainment workflows access data by using nework file protocols, such as NFS. These workflows require flexible, consistent, and secure access to data from off-the-shelf, custom-built, and partner solutions.

* *Container storage*. Docker containers are ideal for building microservices because they're quick to provision, easily portable, and provide process isolation. A container that needs access to the original data each time it starts may require a shared file system that it can connect to regardless of which instance they're running on.

* *Database backups*. Backing up data by using existing mechanisms, software, and semantics can create a isolated recovery scenario with little locational flexibility for recovery. 

* *Content management*. You an use EFS to create a file system accesible to people across an organization and establish permissions for users and groups ata the file or directory level.

Customers are using EFS for *Home directories* and *software development tools*.

.. figure:: /compute_d/efsusage.png
   :align: center

   Amazon EFS usage

`Amazon Elastic File System - Scalable, Elastic, Cloud-Native File System for Linux <https://www.youtube.com/watch?v=AvgAozsfCrY&feature=emb_logo>`_

`AWS re:Invent 2018: [REPEAT 1] Deep Dive on Amazon Elastic File System (Amazon EFS) (STG301-R1) <https://www.youtube.com/watch?v=4FQvJ2q6_oA>`_

Amazon EFS architecture
=======================

There are 3 deployment models for NFS storage: On-premises NFS storage, Cloud-based NFS storage in a "do it yourself model", and Amazon EFS, which is a fully-managed NFS storage service.

An on-premises NFS storage system is designed asking the following questions: "How much storage you need today? How do I ensure that it is sized for the performance needs of my application? What is my expected data growth over the next year, three years, and five years? Do I need to design this system for HA?". In general, you might not have all the answers to these questions, which can have you speculating on the best approach.

You might also consider building your own NFS storage solution in the cloud through a combination of compute instances (EC2 instances), storage volumes (EBS volumes attached to EC2 instances), and NFS software. The total costs of an NFS setup become expensive to build and manage.

EFS architecture
----------------

When you choose Amazon EFS, you need to only create mount targets in each AZ where your EC2 instances reside to connect to the Amazon EFS share. Amazon EFS does all the heavy lifting by providing a common DNS namespace in a high durable, scalable, NFS system that your EC2 instances can connect to. EFS supports NFS versions 4.0 and 4.1, so the applications and tools that use this protocols work with EFS. Multiple EC2 instances can access an EFS file system at the same time, providing a common data source for workloads and applications running on more than one instance. EFS charges by gigabyte of data stored and no provisioning of storage is required.

.. Note:: Provisioned Throughput mode.

	Provisioned Throughput mode adds a second price dimension. You are charged for the amount of storage you use and the throughtput you provision.

.. figure:: /compute_d/efs.png
   :align: center

	 Amazon EFS architecture

EFS file system
^^^^^^^^^^^^^^^

The **EFS file system** is the primary resource for EFS where files and directories are stored. EFS provides strong data consistency and file-locking features, so using EFS is just like using any of the popular NFS file systems. EFS is based on aregional construct, so you create an EFS file system in your chosen supported region. For most regions, EFS limits the number of file systems that you can create per account to 125. 

When creating your file system, you can choose from 2 performance modes: General Purpose and Max I/O. **General Purpose** mode is recommended as the best choice for most workloads, and provides the lowest latency for file operations. Consider the **Max I/O** mode for data-heavy applications that scale out significantly over time.

You can choose from 2 throughput modes: Bursting and Provisioned. **Bursting** Throughput mode is recommended for most file systems. Use the **Provisioned** Throughtput mode for applications that require more throughput than allowed by Bursting Throughput.

After you have created your file system, it is instantly accessible from EC2 instances within your VPC and can be accessed by multiple instances simultaneously. Additionally, you can connect to EFS from your on-premises clients by using AWS Direct Connect. After you have mounted your EFS file system, you can control access by using Portable Operating System Interface (POSIX) permissions.

To help you easily identify or organize the multiple file systems you create, you can add tags to your file systems. These are key and value pairs that you create during or after your file system creation. You can create up to 50 tgas per file system. 

Mount target
^^^^^^^^^^^^

A **mount target** is the resource created to enable access to your EFS file system from an EC2 instance or on-premises clients. A single mount target exists in each AZ an is the only way in which you can access your EFS file system. A mount target is analogous to an NFS endpoint. A mount target allows resources that reside in a VPC to access the EFS file system. Mount targets are automatically created during the EFS file system creation process. The mount target has an IP address and a DNS name that you use to mount your EFS file system to your EC2 instances.

.. figure:: /compute_d/mount.png
   :align: center

	 Mount targets

The DNS name contains the file system ID and the AWS Region where the file system was created. By default, mount targets are designed to be highly available. You can also configure access to a mount target by using security groups.

Only one mount target is in each AZ, but if your AZ contains multiple subnets, you can choose which subnet ID to assign to your EFS file system, then mount your Ec2 instances. After this is done, you can create one mount target in each AZ. The mount target obtains an IP address from the subnet dynamically, or you can assign a static IP address. The subnet IP address of the mount target does not change.

EFS requirements
----------------

Before setting up your file system in EFS, you must take insto account certain requirements:

1. You can mount an EFS file system to instances in only one VPC at a time. As you design and configure your applications, remember to keep your instances, which need access to the same file system, in a single VPC.

2. Your EFS file system and your VPC must reside in the same region. Because EFS is available only in certain regions, consider the locations where your are deploying resources in AWS.

Accessing EFS file systems
--------------------------

You can access EFS file systems in 3 ways: from EC2 instances, from on-premises hosts that mount EFS file systems over AWS Direct Connect, and from hosts running in the VMware Cloud on AWS.

From on-premises hosts, you mount your file systems through mount targets as you would with EC2, but instead of using a DNS name, AWS recommends that you use an IP address in the mount command. If you choose to mount your file system on your on-premises server through AWS Direct Connect with a DNS name, you must integrate your DNS in your VPC with your on-premises DNS domains. Specifically, to forward the DNS requests for EFS mount targets to a DNS server in the VPC over the AWS Direct Connect connection, you must update your on-premises DNS server.

.. figure:: /compute_d/dx.png
   :align: center

	 Amazon EFS with AWS Direct Connect

Some of the common uses cases for using AWS Direct Connect are the migration of data, backup/disaster recovery, and bursting. Bursting is copying on-premises data to EFS, analyzing the data at high speed, and sending the data back to the on-premises servers.

Amazon EFS File Sync
--------------------

Amazon EFS File Sync copies existing on-premises or cloud file systems to an EFS file system. Data copy operations are 5 times faster than standard Linux copy tools, and you can set up and manage your copy job easily from the AWS Management Console.

`What Is Amazon Elastic File System? <https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html>`_

Amazon EFS File System Management
=================================

Setting up and managing a file system
-------------------------------------

With EFS, you can set up and manage your file system by using 3 distinct interfaces: the AWS Management Console, AWS CLI and AWS SDK. The process of creating an EFS file system from the AWS Management Console has the following steps:

1. Choose the region where you want to create your file system.

2. Choose a VPC that has EC2 instances that will connect to your new file system.

3. Choose the appropriate subnets for your EFS where your EC2 instances reside.

4. Assign a security group for your file system. If you have not created a security group, you can create it later.

5. Choose the performance moe for your cloud storage workloads. Choose the throughput mode for your file system.

6. You can enable encryption for your file system, if it is needed.

Mounting a file system
----------------------

After creating a file system, you can view details about it in the AWS Management Console, such as its file system ID, performance mode, and throughput mode. The instructions for mounting the file system on an EC2 instance provide steps for installing the EFS mount helper and the NFS client. Steps to mount the file system with either the NFS client or the EFS mount helper are also provided. Each mount command requires the file system ID as an argument.

To mount your EFS files systems, use the EFS mount helper included in the *amazon-efs-utils* package. It is an open-source collection of Amazon EFS tools and there's no additional cost to use them. This package includes a mount helper and tooling that make it easier to perform encryption of data in transit for EFS. A mount helper is a program that you use when you mount a specific type of file system. 

To mount a file system with the EFS mount helper, follow these steps:

1. For an Amazon Linux EC2 isntance, install the Amazon EFS utilities

.. code-block:: console

	sudo yum install -y amazon-efs-utils

By default, when using the EFS mount helper with Transport Layer Security (TLS), the mount helper enforces the use of the Online Certificate Status Protocol (OCSP) and certificate hostname checking.

2. Create a new directory on your EC2 instance for the mount point, such as ``efs``. 

.. code-block:: console

	sudo mkdir efs

3. To mount a file system whose ID is ``fs-4fad7b36``, without encryption using the EFS mount helper:

.. code-block:: console

  sudo mount -t efs fs-4fad7b36:/ efs

If you require encryption of data in transit, include the TLS mount option, as shown:

.. code-block:: console

  sudo mount -t efs -o tls fs-4fad7b36:/ efs

4. With your file system created, you can now mount your file system to your EC2 instances. However, before you can begin the mount process, you must install the NFS client onto the operating system of your EC2 instance and create a directory for the mount point.

.. code-block:: console

  sudo mount -t nfs4 -o nfsvers=4.1, rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 file-system-id.ef.aws-region.amazonaws.com:/ efs

Obtain the file system ID and AWS REgion from the EFS console. The ``nfsvers`` parameter sets the protocol version for NFS. In this case, it is NFS protocol 4.1. The ``rsize``and ``wsize`` parameters are the I/O parameters for read and write data block size. For EFS, the recommended initial size is 1 MB, which is represented in bytes. The next parameter is the mount type. ``Hard`` is the reccommended default value; although ``soft`` can be used with some additional considerations for ``timeo``. ``Timeo`` is the timeout setting, with 600 deciseconds (one-tenth of a second) as the recommended default value for EFS. If the timeout value is changed from the recommended 60 secondsm set it to a minimum of 15 seconds. The ``retrans=2`` parameter specifies that 2 minor timeouts will occur before a major timeout occurs.

Additionally, you can automatically mount your instance to your EFS file system upon startup. You cando this by using a script or configuring an ``fstab`` file when launching and starting your EC2 instance.

`Mounting from an Amazon EC2 Instance <https://docs.aws.amazon.com/fsx/latest/LustreGuide/mounting-ec2-instance.html>`_

`Mounting Your Amazon EFS File System Automatically <https://docs.aws.amazon.com/efs/latest/ug/mount-fs-auto-mount-onreboot.html>`_

`Mounting File Systems Without the EFS Mount Helper <https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-old.html>`_

`Using Microsoft Windows File Shares <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-file-shares.html>`_

Securing your data in Amazon EFS
================================

Security controls
-----------------

You can control network traffic to and from file system by using VPC security groups and network access control lists to secure network access to your mount targets. To manage file and directory access, use standard Linux directory and file-level permissions to secure access to your data like any other NFS share. To control administrative access to EFS, use AWS IAM to control who can create, change, and manage EFS file systems. If you require encryption, you an encrypt your data at rest in EFS by integrating with the AWS KMS. You can also encrypt data in transit by enabling TLS when you mount your file system.

Security groups
---------------

For EFS, you can configure up to 5 security groups per mount target. To obtain access to an NFS mount target in AWS, TCP port 2049 must be open for inbound traffic to the mount target and outbound traffic to clients must be connected to the EFS file system.

Amazon EFS POSIX permissions
----------------------------

Amazon EFS supports the standard permission model you use when working with local file systems in Linux or Windows. These permission settings enforce user and group rights at the file and directory level. In a Linux instance, you can use ``chmod`` and specify read (r), write (w), execute (x) permissions.

Integrating with AWS IAM
------------------------

Use IAM policies to control access to EFS. AWS IAM has 2 default policies for managin access: ``AmazonElasticFileSystemFullAccess`` and ``AmazonElasticFileSystemReadOnlyAccess``. These policies grant full administrative access and read-only access to EFS.

For scenarios in which you want to grant the ability to create new file systems but prohibit the deletion of files systems, create a custom IAM policy for those types of granular permissions. Additionally, you can allow or deny mount target creation and deletion, security group modification, and tag creation.

Encryption at rest
------------------

If your workload requires encrypting data at rest, EFS integrates with the AWS KMS to provide encryption key management. Choosing the encryption option when you are creating your file system encrypts all data and metadata in your file system. After you have chosen encryption and created the file system, you cannot change these settings.

If you have an existing EFS file system that contains data that you want to encrypt, you must copy that data to a new encrypted EFS file system. You can create encrypt file systems through the AWS Management console, AWS CLI and AWS SDK.

AWS KMS handles the encryption and decryption of files, which makes the process transparent. Data and metadata are encrypted before being written to a disk and decrypted before being accessed by a client. Additionally, because the encryption process is transparent, it does not affect an application's access to data or metadata, so modifications to your application are not required. 

The process of enabling encryption is simple: select the Enable encryption check box and choose your encryption master key. You must select the encryption option when creating the EFS file system.

Encrypting data in transit
--------------------------

You can encrypt data in transit for EFS file system by enabling TLS when you mount your file system by using the EFS mount helper. When encryption of data in transit is declared as a mount option for your EFS file system, the mount helper initializaes a client stunnel (ssl-tunnel) process. Stunel is an open source multipurpose network relay. The client stunnel process listens on a local port for inbound traffic, and the mount helper redirects NFS client traffic to this local port. The mount helper uses TLS version 1.2 to communicate with your file system.

`Data Encryption in EFS <https://docs.aws.amazon.com/efs/latest/ug/encryption.html>`_ 

Performance and optimization
============================

Amazon EFS is a distributed file system in that it is distributed across an unconstrained number of servers. This configuration enables EFS to avoid bottlenecks and constraints of traditional file servers. Additionally, this distributed design enables a high level of aggregate IOPS and throughput for your applications. Data is also distributed across AZs, which enables the high level of durability and availability that EFS provides. Mount targets are placed in each AZ, and data is distributed across AZs.

Performance modes
-----------------

The default general purpose mode, is suitable for most workloads, general purpose mode provides the lowest latency operations, but has a limit of 7000 operations per second. Mas I/O mode is suitable for workloads that require more than 7000 operations per second, but there are some tradeoff to consider. The increase in operations per second often results in higher latency times for file operations. If a change in performance mode is needed after creation, you must create a new file system, select the correct mode, and then copy your data to the new resource.

.. figure:: /compute_d/performance.png
   :align: center

   Amazon EFS performance modes

Throughput in relation to size
------------------------------

With EFS, the throughput performance you can achieve is directly related to the size of the file system. Throughput levels on EFS scale as a file system grows. Because file-based workloads are typically spiky, which drive high levels of throughput for short periods of time and low level of throughput the rest of the time, EFS is designed to burst to high throughtput levels when needed.

All file systems, regardless of size can burst to 100 MiB/s of throughput, and those over 1-TiB large can burst to 100 MiB/s per TiB of data stored in the file system. For example, a 3-TiB file system can burst 300 MiB per second of throughput. The portion of time a file system can burst is determined by its size, and the bursting model is designed so that typical file system workloads will be able to burst when needed.

EFS uses a credit system to determine when file systems can burst. Each file system earns credits over time ata a baseline rate that is determined by the size of the file system, and uses credits whenever it reads or writes data. If you find that you need more throughput than EFS is providing based on your data size, you can enable Provisioned Throughput mode to provide additional throughput to support your application requirements.

Throughput modes
----------------

The throughput mode of the file system helps determine the overall throughput a file system is able to achieve. You can select the throughput mode at any time (subject to daily limits). Changing the throughput mode is a non-disruptive operation and can be run while clients continuously access the file system. You can choose between 2 throughput modes: Bursting or Provisioned. 

**Bursting Throughput** is the default mode and is recommended for a majority of uses cases and workloads. Throughput scales as your file system grows, and you are billed for only the amount of data stored on the file system in GB-Month. Because file (based workloads are typically spiky-driving high levels of throughput for short periods of time and low level of throughput the rest of the time) using Bursting Throughtput mode allow for high throughput levels for a limited period of time. 

You can monitor and alert on your file system's burst credit balance by using the ``BurstCreditBalance`` file system metric in Amazon CloudWatch. File systems earn burst credits at the baseline throughput rate of 50 MiB/s per TiB of data stored and can accumulate burst credits up to the maximum size of 2.1 TiB per TiB of data stored. A newly created file systems begin with an initial credit balance of 2.1 TiB. As a result, larget file systems can accumulate and store more burst credits, which allows them to burst to longer periods.

**Provisioned Throughput** is available for applications that require a higher throughput to storage ratio thatn those allowed by the Bursting Throughput moe. In this mode, you can provision the file system's throughput independent of the amount of data stored in the file system. Provisioned Throughput allows you to optimize your file system's throughput performance to match your application's needs, and your application can drive up to the provisioned throughput continuously. 

When file systems are running in Provisioned Throughput mode, you are billed for the storage you use in GB-Month and for the throughput provisioned in MiB/s-Month. The storage charge for both Bursting and Provisioned Throughput modes includes throughput of the file system in the price storage.

You can increase Provisioned Throughput as often as you need. You can decrease Provisioned Throughput or switch throughput modes as long as it's been more then 24 hours since the last decrease or throughput mode change.

.. figure:: /compute_d/throughput.png
   :align: center

   Amazon EFS throughput modes

`Whitepaper: Choosing Between the Different Throughput & Performance Modes <https://aws.amazon.com/efs/choosing-your-performance-mode/>`_

`Amazon EFS Performance <https://docs.aws.amazon.com/efs/latest/ug/performance.html>`_

Maximizing Amazon EFS throughput
--------------------------------

Parallelizing file operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When looking at your workload, consider the type of Amazon EC2 instance that is connecting to your file system. Review the virtual CPU, memory, and the network performance capabilities before deciding on Amazon EFS. These attributes determine the performance level of applications that use EFS.

To achieve higher throughput levels, EFS takes advantage of parallelizing your operations owing to EFS' distributed architecture. Parallelization means using more instances and more threads per instance. If your application can use multiple threads to perform file operations, you can take advantage of parallelization to increase performance.

An effective use case could be a data migration or large file copy operation that use multiple threads to shorten the time frame of the data move.

I/O size - serial operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The I/O size impact throughput for EFS is when performing serialized operations. As the amount of data you are reading or writing in an operation increases, the throughput increases as well. This is because of the distributed storage design of Amazon EFS. 

This distributed architecture results in a small latency overhead for each file operation. As the result of this per-operation latency, overall throughput generally increases as the average I/O size increases because the overhead is amortized over a larger amount of data.

Testing your workloads and understanding how your application is reading or writing data help you determine which applications are eligible for high throuhput data transfers with EFS. 

Amazon EFS CloudWatch metrics
-----------------------------

Performance metrics are displayed for each file system created. CloudWatch captures the following metrics:

* ``BurstCreditBalance`` determines the number of burst credits you have available.

* ``ClientConnections`` displays the number of client connections to a file system. When using a standard clien, there is 1 connection per mounted EC2 instance.

* ``DataReadIOBytes`` is the number of bytes for each file system read operation.

* ``DataWriteIOBytes`` is the number of bytes for each file system write operation.

* ``MetaDataIOBytes`` is the number of bytes for each metadata operation.

* ``PercentIOLimit`` is an important metric to look at when using the General Purpose mode. This metric is available only on the General Purpose mode and helps you determine whether you are reaching the limits of this mode, and if you need to switch to the Max I/O mode.

* ``PermittedThroughput`` shows the amount of throughput the file system is allowed. For file systems in the Provisioned Throughput mode, this value is the same as the provisioned throughput. For the file systems in the Bursting Throughput mode, this value is a function of the file system size and ``BurstCreditBalance``.

* ``TotalIOBytes`` is the number of bytes for each file system operation, including data read, data write, and metadata operations.

The 2 most important metrics for CloudWatch monitoring are ``PercentIOLimit`` and ``BurstCreditBalance``. ``PercentIOLimit`` because you will use this metric for determining when to use the General Purpose mode or Max I/O mode. ``BurstCreditBalance`` because it can show you how youa are using the available burst credits you have and how often you are using burst capacity. File systems by nature are spiky and will most likely use some bursting, but if a performance issue surfaces, you must also determine how often you might be draining you burst credits.

Metric math enables you to query multiple CloudWatch metrics and use math expressions to create a new time series based on these metrics. You can visualize the resulting time series in the CloudWatch console and add them to dashboards.

`Monitoring EFS with Amazon CloudWatch <https://docs.aws.amazon.com/efs/latest/ug/monitoring-cloudwatch.html>`_

Best practices using Amazon EFS
-------------------------------

In summary, here are some key recommendations to consider when using Amazon EFS:

* Before moving your applications to EFS, set up test environments in AWS to understand how your applications behaves while using EFS. In your test environment, you can obtain data on performance levels, throughput levels, and latency before deciding on EFS. The General Purpose setting is suitable for the majority of most workloads and provides the lowest latency.

* Start testing with Bursting Throughput. It is the recommended throughput mode for most file systems.

* For optimal performance and to avoid a variety of known NFS client defects, work with a recent Linux kernel, version 4.0 or later.

* To mount your EFS file system on your EC2 instance, use the EFS mount helper. You can use NFS version 4.1 when creating your file system mount points to ensure optimum compatibility. EFS supports NFS versions 4.0 and 4.1 protocols when mounting your file systems on EC2 instances. However, NFS v4.1 provides better performance.

* Improve EFS performance by aggregating I/O operations, parallelizing, and managing burst credits. Check your burst credit earn/spend rate when testing to ensure a sufficient amount of storage.

* Where possible, leverage the use of multiple threads, EC2 instances, and directories. 

* Monitor EFS metrics with CloudWatch to maintain the reliability, availability, and performance of EFS.

Amazon EFS cost and billing
===========================

EFS pricing model
-----------------

Generally, Amazon EFS pricing varies by region. With EFS, you have 3 pricing dimensions:

* **Storage**: amount of file system storage you use per month.

* **Throughput**. In the default Bursting Throughput mode, no charges are incurred for bandwidth or requests, and you get a baseline rate of 50 KB/s per GB of throughput included with the price of storage. You can choose the Provisioned Throughput mode and provision the throughput of your file system independent of the amount of data stored and pay separately for storage and throughput. Like the default Bursting Throughput mode, the Provisioned Throughput mode also includes 50 KB/s per GB (or 1 MB/s per 20 GB) of throughput in the price of storage. You are billed only for the throughput provisiones above what you are provided based on data you have stored. When using the Provisioned Throughput mode, you pay for the throughput you provision per month. No minimum fee and no setup charges are incurred.

* **EFS File Sync**. You pay per-GB for data copied to EFS. You can use CloudWatch to track the amount of data synced with another file system, whether it's on the AWS Cloud or on premises. If your source file system is in AWS, you are billed at standard EC2 rates fpr the instance on which the EFS File Sync agent runs.

Amazon EFS versus DIY file storage
----------------------------------

EFS pricing is based on paying for what you use. If Provisioned Throughput mode is enabled, there are no minimum commitments or upfront fees, and you are charged per GB stored and throughput consumed. You are not required to provision storage in advance, and you do not incur additional charges or billing dimensions when using EFS. With do-it-yourself file storage configurations, you must consider many costs, such as EC2 instance costs, EBS volume costs, and Inter-Availability Zone transfer costs. 


`Amazon EFS now Supports Access Across Accounts and VPCs <https://aws.amazon.com/about-aws/whats-new/2018/11/amazon-efs-now-supports-access-across-accounts-and-vpcs/?nc1=h_ls>`_

`Mounting EFS File Systems from Another Account or VPC <https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-vpc-peering.html>`_




