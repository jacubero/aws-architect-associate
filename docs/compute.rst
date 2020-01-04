Adding a compute layer
######################

.. _secEC2:

Adding Compute with Amazon EC2
******************************

Amazon EC2 allows to create and run virtual machines on AWS cloud. AWS calls these virtual machines *instances*. AWS provides various configurations of CPU, memory, storage, and networking capacity for your instances, known as *instance types*.

.. figure:: /compute_d/ec2.png
   :align: center

	 Amazon EC2

Launching Amazon EC2 instances with Amazon Machine Images (AMIs)
================================================================

`How do I create an Amazon Machine Image (AMI) from my EBS-backed EC2 instance? <https://www.youtube.com/watch?time_continue=5&v=vSKWBBrEbNQ&feature=emb_logo>`_

Launching Amazon EC2 instances with user data
=============================================


Amazon EC2 and storing data
===========================

Instance store
--------------

The data in an instance store persists only during the lifetime of its associated instance. If an instance reboots (intentionally or unintentionally), data in the instance store persists. However, data in the instance store is lost under any of the following circumstances:

* The underlying disk drive fails

* The instance stops

* The instance terminates

Amazon EBS
----------

`AWS re:Invent 2018: [REPEAT 1] Deep Dive on Amazon Elastic Block Storage (Amazon EBS) (STG310-R1) <https://www.youtube.com/watch?v=BuJa6Vl8cn8>`_

`Introduction to Amazon Elastic Block Store (EBS) <https://www.qwiklabs.com/focuses/370?parent=catalog>`_

Amazon EBS provides 3 volume types: General purpose (SSD), Provisioned IOPS (SSD) and Magnetic.

Cost factors
^^^^^^^^^^^^

To estimate the cost of using EBS, you need to consider the following:

* **Volumes**. Volumes storage for all EBS volume types is charged by the amount you provision in GB per month, until you release the storage.

* **IOPS**. I/O is included in the price of general purpose volumes. Magnetic volumes are charged by the number of requests you make to your volume. Provisioned IOPS volumes are charged by the amount you provision in IOPS, multiplied by the percentage of days you provision for the month.

* **Snapshot**. EBS provides the ability to back up snapshots of your data to S3 for durable recovery. If you opt for EBS snapshots, the added cost is per gigabyte-month of data stored.

* Outbound **Data transfer** is tiered and inbound data is free. 

Amazon EFS
----------

`Amazon Elastic File System - Scalable, Elastic, Cloud-Native File System for Linux <https://www.youtube.com/watch?v=AvgAozsfCrY&feature=emb_logo>`_

`AWS re:Invent 2018: [REPEAT 1] Deep Dive on Amazon Elastic File System (Amazon EFS) (STG301-R1) <https://www.youtube.com/watch?v=4FQvJ2q6_oA>`_


Amazon EC2 instance types
=========================

`Amazon EC2 instance types <https://aws.amazon.com/ec2/instance-types/>`_ 

Amazon EC2 families
-------------------

* **General Purpose**: A1, T3, T3a, T2, M6g, M5, M5a, M5n, M4.

* **Compute Optimized**: C5, C5n, C4.

* **Memory Optimized**: R5, R5a, R5n, R4, X1e, X1, High Memory, z1d.

* **Accelerated Computing**: P3, P2, Inf1, G4, G3, F1.

* **Storage Optimized** I3, I3en, D2, H1.

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

.. _secEC2pricing:

Amazon EC2 pricing options
**************************

AWS offers 3 core purchasing options: On-Demand, Reserved Instances, Spot Instances. Each purchasing model launches the same underlying EC2 instances.

Using **On-demand Instances** is often where customers begin their Amazon EC2 journey, because they need to define teir needs and support spikey workloads.

Then, once customers have identified what is steady state and what is predictable, **Reserved Instances** come into play. Reserved Instances are instances that require a 1 to 3-year commitment, and in exchange, customers get a significatn discount off of On-Demand prices. This is ideals for customers' committed and more predictable, steady state use.

**Spot instances** are the most inexpensive and flexible way to access Amazon EC2 instances. 

With all these pricing models, the key is striking a balance. Use RIs for predictable or always-on workloads, and On-Demand and Spot Instances for unpredictable workloads.

Reserved Instances
==================

`Introduction to Amazon EC2 Reserved Instances <https://www.youtube.com/watch?time_continue=1&v=XrmdkRQZhUQ&feature=emb_logo>`_

Using Reserved Instances can have a significant impact on savings compared to on-demand, in some cases up to 75%. Typically, Reserved Instances are used for workloads that need to run most or all of the time, such as production environments. The commitment level could be 1 year or 3 years. AWS services offering RIs are: Amazon EC2, ECS, RDS, DynamoDB, Redshift, ElastiCache, Reserved Transcode Slots and Reserved Queues (AWS Elemental MediaConvert). RI types are Standard, Convertible and Scheduled.

While using RIs, in certain cases, customers can take advantage of regional benefits. Regional benefits can simplify reserved instance optimization by allowing a reserved instance to be applied for the whole AWS Region, rather than just a specific Availability Zone, which can simplify capacity planning.

.. figure:: /intro_d/regional.png
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

.. figure:: /intro_d/convertible.png
	:align: center

	Standard and convertible RI payments

Some guidelines for exchanging convertible RIs are the following:

* Customers can exchange to the same value or higher of convertible RIs.

* Converted RIs retain the expiration data of the original RIs.

* Converted RIs have the same term as the original RIs.

* When exchanging a group of convertible RIs:

  * Converted RIs have the latest expiration data of the whole group.

  * In the case of multiple terns, converted RIs will be a 3-year RIs.

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

Amazon EC2 dedicated options
============================


AWS tagging strategies
======================

`AWS Tagging Strategies <https://aws.amazon.com/answers/account-management/aws-tagging-strategies/>`_

* **Cost Allocation Tags** only eases the organization of your resource costs on your cost allocation report, to make it easier for you to categorize and track your AWS costs.

Amazon EC2 considerations
*************************

The appropriate user names for connecting to a newly created Amazon EC2 instance are as follows:

* For an Amazon Linux AMI, the user name is ``ec2-user``.

* For a RHEL AMI, the user name is ``ec2-user`` or ``root``.

* For an Ubuntu AMI, the user name is ``ubuntu`` or ``root``.

* For a Centos AMI, the user name is ``centos``.

* For a Debian AMI, the user name is ``admin`` or ``root``.

* For a Fedora AMI, the user name is ``ec2-user``.

* For a SUSE AMI, the user name is ``ec2-user`` or ``root`.


`Instance Lifecycle <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html>`_


`Resource Locations <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resources.html>`_


Security groups operate at the instance level.

Security groups disallow all traffic unless there are specific allow rules for the traffic in the security group. They only provide for allow rules.

Security groups evaluate all the rules on the group before deciding how to handle traffic.

Changes to a security group take place immediately.

For all new AWS accounts, 20 instances are allowed per region. However, you can increase this limit by requesting it via AWS support.

Instances within a VPC with a public address have that address released when it is stopped and are reassigned a new IP when restarted.

All EC2 instances in the default VPC have both a public and private IP address.

`AWS re:Invent 2018: [REPEAT 1] Amazon EC2 Foundations (CMP208-R1) <https://www.youtube.com/watch?time_continue=1&v=vXBeO9vQAI8&feature=emb_logo>`_
