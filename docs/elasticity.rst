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

`AWS re:Invent 2018: CloudWatch Logs Insights Customer Use Case <https://www.youtube.com/watch?time_continue=3&v=RnN1o4Zdego&feature=emb_logo>`_

`AWS re:Invent 2018: Augmenting Security & Improving Operational Health w/ AWS CloudTrail (SEC323) <https://www.youtube.com/watch?v=YWzmoDzzg4U&feature=emb_logo>`_

Auto Scaling
************

We can identify 3 types of autoscaling services:

* **Amazon EC2 Auto Scaling** helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. 

* **Application Auto Scaling** allows you to configure automatic scaling for the following resources:

	* Amazon ECS services

	* Spot Fleet requests

	* Amazon EMR clusters

	* AppStream 2.0 fleets

	* DynamoDB tables and global secondary indexes

	* Aurora replicas

	* Amazon SageMaker endpoint variants

	* Custom resources provided by your own applications or services. For more information, see the GitHub repository.

	* Amazon Comprehend document classification endpoints

	* Lambda function provisioned concurrency

* **AWS Auto Scaling** which allows you to scale a number of services at the same time and in a very simple fashion. For example, if you have an application that is using EC2 instances and DynamoDB tables, you can setup the automatic provisioning and scaling of all these resources from one single interface.

Amazon EC2 Auto Scaling
=======================

Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. Using Auto Scaling removes the guesswork of how many EC2 instances you need at a point in time to meet your workload requirements.

When you run your applications on EC2 instances, it is critical to monitoring the performance of your workload using Amazon CloudWatch (for example, CPU utilization). EC2 resources requirements can vary over time, with periods with more demand and others with less demand. Auto Scaling allows you adjust capacity as needed (i.e. Capacity Management) based on conditions that you define and it is especially powerful in environments with fluctuating performance requirements. It allows you to maintain performance and minimize costs. Auto Scaling really answers 2 critical questions:

1. How can I ensure that my workload has enough EC2 resources to meet fluctuating performance requirements?

2. How can I automate EC2 resource provisioning to occur on-demand?

It matches several reliability design principles: Scale horizontally, Stop guessing capacity and Manage change in automation. If Auto Scaling adds more instances, this is termed as *scaling out*. When Auto Scaling terminates instances, this is *scaling in*.

There are 3 components required for auto-scaling:

1. Create a **launch configuration** or **launch template** determines what will be launched by Auto Scaling, i.e. the EC2 instance characteristics you need to specify: AMI, instance type, security groups, SSH keys, AWS IAM instance profile and user data to apply to the instance.

2. Create a **Auto Scaling group**. It is a logical group of instances for your service and defines where the deployment takes place and some boundaries for the deployment. You define which VPC to deploy the instances, in which load balancer to interact with, and specify the boundaries for a group: the *minimum*, the *maximum*, ans the *desired* size of the Auto Scaling Group. If you set a minimum of 1, if the number of servers goes below 1, another instance will be launched. If you set a maximum of 4, you will never have more than 4 instances in your group. The desire capacity is the number of instances that should be running at any given time (for example 2). The Auto Scaling is going to launch instances or terminate instances in order to meet the desired capacity. You can select the health check type.

.. figure:: /elasticity_d/as-basic-diagram.png
   	:align: center

	Sample Auto Scaling group

3. Define a least one **Auto Scaling policy**, which specifies how and when to scale in or scale out, that is, to launch or terminate EC2 instances. 

Auto Scaling policies
---------------------

There 4 possible types of auto scaling policies: manual scaling, scheduled scaling, dynamic scaling, predictive scaling.

Manual Scaling
^^^^^^^^^^^^^^

At any time, you can change the size of an existing Auto Scaling group manually.

.. figure:: /elasticity_d/manual.png
   	:align: center

	Manual Scaling

Scheduled scaling
^^^^^^^^^^^^^^^^^

Scaling based on a schedule allows you to set your own scaling schedule for predictable load changes. For example, every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. You can plan your scaling actions based on the predictable traffic patterns of your web application. Scaling actions are performed automatically as a function of time and date. You can schedule recurring scaling events or individual events.

.. Note::

	For scaling based on predictable load changes, you can also use the predictive scaling feature of AWS Auto Scaling. 

Dynamic scaling
^^^^^^^^^^^^^^^

When you configure dynamic scaling, you must define how to scale in response to changing demand. You create conditions that define thresholds to trigger adding or removing instances. Condition-based policies make your Auto Scaling dynamic and able to meet fluctuating requirements. It is best practice to create at least one Auto Scaling policy to specify when to scale out and at least one policy to specify to scale in. You can attach one or more Auto Scaling policies to an Auto Scaling group. It supports the following types of scaling policies:

