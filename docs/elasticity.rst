Elasticity, High Availability, and Monitoring
#############################################

Understanding the basics
************************

**Fault tolerance** refers to the ability of a system to remain operational even if some components of that system fail. It can be seen as the built-in redundancy of an application's components. The user does not suffer any impact from a fault, the SLA is met.

**High availability** is a concept regarding the entire system. It goes to ensure that:

* Systems are generally functioning and accessible, but it may perform in a degraded state.

* Downtime is minimized as much as possible.

* Minimal human intervention is required.

* Minimal upfront financial investment

A comparison of High Availability on premises versus AWS would be the following:

* Usually, *on premises* could be very expensive and only applied to mission-critical applications. 

* On *AWS* you have the options to expand availability and recoverability among whatever services you choose.

High Availability
=================

The HA service tools are the following:

* **Elastic Load Balancers**. It distributes incoming traffic (loads) among your instances. It can send metrics to Amazon CloudWatch. ELB can be a trigger to notify high latency or if your services are becoming over-utilized. It can also be customize, for example you can configure it to recognize unhealthy EC2 instances. It can be public or internal-facing and it can use multiple different protocols.

* **Elastic IP addresses**. They are useful in providing greater fault tolerance for your application. They are static IP addresses designed for dynamic cloud computing. It allows you to mask a failure of an instance of software by allowing your users to utilize the same IP addresses with replacement resources. Your users continue to access applications even if an instance fails.

* **Amazon Route 53**. It is an authoritative DNS service that it used to translate domain names into IP addresses. It supports:

	* Simple routing

	* Latency-based routing

	* Health checks

	* DNS failovers

	* Geo-location routing

* **Auto Scaling** launches or terminates instances based on specific conditions. It is designed to assist you building a flexible system that can adjust or modify capacity depending on changes on customer demand. You can create new resources on demand or have scheduled provisioning. This is used to keep your applications and systems running no matter the load is.

* **Amazon CloudWatch** is a distributed statistics gathering system. It collects and tracks your metrics of your AWS infrastructure. You can create and use your own custom metrics. If there are metrics that surpasse a threshold CloudWatch in conjunction with Auto Scaling can scale automatically to ensure HA of your architecture.

Fault tolerance
===============

The fault tolerant service tools are the following:

* **Amazon Simple Queue Service (SQS)** which can be used as the backbone of your fault tolerant application. It is a highly reliable distributed messaging system. It helps you to ensure that the queue is always available.

* **Amazon Simple Storage Service (S3)** which provides highly durable and fault tolerant data storage. It stores the data redundantly across multiple different devices, across multiple facilities in a region.

* **Amazon Relational Database Service (RDS)** which is web service tool for you to set up, operate and scale relational databases. It provides HA and fault tolerance by offering several features to enhance the realibility on your critical databases. Some of these features include automatic backups, snapshots, and multi-AZ deployments.

Monitoring
**********

AWS Cost Explorer
=================

Cost Explorer helps you visualize and manage your AWS costs and usages over time. It offers a set of reports you can view data with for up to the last 13 months, forecast how much you're likely to spend for the next 3 months, and get recommendations for what Reserved Instances to purchase. You use Cost Explorer to identify areas that need further inquiry and see trends to understand your costs.

Amazon CloudWatch
=================

Amazon CloudWatch is a monitoring service that allows you to monitor your AWS resources and the applications you run on AWS in real time.

Some Amazon CloudWatch features include collecting and tracking metrics like CPU utilization, data transfer, as well as disk I/O and utilization. We can also monitor services for cloud resources and applications via collecting and monitoring log files. Additionally, you have the ability to set alarms on any of your metrics so that you can send notifications or take other automated actions.


`Collect Metrics and Logs from Amazon EC2 instances with the CloudWatch Agent <https://www.youtube.com/watch?time_continue=3&v=vAnIhIwE5hY&feature=emb_logo>`_

`AWS re:Invent 2018: Augmenting Security & Improving Operational Health w/ AWS CloudTrail (SEC323) <https://www.youtube.com/watch?v=YWzmoDzzg4U&feature=emb_logo>`_

Gaining elasticity and scaling your architecture
************************************************

Auto Scaling
============

Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. Using Auto Scaling removes the guesswork of how many EC2 instances you need at a point in time to meet your workload requirements.

When you run your applications on EC2 instances, it is critical to monitoring the performance of your workload using Amazon CloudWatch (for example, CPU utilization). EC2 resources requirements can vary over time, with periods with more demand and others with less demand. Auto Scaling allows you adjust capacity as needed (i.e. Capacity Management) based on conditions that you define and it is especially powerful in environments with fluctuating performance requirements. It allows you to maintain performance and minimize costs. Auto Scaling really answers 2 critical questions:

1. How can I ensure that my workload has enough EC2 resources to meet fluctuating performance requirements?

2. How can I automate EC2 resource provisioning to occur on-demand?

It matches several reliability design principles: Scale horizontally, Stop guessing capacity and Manage change in automation.

If Auto Scaling adds more instances, this is termed as *scaling out*. When Auto Scaling terminates instances, this is *scaling in*.

There are 3 components required for auto-scaling:

1. Create a **launch configuration**. This defines what will be launched by Auto Scaling, i.e. the EC2 instance characteristics you need to specify: AMI, instance type, security groups and roles to apply to the instance.

2. Create a **Auto Scaling group**. This defines where the deployment takes place and some boundaries for the deployment. You define which VPC to deploy the instances, in which load balancer to interact with, and specify the boundaries for a group: the minimum, the maximum, ans the desired size of the Auto Scaling Group. If you set a minimum of 2, if the number of servers goes below 2, another instance will be launched. If you set a maximum of 8, you will never have more than 8 instances in your group. The desire capacity is the number that you wich to start with. You can select the health check type.

3. Define a least one **Auto Scaling policy**, which specifies how much to scale in or scale out. This specifies when to launch or terminate EC2 instances. You can schedule Auto Scaling every Thrusday at 9:00 a.m. as an example, or create conditions that define thresholds to trigger adding or removing instances. Condition-based policies make your Auto Scaling dynamic and able to meet fluctuating requirements. It is best practice to create at least one Auto Scaling policy to specify when to scale out and at least one policy to specify to scale in. You can attach one or more Auto Scaling policies to an Auto Scaling group.

One common configuration to have dynamic Auto Scaling is to create CloudWatch alarms based on performance information from your EC2 instances or a load balancer. When a performance threshold is breached, a CloudWatch alarm triggers an Auto Scaling event which either scales out or scales in EC2 instances in the environment. 

.. figure:: /elasticity_d/alarm.png

	Sample CloudWatch alarm

CloudWatch can monitor metrics such as CPU, network traffic and queue size. CloudWatch has a feature called CloudWatch Logs that alllows you pick up logs from EC2 instances, AWS Lambdas or CloudTrail. You can store the logs in the CloudWatch logs. You can also convert logs into metrics by extracting metrics using patterns. CloudWatch provides default metric across many AWS services and resources. You can also define custom metrics for your applications.

`AWS re:Invent 2018: Capacity Management Made Easy with Amazon EC2 Auto Scaling (CMP377) <https://www.youtube.com/watch?v=PideBMIcwBQ&feature=emb_logo>`_

`Introduction to Amazon EC2 Auto Scaling <https://www.qwiklabs.com/focuses/7932?parent=catalog>`_

Scaling your databases
**********************