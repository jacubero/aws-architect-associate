Appendix
########

AWS Web Application Firewall (WAF)
**********************************

It helps protect web applications from common web exploits gat could affect application availability, compromise security, or consume excessive resources unexpectedly.

AWS WAF gives customers control over which traffic to allow or block to their web applications by defining customizable web security rules. Customers can use AWS WAF to create rules that block common attack patterns, such as SQL injection or cross-site scripting, as well as rules tailored to their specific application.

New rules can be deployed within minutes in response to changing traffic patterns. Also, AWS WAF includes a full-featured API that customers can use to automate the creation, deployment, and maintenance of web security rules. AWF integrates with services such as CloudFront and ELB, allowing customers to enforce security at the AWS edge, before traffic even reaches customer application infrastructure.

AWS Shield
**********

AWS Shield Standard
===================

AWS Shield is a managed DDoS protection service that safeguards applications running on AWS. There are 2 tiers of AWS Shield: Standard and Advanced.

.. figure:: /appendix_d/standard.png
   :align: center

	AWS Shield Standard

AWS Shield Standard protects applications running on AWS by providing always-on detection and automatic inline mitigations of DDoS attacks, to minimize application downtime and performance degradation. All AWS customers benefit from the automatic protections of AWS Shield Standard, at no additional charge. It defends against most common, frequently ocurring network and transport layer DDoS attacks that target web sites or applications. It integrates with Amazon CloudFront and Amazon Route 53, to provide comprehensive availability protection against many types of infrastructure attacks. 

A combination of traffic signatures, anaomaly alogorithms and other analysis techniques are employed to detect malicious traffic in real-time. Automated mitigation techniques are built into this service, applied inline to your applications so there is no latency impact. Several techniques, such as deterministic packet filtering and priority-based traffic shaping are used to automatically mitigate attacks without impacting your applications. You can mitigate application layer attacks by writing rules using AWS WAF, only paying for what you use. It is a self service and there is no need to engage AWS support to receive protection against DDoS attacks.

AWS Shield Advanced
===================

.. figure:: /appendix_d/advanced.png
   :align: center

	AWS Shield Advanced

Customers can also subscribe to AWS Shield Advanced. It provides additional detection and mitigation against large and sophisticated DDoS attacks. It provides near real-time visibility and integrates with AWS WAF. It gives customers 24x7 access to the AWS DDoS Response Team (DRT) and protection against DDoS-related spikes in their EC2, ELB, CloudFront and Route 53 charges. DRT can be engaged before, during, or after an attack. The DRT will triage incidents, identify root causes, and apply mitigations on your behalf. They can also assist you with post attack analysis. AWS Shield Advanced is available globally on Amazon CloudFront and Amazon Route 53 edge locations.

Using advaced routing techniques, this service tier provides additional capacity to protect against larger DDoS attacks. For application layer attacks, you can use AWS WAF to set up proactive rules like Rate-based Blacklisting to automatically stop bad traffic or respond immediately, all at no additional charge. You'll have complete visibility into DDoS attacks with near real-time notification through Amazon CloudWatch and detailed diagnostics on the management console. AWS Shield Advanced monitors application layer traffic to your Elastic IP addresses, ELB, CloudFront or Route 53 resources. It detects application layer attacks like HTTP floods or DNS query floods by baselining traffic on your resource and identifying anomalies. If any of these services scale up in response to a DDoS attack, AWS will provide service credits for charges due to usage spikes.

Protecting DNS
==============

AWS Shield Standard protects your Amazon Route 53 Hosted Zones from infrastructure layer DDoS attacks, including reflection attacks or SYN floods that frequently target DNS. A variety of techniques, such as header validationss and pritority-based traffic shaping, automatically mitigate these attacks.

AWS Shield Advanced provides greater protection, visibility into attacks on your Route 53 infrastructure, and help from AWS response team for extreme excenarios.

Protecting web applications and APIs
====================================

When using Amazon CloudFront, AWS Shield Standard provides comprehensive protection against infrastructure layer attacks like SYN floods, UDP floods, or other reflection attacks. Always-on detection and mitigation systems automatically scrub bad trafic at layer 3 and 4 to protect your application.