1. *Target tracking scaling*. Increase or decrease the current capacity of the group based on a target value for a specific metric. This is similar to the way that your thermostat maintains the temperature of your home – you select a temperature and the thermostat does the rest.

For example, you have a web application that currently runs on two instances and you want the CPU utilization of the Auto Scaling group to stay at around 50 percent when the load on the application changes. This gives you extra capacity to handle traffic spikes without maintaining an excessive amount of idle resources. You can configure your Auto Scaling group to scale automatically to meet this need.

.. figure:: /elasticity_d/dynamic.png
   	:align: center

	Dynamic Scaling with target tracking

One common configuration to have dynamic Auto Scaling is to create CloudWatch alarms based on performance information from your EC2 instances or a load balancer. When a performance threshold is breached, a CloudWatch alarm triggers an Auto Scaling event which either scales out or scales in EC2 instances in the environment. 

.. figure:: /elasticity_d/CloudWatchalarm.png
	:align: center

	Sample CloudWatch alarm

CloudWatch can monitor metrics such as CPU, network traffic and queue size. CloudWatch has a feature called CloudWatch Logs that allows you pick up logs from EC2 instances, AWS Lambdas or CloudTrail. You can store the logs in the CloudWatch logs. You can also convert logs into metrics by extracting metrics using patterns. CloudWatch provides default metric across many AWS services and resources. You can also define custom metrics for your applications.

2. *Step scaling*. Increase or decrease the current capacity of the group based on a set of scaling adjustments, known as step adjustments, that vary based on the size of the alarm breach.

.. figure:: /elasticity_d/step.png
   	:align: center

	Dynamic Scaling with step scaling

3. *Simple scaling*. Increase or decrease the current capacity of the group based on a single scaling adjustment.

If you are scaling based on a utilization metric that increases or decreases proportionally to the number of instances in an Auto Scaling group, we recommend that you use target tracking scaling policies. Otherwise, we recommend that you use step scaling policies.

For an advanced scaling configuration, your Auto Scaling group can have more than one scaling policy. For example, you can define one or more target tracking scaling policies, one or more step scaling policies, or both. This provides greater flexibility to cover multiple scenarios.

When there are multiple policies in force at the same time, there's a chance that each policy could instruct the Auto Scaling group to scale out (or in) at the same time. When these situations occur, Amazon EC2 Auto Scaling chooses the policy that provides the largest capacity for both scale out and scale in. 

The approach of giving precedence to the policy that provides the largest capacity applies even when the policies use different criteria for scaling in. For example, if one policy terminates three instances, another policy decreases the number of instances by 25 percent, and the group has eight instances at the time of scale in, Amazon EC2 Auto Scaling gives precedence to the policy that provides the largest number of instances for the group. This results in the Auto Scaling group terminating two instances (25 percent of 8 = 2). The intention is to prevent Amazon EC2 Auto Scaling from removing too many instances.

Predictive scaling
^^^^^^^^^^^^^^^^^^

Using data collected from your actual EC2 usage and further informed by billions of data points drawn from Amazon.com observations, we use well-trained Machine Learning models to predict your expected traffic (and EC2 usage) including daily and weekly patterns. The model needs at least one day's of historical data to start making predictions; it is re-evaluated every 24 hours to create a forecast for the next 48 hours.

It performs a regression analysis between load metric and scaling metric and schedules scaling actions for the next 2 days, hourly, and repeats this process every day.


Use case: Automate provisioning of instances
--------------------------------------------

One of the use cases of Auto Scaling is automating the provision of EC2 instances. When the instances come up, they need to have some software and applications installed. You have to approaches to achieve it:

* You can use AMIs with all required configuration and software for this purpose, this is called the **golden image**. This golden image can be specified in the launch template.

* You can define a **base AMI** and install code and configuration as needed through user data in the launch template, AWS CodeDeploy, AWS Systems Manager, or even with configuration tools such as Puppet, Chef, and Ansible.

.. code-block:: console
	:caption: Sample user data

	#!/bin/bash

	# Install updates
	sudo yum update -y;

	# Install AWS CodeDeploy agent
	cd /home/ec2-user;
	wget https://aws-codedeploy-us-east-1.s3.region-identifier.amazonaws.com/latest/install \ -o install &&
	chmod +x ./install &&
	sudo ./install auto && sudo service codedeploy-agent start;

Perform additional actions with lifecycle hooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another use case is when the EC2 instance comes up, you want to execute additional actions when the instance is in pending state or terminating state such as:

* Assign EC2 IP address or ENI on launch.

* Register new instances with DNS, external monitoring systems, firewalls.

* Load existing state from Amazon S3 or other system.

* Pull down log files before instance is terminated.

