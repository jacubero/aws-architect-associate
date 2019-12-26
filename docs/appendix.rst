Appendix
########

AWS Web Application Firewall (WAF)
**********************************

It helps protect web applications from common web exploits gat could affect application availability, compromise security, or consume excessive resources unexpectedly.

AWS WAF gives customers control over which traffic to allow or block to their web applications by defining customizable web security rules. Customers can use AWS WAF to create rules that block common attack patterns, such as SQL injection or cross-site scripting, as well as rules tailored to their specific application.

New rules can be deployed within minutes in response to changing traffic patterns. Also, AWS WAF includes a full-featured API that customers can use to automate the creation, deployment, and maintenance of web security rules. AWF integrates with services such as CloudFront and ELB, allowing customers to enforce security at the AWS edge, before traffic even reaches customer application infrastructure.

AWS Shield
**********

AWS Shield is a managed DDoS protection service that safeguards applications running on AWS. There are 2 tiers of AWS Shield: Standard and Advanced.

.. figure:: /appendix_d/standard.png

	AWS Shield Standard

AWS Shield Standard protects applications running on AWS by providing always-on detection and automatic inline mitigations of DDoS attacks, to minimize application downtime and performance degradation. All AWS customers benefit from the automatic protections of AWS Shield Standard, at no additional charge. It defends against most common, frequently ocurring network and transport layer DDoS attacks that target web sites or applications. It integrates with Amazon CloudFront and Amazon Route 53, to provide comprehensive availability protection against many types of infrastructure attacks. 

A combination of traffic signatures, anaomaly alogorithms and other analysis techniques are employed to detect malicious traffic in real-time. Automated mitigation techniques are built into this service, applied inline to your applications so there is no latency impact. Several techniques, such as deterministic packet filtering and priority-based traffic shaping are used to automatically mitigate attacks without impacting your applications. You can mitigate application layer attacks by writing rules using AWS WAF, only paying for what you use. It is a self service and there is no need to engage AWS support to receive protection against DDoS attacks.

.. figure:: /appendix_d/advanced.png

	AWS Shield Advanced

Customers can also subscribe to AWS Shield Advanced. It provides additional detection and mitigation against large and sophisticated DDoS attacks. It provides near real-time visibility and integrates with AWS WAF. It gives customers 24x7 access to the AWS DDoS Response Team (DRT) and protection against DDoS-related spikes in their EC2, ELB, CloudFront and Route 53 charges. DRT can be engaged before, during, or after an attack. The DRT will triage incidents, identify root causes, and apply mitigations on your behalf. They can also assist you with post attack analysis. AWS Shield Advanced is available globally on Amazon CloudFront and Amazon Route 53 edge locations.

Using advaced routing techniques, this service tier provides additional capacity to protect against larger DDoS attacks. For application layer attacks, you can use AWS WAF to set up proactive rules like Rate-based Blacklisting to automatically stop bad traffic or respond immediately, all at no additional charge. You'll have complete visibility into DDoS attacks with near real-time notification through Amazon CloudWatch and detailed diagnostics on the management console. AWS Shield Advanced monitors application layer traffic to your Elastic IP addresses, ELB, CloudFront or Route 53 resources. It detects application layer attacks like HTTP floods or DNS query floods by baselining traffic on your resource and identifying anomalies. If any of these services scale up in response to a DDoS attack, AWS will provide service credits for charges due to usage spikes.

Protecting DNS
==============

Amazon Inspector
****************

Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. The service automatically assesses applications for vulnerabilities or deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed report with prioritized steps for remediation.

It is agent-based, API-driven, and delivered as a service. This makes it easy for you to build right into your existing DevOps process, decentralizing and automating vulnerability assessments, and empowering your DevOps teams to make security assessment an integral part of the deployment process.



AWS Config
**********

AWS Config is a service that enables customers to assess, audit, an evaluate the configurations of AWS resources. AWS Config continuously monitors and records AWS resource configurations and allows customers to automate the evaluation of recorded configurations against desired configurations.

With Config, customers can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine the overall compliance against the configurations specified in their internal or best-practices guidelines. Config enable customers to simplify compliance auditing, security analysis, change management, and operational troubleshooting.

In addition, AWS Config can compare configuration changes against best-practices configuration rules, which are available from AWS. Any deviations can generate notification or automated remediation events that trigger actions using services like AWS Lambda. Config can also be used to track resource inventory of the environment.

Cloud Migration
***************

.. figure:: /appendix_d/options.png

	Migration options

.. figure:: /appendix_d/tools.png

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

.. figure:: /intro_d/maturity.png
	:align: center

	AWS maturity versus activities

IT team members who used to work on projects like storage array deployments and server refreshes can transition to become DevOps specialists. By being integrated into the dev team, they can support the development of new products and services.

.. figure:: /intro_d/server.png
	:align: center

	Server benefits

.. figure:: /intro_d/network.png
	:align: center

	Network benefits

.. figure:: /intro_d/storage.png
	:align: center

	Storage benefits

.. figure:: /intro_d/application.png
	:align: center

	Application benefits

.. figure:: /intro_d/facilities.png
	:align: center

	Facilities benefits

.. figure:: /intro_d/securityben.png
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

AWS has a shared security model, which means that AWS shares security responsibilities with customers. In this model, AWS is responsible for the security of everything from the hypervisor level to the operating system.

AWS helps to reduce security risks in numerous ways:

* Leverages AWS automation and tools available to help customers mitigate the most severe security risks, including denial of service attacks.

* Provides the AWS Identity Access Management (IAM), service to centrally manage users and credentials, which helps customers reduce or eliminate the existence of "rogue servers".

* Leverages our roster of 30 plus compliance certifications and accreditations to help our customers build secure, compliance-ready environment.

.. figure:: /intro_d/shared.png
	:align: center

	AWS shared security model

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

.. image:: /intro_d/kpis.png

Time to market for new applications
-----------------------------------

Some of the most important activities that a healthy business must do to continue to grow and innovate are to scope, prioritize, and take on new initiatives. You can think about the initiative process like a project funnel.

.. figure:: /intro_d/funnel.png
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

.. image:: /intro_d/financial.png

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