With AWS Shield Advanced the AWS response team actuvely applies any mitigations necessary for sophisticated infrastructure layer 3 or 4 attacks using traffic engineering. Application layer attacks, like HTTP floods, are also protected.

The always-on detection system baselines customers' steady-state application traffic and monitors for anomalies. Using AWS WAF, you can customize any application layer mitigation.

Protecting other applications
=============================

For other custom applications, not based on TCP (for example UDP and SIP), you cannot use services like Amazon CloudFront or ELB. In these cases, you often need to run your application directly on internet-facing EC2 instances.

AWS Shield Standard protects your EC2 instance from common infrastructure layer 3 or 4 attacks, such as UDP reflection attacks that include DNS, NTP, and SSDP reflection attacks. Techniques, such as priority-based traffic shaping, are automatically engaged when a well-defined DDoS attack signature is detected.

With AWS Shield Advanced on Elastic IP address, you have enhanced detection that automatically recognizes the type of AWS resource and size of EC2 instance and applies pre-defined mitigators. You can create custom mitigation profiles, and during the attack, all your Amazon VPC NACLs are automatically enforced at the border of the AWS network, giving you access to additional bandwidth and scrubbing capacity to mitigate large volumetric DDoS attacks. It also protects against SYN floods or other vectors, such as UDP floods.

Amazon Inspector
****************

Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. The service automatically assesses applications for vulnerabilities or deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed report with prioritized steps for remediation.

It is agent-based, API-driven, and delivered as a service. This makes it easy for you to build right into your existing DevOps process, decentralizing and automating vulnerability assessments, and empowering your DevOps teams to make security assessment an integral part of the deployment process.

AWS Config
**********

AWS Config is a service that enables customers to assess, audit, an evaluate the configurations of AWS resources. AWS Config continuously monitors and records AWS resource configurations and allows customers to automate the evaluation of recorded configurations against desired configurations and notify you if something is not compliant. 

With Config, customers can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine the overall compliance against the configurations specified in their internal or best-practices guidelines. This enables customers to simplify compliance auditing, security analysis, change management, and operational troubleshooting.

In addition, AWS Config can compare configuration changes against best-practices configuration rules, which are available from AWS. Any deviations can generate notification or automated remediation events that trigger actions using services like AWS Lambda. Config can also be used to track resource inventory of the environment.

When you set up AWS Config, you complete the following:

* Specify the resource types that you want AWS Config to record.

* Set up an S3 bucket to receive a configuration snapshot on request and configuration history.

* Set up an SNS topic to send configuration stream notifications.

* Grant AWS Config the permissions it needs to access S3 bucket and the SNS topic.

* Specify the rules that you want AWS Config to use to evaluate compliance information for the recorded resource types.

Amazon Simple Workflow Service (SWF)
************************************

Introduction
============

It is a managed workflow service that helps developers build, run, and scale applications that coordinate work across distributed components. You can of Amazon SWF as a fully managed state tracker and task coordinator for your background jobs that requires sequential and parallel steps. An application can consists of several different tasks to be performed and a certain sequence driven by a set of conditions. SWF makes it easy to architect and implement and coordinate these tasks in AWS cloud. 

When building solutions to coordinate tasks in a distributed environment, the developer has to account for several variables. Tasks that drive a processing steps can be long running and may fail, timeout or require a restart. They often complete with varying throughtputs and latencies. Tracking and visualization tasks in all these cases is not only challenging but also undifferentiated work. As applications and tasks scale up, you see different distributed system problems, for example: you must ensure that a task is assigned once and that the outcome is tracked reliably through unexpected failures and outages. 

By using Amazon SWF you can easily manage your application tasks and how to coordinate them.

.. figure:: /appendix_d/ecommerceSWF.png
   :align: center

	An e-commerce application workflow

The tasks in this workflow are sequential. An order must be verified before making a charge in the credit card. A credit card must be charged successfully before an order must be shipped. An order must be shipped before being recorded. Even so, because SWF supports distributed processes, these tasks can be carried out in different locations. If the tasks are programmatic in nature, they can also be written in different programming languages or using different tools.

In addition to sequential processing of tasks, SWF also supports workflow with parallel processing of tasks. Parallel tasks are performed at the same time and may be carried out independently by different applications or human workers. Your workflow makes decissions on how to proceed once one or more parallel tasks have been completed.

The benefits of SWF are:

* Logical separation. The service promotes the separation betwwen the control flow of your background jobs stepwise logic and the actual units of work that contains your unique business logic. This allows you to separately manage, maintain and scale state machinery of your application from the core business logic. As your business requirements change, you can easily change application logic without having to worry about your state machinery, tasks dispatch and flow control.

* Reliable. It runs on Amazon HA data centers so the state tracking and tasks processing engine is available whenever application need them. SWF redundantly stores tasks, realiably dispatches them to application components, track the progress and keeps the related state.

* Simple. It is simple to use and replaces the complexity of customed-coded solution and process automation software with a fully managed cloud web service. This eliminates the need for developers to manage infrastructure plumbing for the process automation so they can focus on the functionality of the application.

* Scale. SWF scales with your application usage. No manual administration of your workflow service is required as you add more workflows to your application or increase the complexity of your workflows.

* Flexible. It allows you write your application components and coordination logic in any programming language and run them in the cloud or on-premises.

Overview
========

Domain is a collection of related workflows. A workflow starter is any application that can initiate workflow executions. Workflows are collections of actions and actions are tasks or workflow steps. Decider implements the workflow coordination logic. Activity workers implements actions. Workflow history is the detailed, complete and consistent record of every event that occur since the workflow execution started. Additionally, in the course of its operations SWF interacts with a number of different types of programmatic actors. Actors can be workflow starters, deciders or activity workers. These actors communicate with SWF through its API. You can develop these actors in any programming language.

.. figure:: /appendix_d/swf-components.png
   :align: center

	SWF key components

Each workflow runs on an AWS resource called the **Domain**. Domains provide a way of scoping SWF resources within your AWS account. All the components of your workflow such as workflow types and activities types must be specified to be in a domain. It is possible to have more than a workflow in a domain. However, workflows in different domains can interact one with another. When setting up a new workflow, before you set up any of the other workflow components you have to register a domain if you have not done so. When you register a domain you have to specify a workflow history retention period. This period is the length of time SWF would continue to retain information about the workflow execution after the workflow execution is complete.

**Workflows** coordinate and manage the execution of activities that can be run asynchronously across multiple computing devices and that can feature both sequential and parallel processing. The workflow starter starts the workflow instance, also refered as the workflow execution, and can interact with an instance during execution for purposes such as pass additional data to the workflow worker or obtaining the current workflow state. The workflow starter uses a workflow client to start the workflow execution and interacts with the workflow as needed during execution and handles clean up. The workflow starter can be a locally run application, a web application, the AWS CLI or even the AWS management console. 

SWF interacts with activity workers and deciders by providing them with work assigments known as **tasks**. There are 3 types of tasks in Amazon SWF:

* *Activity task* tells an activity worker to perform its function, such as to check inventory or charge a credit card. The activity task contains all the information that the activity worker needs to perform its function. 

* *Lambda task* is similar to an activity task but executes the a Lambda function an set up a traditional SWF activity.

* *Decision task* tells the decider that the state of the workflow execution has changed, so that the decider can determine the next activity that needs to be performed. It contains to current workflow history. SWF schedule the decision task when the workflow starts and whenever the state of a workflow changes, such as when an activity task complete. 

Each decision task contains a paginated view of the entire workflow execution history. The decider analyzes the workflow execution history and responds back to SWF with a set of decisions that specify what should occur next in the workflow execution. Essentially, every decision task gives the decider an opportunity to assess the workflow and provides direction back to SWF. To ensure that no conflicting decisions are processed, SWF assigns each decision task to exactly one decider and allows one decision task at a time to be active in a workflow execution.

A **decider** is an implementation of a workflow coordination logic. Deciders control the flow of activity tasks in a workflow execution. Whenever a change occur in workflows executions, such as the completion of an activity task, SWF creates a decision task that contains the workflow history up to that point in time and assigns the task to a decider. When the decider receives the decision task from the SWF, it analyzes the workflow execution history to determine the next appropriate steps in the workflow execution. The decider communicates these steps back to SWF using decisions. A decision is a SWF data type that can represent next actions.