* Investigate issues with an instance before terminating it.

* Persist instance state to external system.

The EC2 instances in an Auto Scaling group have a path, or lifecycle, that differs from that of other EC2 instances. The lifecycle starts when the Auto Scaling group launches an instance and puts it into service. The lifecycle ends when you terminate the instance, or the Auto Scaling group takes the instance out of service and terminates it. The following illustration shows the transitions between instance states in the Amazon EC2 Auto Scaling lifecycle.

.. figure:: /elasticity_d/auto_scaling_lifecycle.png
	:align: center

	Auto Scaling Lifecycle

.. Note::
	You are billed for instances as soon as they are launched, including the time that they are not yet in service.

You can receive notification when state transitions happen. You can rely on notifications to react to changes that happened. It is available via Amazon SNS and Amazon CloudWatch Events.

Register instances behind load balancer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You have full integration with ELB allowing you to automatically register instances behind Application Load Balancer, Network Load Balancer, and Classic Load Balancer.

Use case: Reduce paging frequency
---------------------------------

Replace unhealthy instances
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the load balancer determines that an instance is unhealthy, it stops routing requests to that instance. The load balancer resumes routing requests to the instance when it has been restored to a healthy state. There are 3 ways of checking the status of your EC2 instances:

1. **Via the Auto Scaling group**. The default health checks for an Auto Scaling group are EC2 status checks only. If an instance state is different from ``running`` or system health check equals ``impaired``, the Auto Scaling group considers the instance unhealthy and replaces it. If you attached one or more load balancers or target groups to your Auto Scaling group, the group does not, by default, consider an instance unhealthy and replace it if it fails the load balancer health checks.

2. **Via the ELB health checks**. However, you can optionally configure the Auto Scaling group to use Elastic Load Balancing health checks. This ensures that the group can determine an instance's health based on additional tests provided by the load balancer. The load balancer periodically sends pings, attempts connections, or sends requests to test the EC2 instances. These tests are called health checks. Load balancer health checks fail if ELB health equals ``OutOfService``.

If you configure the Auto Scaling group to use Elastic Load Balancing health checks, it considers the instance unhealthy if it fails either the EC2 status checks or the load balancer health checks. If you attach multiple load balancers to an Auto Scaling group, all of them must report that the instance is healthy in order for it to consider the instance healthy. If one load balancer reports an instance as unhealthy, the Auto Scaling group replaces the instance, even if other load balancers report it as healthy.

3. **Via custom health checks**. You can manually mark instances as ``unhealthy``. You can integrate with external monitoring systems.

`Why did Auto Scaling Group terminate my healthy instance(s)? <https://www.youtube.com/watch?v=_ew-J3DQKZg&feature=emb_logo>`_

Balance capacity across AZs
^^^^^^^^^^^^^^^^^^^^^^^^^^

The nodes for your load balancer distribute requests from clients to registered targets. When cross-zone load balancing is enabled, each load balancer node distributes traffic across the registered targets in all enabled Availability Zones. When cross-zone load balancing is disabled, each load balancer node distributes traffic only across the registered targets in its Availability Zone. 

With Application Load Balancers, cross-zone load balancing is always enabled. With Network Load Balancers, cross-zone load balancing is disabled by default. When you create a Classic Load Balancer, the default for cross-zone load balancing depends on how you create the load balancer. With the API or CLI, cross-zone load balancing is disabled by default. With the AWS Management Console, the option to enable cross-zone load balancing is selected by default.

For example, suppose we have 6 EC2 instances across 2 AZs behind an Elastic Load Balancer. In this case, we will have 3 EC2 instances in each AZ. If one of the AZs goes down, then Auto Scaling is going to terminate the 3 EC2 instances that were in this AZ and launch 3 EC2 instances in the AZ that is alive. Whenever the failed AZ is restored, then Auto Scaling rebalance the number of EC2 instances and setting 3 EC2 instances in each AZ.

Use case: Use spot instances to reduce costs
--------------------------------------------

You can reduce costs, optimize performance and eliminate operational overhead by automatically scaling instances across instance families and purchasing models (spot, on-demand, and reserved instances) in a single Auto Scaling group. 

You can specify what percentage of your group capacity should be fulfilled by on-demand instances, and spot instances to optimize cost. Use a prioritized list for on-demand instance types to scale capacity during an urgent, unpredictable event to optimize performance.

`AWS re:Invent 2018: Capacity Management Made Easy with Amazon EC2 Auto Scaling (CMP377) <https://www.youtube.com/watch?v=PideBMIcwBQ&feature=emb_logo>`_

`Introduction to Amazon EC2 Auto Scaling <https://www.qwiklabs.com/focuses/7932?parent=catalog>`_


Scaling your databases
**********************