An **activity worker** is a process or thread that performs the activity tasks that are part of your workflow. The activity tasks represent one of the tasks that you identified in your application. Each activity worker pulls SWF for new tasks that is appropriate for that activity worker to perform and certain tasks can only be performed by certain activity workers. After receiving a task, the activity worker processes the tasks to completion and reports SWF that the task was completed and provides the result. The activity worker polls then for a new task. The activity worker is associated with a workflow execution continuing this way: processing tasks until the workflow execution itself is complete. Multiple activity workers can process tasks of the same activity type.

**Workflow history** is a detailed, complete, and consistent record of every event that occurred since the workflow execution started. An event represents a discete change in the workflow execution state, such as a new activity being scheduled or running activity being completed. The workflow history contains every event that causes the execution state of the workflow execution to change, such as scheduled completed activities, tasks timeouts and signals. Operations that don't change the state of the workflow execution don't typically appear in the workflow history. For example, the workflow history doesn't show pull attempts or the use of visibility operations. The Workflow history has a set of key benefits: 

* It enables applications to be stateless because all information about a workflow execution is stored in the Workflow history.

* For each worflow execution the Workflow history provides of what activities were scheduled, the current status, and the results. The workflow execution uses this information to determine the next steps. 

* The history provides the detailed auditrail that you can use to monitor running workflow executions and verify completed workflow executions.

The process that SWF follows is the following:

1. A workflow starter kick outs your workflow execution. For example, this can be a web server front end.

2. SWF receives the start workflow execution request and then scheduled a Decision task.

3. The decider receives the task from SWF, reviews the history and applies the coordination logic to determine the activity that needs to be performed.

4. SWF receives the decision, schedule the activity task and waits the activity task to complete or time out.

5. SWF assigns the activity to a worker that performs the tasks and returns the results to SWF. 

6. SWF receives the results of the activity, add them to the workflow history, and schedule the decision task.

7. This process repeats itself for each activity in your workflow.

.. figure:: /appendix_d/swf-process.png
   :align: center

	SWF process

Deciders and activity workers communicates with SWF using long polling. With this approach, the decider or activity worker periodically initiates communication with SWF notifying SWF of visibility to accept the task and then specify the tasks list to get tasks from. If the task is available in a specified task list, SWF returns it immediately in the response. If no task is available, SWF holds the TCP connection open up to 60 seconds, so that if a task becomes available during that time, it can be returned in the same connection. 

Use Cases
=========

In general, customers have used SWF to build applications for video encoding, social commerce, infrastructure provisioning, mapreduce pipelines, business process management, and several other use cases.

Cloud Migration
***************

.. figure:: /appendix_d/options.png
   :align: center

	Migration options

.. figure:: /appendix_d/tools.png
   :align: center
   
	Migration tools

Cloud Economics
***************

The cloud economics offering support AWS APN Partners in multiple areas, including **business value** and **cloud financial management**. For business value, the cloud value framework consists of 4 pillars:

1. Cost savings (typical focus)

2. Staff productivity 

3. Operational resilience

4. Business agility

The last 3 being the most compelling cloud benefits.

The cloud financial management offering is to make sure customers reap the cost benefits associated with running their workloads on AWS.

Cost savings
============

See section :ref:`secAWSpricing`

Staff productivity
==================

As enterprises move to AWS, a few common pattersn emerge ata the IT staff level. Tactical, undifferentiated work previously required for traditional data centers, like provisioning resources, moves from manual to automated. This saves staff time and reduces time to market. This allows customers' resurces to move to more strategic work.

As AWS maturity increases, customers learn how to further improve their businesses with AWS. They adopt new services and technologies, which can result in additional cost reductions and accelerated time to market.

.. figure:: /appendix_d/maturity.png
	:align: center

	AWS maturity versus activities

IT team members who used to work on projects like storage array deployments and server refreshes can transition to become DevOps specialists. By being integrated into the dev team, they can support the development of new products and services.

.. figure:: /appendix_d/server.png
	:align: center

	Server benefits

.. figure:: /appendix_d/network.png
	:align: center

	Network benefits

.. figure:: /appendix_d/storage.png
	:align: center

	Storage benefits

.. figure:: /appendix_d/application.png
	:align: center

	Application benefits

.. figure:: /appendix_d/facilities.png
	:align: center

	Facilities benefits

.. figure:: /appendix_d/securityben.png
	:align: center

	Security benefits

Operational resilience
======================

Operational resilient IT organizations depend on the health of 4 cornerstones: operations, security, software, and infrastructure.

Operations failures
-------------------

Some primary causes of operations failures are:

* Human errors, such as lack of clearly defined procedures or user privilege.

* Configuration errors in hardware or operating system settings and startup scripts.

* Procedural errors, like restoring the wrong backup or forgetting to restart a device.

* Commonplace accidents in the data center, like tripping over power cords, dropping equipment, or disconnecting devices.

AWS leverages automation; manages services from end to end; provides system-wide visbility for usage, performance, and operational metrics; enables security and governance configuration; and monitors API access.

Security: causes for breaches
-----------------------------

The causes for security breaches include:

* Malware, such as worms, viruses, and trojan horses.

* Network attacks, like open ports, SYN floods, and fragmented packets.

* Unpatched applications or operating systems.

* Security issues, such as password disclosures, social engineering, credentials not stored securely, non-strict password policies, and poor privilege and access management.

* Poor or limited authentication.

AWS has a `Shared Responsibility Model <https://aws.amazon.com/es/compliance/shared-responsibility-model/>`_, which means that AWS shares security responsibilities with customers. In this model, AWS is responsible for the security of everything from the hypervisor level to the operating system.

.. figure:: /appendix_d/shared.png
	:align: center

	AWS shared security model

AWS managed services move the line of responsibility higher.

AWS helps to reduce security risks in numerous ways:

* Leverages AWS automation and tools available to help customers mitigate the most severe security risks, including denial of service attacks.

* Provides the AWS Identity Access Management (IAM), service to centrally manage users and credentials, which helps customers reduce or eliminate the existence of "rogue servers".

* Leverages our roster of 30 plus compliance certifications and accreditations to help our customers build secure, compliance-ready environment.

Software: causes for failure
----------------------------

Common causes for software resilience failures include:

* Resource exhaustion, like runaway processes, memory leaks, and file growth.

* Computational or logic errors, such as faulty references, de-allocated memory, corrupt pointers, sync errors, and race conditions.

* Inadequate monitoring, such as the inability to identify issues.

* Failed upgrades, such as intercompatibility and integrations.

AWS provides services in a way that allows customers to increase or decrease the resources they need and have AWS manage the changes. To provide software resilence, AWS:

* Offer blue and green deployments that allow for quick rollbacks.

* Automates continuous integration and continuous delivery workflow.

* Runs smaller code deployments to reduce unit, integration, and system bugs.

* Provides current and secure resources with OS patching.

* Creates and manages a collection of related AWS resources.

Infrastructure: causes for failure
----------------------------------

Causes for infrastructure failure include:

* Hardware failure of servers, storage, or networks.

* Natural disaster, like hurricanes, floods, and earthquakes.

* Power outages, including failed power supplies and batteries.

* Volumetric attacks, such as DDoS, DNS amplification; or UDP/ICMP floods.

AWS helps reduce infrastructure failures in numerous ways:

* AWS continues to expand their world-class infrastructure and leads the industry in improving data centers on a massive scale.

* Customers can run applications and failover across multiple Availability Zones and Regions.

* AWS systems are designed to be highly available and durable. S3 is designed to provide eleven 9s of durability and four 9s of availability. Amazon Ec2 is designed for four 9s of availability, and Amazon EBS volumes are designed for five 9s of availability.

* As a standard, each AWS Availability Zone in each Region is redundantly connected to multiple tier-one transit providers.

* At AWS every compute instance is served by two independent power sources, each with utility, UPS, and back-up generator power.  

Business agility
================

Here, you can see a list of KPIs for measuring business agility:

.. image:: /appendix_d/kpis.png

Time to market for new applications
-----------------------------------

Some of the most important activities that a healthy business must do to continue to grow and innovate are to scope, prioritize, and take on new initiatives. You can think about the initiative process like a project funnel.

.. figure:: /appendix_d/funnel.png
	:align: center

	Innovate by increasing "fail fast" while reducing risks and costs

Code throughput and systems stability
-------------------------------------

DevOps practices help customers deliver software faster, more reliably, and with fewer errors. Two key DEvOps- related IT performance dimensions are code throughput and systems stability.

Lead time for changes and deployment frequency correspond to code throughput. Throughput is measured by how frequently a team is able to deploy code and how quickly it can move from committing code to deploying it.

Change failure rate and Mean Time to Recover (MTTR) correspond to systems stability. Stability is measured by how quickly a system can recover from downtime and how many changes succeed versus how many fail.

Cloud financial management
==========================

Cloud financial management includes four key areas.

.. image:: /appendix_d/financial.png

To enable cost transparency you must have the right tagging scheme and apply it to all areas of spending. User-defined tags allow customers to label their resources so they can manage them. At a minimum, from cost perspective, customers should use the following 5 tags:

* What cost center does it belong to? This may belong to more then one.

* What application or workload does it support?

* Who owns it?

* What is the expiration date? When should it be turned off? This helps with Reverved Instance purchasing.

* Automation tags can state directions such as "shut me down on the weekend" for and non-production environment, or "This instance runs non-critical workloads and can be freed up for disaster recovery in case of a mulfunction on a different Availability Zone."

An ideal tool for measuring and monitoring should provide:

* Cost and usage data.

* Optimization recommendations.

* Other information that helps teams make data-driven, cost-based decisions.

AWS Cost Explorer is a free tool that helps customers dive deeper into cost and usage data to indetify trends, pinpoint cost drivers, and detect anomalies.

AWs has identified 4 key pillars of cost optimization best practices:

Righ-sizing instances
---------------------

This means selecting the least expensive instance available that meets the functional and performance requirements. Right-sizing is the process of reviewing depoyed resources and seeking opportunities to downsize when possible. For example, if only CPU and RAM are underused, a customer can switch to a smaller size instance.

AWS Cost Explorer generates EC2 instance rightsizing recommendations by scanning your past usage over the previous 14 days. From there, AWS removes Spot Instance usage and any instances it believes that you terminated. AWS then analyzes the remaining instance uage to identify idle and underutilized instances:

* Idle instances are instances that have lower than 1% maximum CPU utilization.

* Underutilized instances are instances with maximum CPU utilization between 1% and 40%.

When AWS Cost Explorer identifies an idle instance, it will generate a termination recommendation. When it identifies an underutilized instance, AWS simulates covering that uasge with a smaller instance within the same family.

Increasing application elasticity
---------------------------------

Turn off non-production instances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In regards to increasing application elasticity for cost optimization, reviewing production versus non-production instances is key. Instances that are non-production, sucas dev, test, and QA, may not need to run during nonworking hours, such as nights and weekends. In these cases, these servers can be shut down, and will stop incurring charges if they are not Reserved Instances. Typically when a nonproduction instance has a usage percentage less than or equal to 36%, it is less expensive to use On-Demand pricing versus Reserved Instances.

A customer can create an AWS Lambda function that can automate the starting and stopping of instances based on parameters like idling and time of day:

`How do I stop and start Amazon EC2 instances at regular intervals using Lambda? <https://aws.amazon.com/es/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/>`_

Automatic scaling
^^^^^^^^^^^^^^^^^

Automatic scaling helps to ensure the correct number of instances are available to handle the workload of an application. Both the minimum and maximum number of instances can be specified, and automatic scaling ensures that you never go below or above the thresholds.

This provides the customer the opportunity to provision and pay for a baseline and then automatically scale for peak when demand spikes, which lowers costs with no performance impact.

Automatic scaling can be scheduled based on predefined times or performance. Recently, with the introduction of predective scaling for EC2, AWS will use  data collected from your actual EC2 usage and billions of data points drwan from AWS' own observations, in combination with well-trained machine learning models to predict expected traffic ( and EC2 usage) including daily and weekly patterns. The prediction process produces a scaling plan that can drive one or more groups of auto scaled EC2 instances. This allows you to automate the process of proactively scaling, ahead of daily and weekly peaks, improving overall user experience for your site or business, and avoid over-provisioning, which will reduce your EC2 costs. 

Choosing the right pricing model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See section :ref:`secEC2pricing`

Optimizing storage
^^^^^^^^^^^^^^^^^^

See section :ref:`secStorageClasses`

Resources for preparing the exam
********************************

`Practice questions <https://tutorialsdojo.com/aws-solutions-architect-associate-questions-with-explanations-part-1/>`_ 

`Solutions Architect Associate Bootcamp <https://github.com/parallax/reinvent-2018/blob/master/aws-sa-exam.md>`_