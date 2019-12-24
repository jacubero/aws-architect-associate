Introduction
############

Cloud computing
***************

In this section, I outline the definition of cloud computing given by NIST and map its essential characteristics, service and deployment models with the AWS offering. 

Definition
==========

The National Institute of Standards and Technology (NIST) comprehensively outlined the definition of Cloud Computing in their September 2011 `NIST SP 800-145 <https://csrc.nist.gov/publications/detail/sp/800-145/final>`_ publication:

	*Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction.*

`What is cloud computing? <https://aws.amazon.com/what-is-cloud-computing/>`_

This cloud model is composed of five essential characteristics, three service models, and four deployment models.

Essential Characteristics
=========================

1. On-demand self-service
-------------------------

*A consumer can unilaterally provision computing capabilities, such as server time and network storage, as needed automatically without requiring human interaction with each service provider.*

To access Amazon Web Services (AWS) Cloud services, you can use the AWS Management Console, the AWS Command Line Interface (CLI), or the AWS Software Development Kits (SDKs). These services are provisioned automatically without any human intervention from AWS staff.

When you create a user, that user has no permissions by default. To give your users the permissions they need, you attach policies to them. It applies also to controlling user access to the AWS Management Console, AWS CLI or AWS SDKs.

2. Broad network access
-----------------------

*Capabilities are available over the network and accessed through standard mechanisms that promote use by heterogeneous thin or thick client platforms (e.g., mobile phones, tablets, laptops, and workstations).*

The AWS Management Console has been designed to work on tablets as well as other kinds of devices:

* Horizontal and vertical space is maximized to show more on your screen.

* Buttons and selectors are larger for a better touch experience.

The AWS Management Console is also available as an app for Android and iOS. This app provides mobile-relevant tasks that are a good companion to the full web experience. For example, you can easily view and manage your existing Amazon EC2 instances and Amazon CloudWatch alarms from your phone.

You can download the AWS Console mobile app from Amazon Appstore, Google Play, or iTunes.

3. Resource pooling
-------------------

*The provider’s computing resources are pooled to serve multiple consumers using a multi-tenant model, with different physical and virtual resources dynamically assigned and reassigned according to consumer demand. There is a sense of location independence in that the customer generally has no control or knowledge over the exact location of the provided resources but may be able to specify location at a higher level of abstraction (e.g., country, state, or datacenter). Examples of resources include storage, processing, memory, and network bandwidth.*

:ref:`secGlobalInfrastructure`

4. Rapid elasticity
-------------------

*Capabilities can be elastically provisioned and released, in some cases automatically, to scale rapidly outward and inward commensurate with demand. To the consumer, the capabilities available for provisioning often appear to be unlimited and can be appropriated in any quantity at any time.*

:ref:`secAWSAutoScaling` monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost. Currently, the supported applications are: :ref:`secECS`, :ref:`secEMR`, :ref:`secEC2`, :ref:`secAppStream`, :ref:`secDynamoDB`, :ref:`secRDS`, :ref:`secSageMaker`, :ref:`secComprehend`. 

Any service that you build with adjustable resource capacity can be automatically scaled using the new Custom Resource Scaling feature of Application Auto Scaling. To use Custom Resource Scaling, you register an HTTP endpoint with the Application Auto Scaling service, which will use that endpoint to scale your resource.

5. Measured service
-------------------

*Cloud systems automatically control and optimize resource use by leveraging a metering capability [1]_ at some level of abstraction appropriate to the type of service (e.g., storage, processing, bandwidth, and active user accounts). Resource usage can be monitored, controlled, and reported, providing transparency for both the provider and consumer of the utilized service.*

:ref:`secCloudWatch` monitors your AWS resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications. A namespace is a container for CloudWatch metrics. For the list of AWS namespaces, see `AWS Services That Publish CloudWatch Metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_.

CloudWatch ServiceLens enhances the observability of your services and applications by enabling you to integrate traces, metrics, logs, and alarms into one place. ServiceLens integrates CloudWatch with AWS XRay to provide an end-to-end view of your application to help you more efficiently pinpoint performance bottlenecks and identify impacted users. A service map displays your service endpoints and resources as “nodes” and highlights the traffic, latency, and errors for each node and its connections. You can choose a node to see detailed insights about the correlated metrics, logs, and traces associated with that part of the service. This enables you to investigate problems and their effect on the application. 

.. figure:: /intro_d/ServiceMap.png

	Service Map

You can use Event history in the :ref:`secCloudTrail` console to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. This includes activity made through the :ref:`secConsole`, :ref:`secCLI`, and AWS SDKs and APIs. CloudTrail is enabled by default for your AWS account.

.. [1] Typically this is done on a pay-per-use or charge-per-use basis.

Service Models
==============

Software as a Service (SaaS)
----------------------------

*The capability provided to the consumer is to use the provider’s applications running on a cloud infrastructure [2]_. The applications are accessible from various client devices through either a thin client interface, such as a web browser (e.g., web-based email), or a program interface. The consumer does not manage or control the underlying cloud infrastructure including network, servers, operating systems, storage, or even individual application capabilities, with the possible exception of limited userspecific application configuration settings.*

AWS offers SaaS solutions through `AWS Marketplace <https://aws.amazon.com/marketplace>`_. AWS Marketplace is a digital catalog with thousands of software listings from independent software vendors that make it easy to find, test, buy, and deploy software that runs on AWS.

Platform as a Service (PaaS)
----------------------------

*The capability provided to the consumer is to deploy onto the cloud infrastructure consumer-created or acquired applications created using programming languages, libraries, services, and tools supported by the provider [3]_. The consumer does not manage or control the underlying cloud infrastructure including network, servers, operating systems, or storage, but has control over the deployed applications and possibly configuration settings for the application-hosting environment.*

AWS has a PaaS service called :ref:`secBeanstalk`.

Infrastructure as a Service (IaaS)
----------------------------------

*The capability provided to the consumer is to provision processing, storage, networks, and other fundamental computing resources where the consumer is able to deploy and run arbitrary software, which can include operating systems and applications. The consumer does not manage or control the underlying cloud infrastructure but has control over operating systems, storage, and deployed applications; and possibly limited control of select networking components (e.g., host firewalls).*

Most of AWS services are IaaS.

.. [2] A cloud infrastructure is the collection of hardware and software that enables the five essential characteristics of cloud computing. The cloud infrastructure can be viewed as containing both a physical layer and an abstraction layer. The physical layer consists of the hardware resources that are necessary to support the cloud services being provided, and typically includes server, storage and network components. The abstraction layer consists of the software deployed across the physical layer, which manifests the essential cloud characteristics. Conceptually the abstraction layer sits above the physical layer.

.. [3] This capability does not necessarily preclude the use of compatible programming languages, libraries, services, and tools from other sources.

Deployment Models
=================

* **Private cloud**. The cloud infrastructure is provisioned for exclusive use by a single organization comprising multiple consumers (e.g., business units). It may be owned, managed, and operated by the organization, a third party, or some combination of them, and it may exist on or off premises.

* **Community cloud**. The cloud infrastructure is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns (e.g., mission, security requirements, policy, and compliance considerations). It may be owned, managed, and operated by one or more of the organizations in the community, a third party, or some combination of them, and it may exist on or off premises.

* **Public cloud**. The cloud infrastructure is provisioned for open use by the general public. It may be owned, managed, and operated by a business, academic, or government organization, or some combination of them. It exists on the premises of the cloud provider.

* **Hybrid cloud**. The cloud infrastructure is a composition of two or more distinct cloud infrastructures (private, community, or public) that remain unique entities, but are bound together by standardized or proprietary technology that enables data and application portability (e.g., cloud bursting for load balancing between clouds). 

Most of AWS Services are provisioned using a Public cloud deployment model. However, `AWS Outposts <https://aws.amazon.com/outposts/>`_ bring native AWS services, infrastructure, and operating models across on premises and the AWS cloud to deliver a truly consistent hybrid experience. AWS Outposts is designed for connected environments and can be used to support workloads that need to remain on-premises due to low latency or local data processing needs.

AWS Outposts come in two variants: 

1. VMware Cloud on AWS Outposts allows you to use the same VMware control plane and APIs you use to run your infrastructure.

2. AWS native variant of AWS Outposts allows you to use the same exact APIs and control plane you use to run in the AWS cloud, but on premises.

AWS Outposts infrastructure is fully managed, maintained, and supported by AWS to deliver access to the latest AWS capabilities. Getting started is easy, you simply log into the AWS Management Console to order your Outpost, choosing from a wide catalog of Amazon EC2 instances and capacity and EBS storage options.  

Six advantages of cloud computing
=================================

`How AWS came to be <https://techcrunch.com/2016/07/02/andy-jassys-brief-history-of-the-genesis-of-aws/>`_

`Six Advantages of Cloud Computing <https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html>`_

`The Six Main Benefits of Cloud Computing with Amazon Web Services <https://www.youtube.com/watch?v=yMJ75k9X5_8>`_

AWS cloud benefits
------------------

* No up-front investment

* Low on-going costs

* Focus on innovation

* Flexible innovation

* Speed and agility

* Global reach on demand

On-premises considerations
--------------------------

* Large upfront capital expense

* Labor, patches and upgrade cycles

* System administration

* Fixed capacity

* Procurement and setup

* Limited geographic regions

Overview of Amazon Web Services
*******************************

`Overview of Amazon Web Services <https://d1.awsstatic.com/whitepapers/aws-overview.pdf>`_

AWS products and services
=========================

.. figure:: /intro_d/products.png
   :name: fig-products
   :target: /intro_d/products.png
   :alt: AWS products and services

AWS pricing
===========

.. figure:: /intro_d/prices.png

	Pricing characteristics

`How do you pay for AWS? <https://aws.amazon.com/pricing/>`_

`How AWS Pricing Works <https://d0.awsstatic.com/whitepapers/aws_pricing_overview.pdf>`_

`Simple monthly calculator <https://calculator.s3.amazonaws.com/index.html>`_

`TCO calculator <https://aws.amazon.com/tco-calculator/>`_

Security of the cloud
=====================

AWS compute security
--------------------

.. figure:: /intro_d/computesec.png

	AWS compute security

AWS memory and storage protection
---------------------------------

.. figure:: /intro_d/memorysec.png

	AWS memory and storage protection

Database security
-----------------

.. figure:: /intro_d/dbsec.png

	Database security


The AWS Well-Architected Framework
**********************************

`AWS Well-Architected Framework <https://aws.amazon.com/es/architecture/well-architected/>`_

AWS Well-Architected Tool
=========================

The AWS Well-Architected Tool helps you review your workloads against current AWS best practices and provides guidance on how to improve your cloud architectures. This tool is based on the **AWS Well-Architected Framework**. The AWS Well-Architected Framework has been developed to help cloud architects build secure, high-performing, resilient, and efficient infrastructure for their applications. Based on five pillars — operational excellence, security, reliability, performance efficiency, and cost optimization. — the Framework provides a consistent approach for customers and partners to evaluate architectures, and implement designs that will scale over time.

This is a free tool, available in the `AWS Management Console <https://console.aws.amazon.com/wellarchitected>`_. The process to evaluate a workload consists of 3 steps:

1. **Define a workload** by filling information about the architecture: name, a brief description to document its scope and intented purpose, the environment (production or pre-production), AWS Regions and Non-AWS Regions in which the workload runs, Account IDs (optional), industry type (optional) and industry (optional).

2. **Document the Workload State** by answering a series of questions about your architecture that span the pillars of the AWS Well-Architected Framework: operational excellence, security, reliability, performance efficiency, and cost optimization. After documenting the state of your workload for the first time, you should save a milestone and generate a workload report. A *milestone* captures the current state of the workload and enables you to measure progress as you make changes based on your improvement plan.

3. **Review the Improvement Plan**. Based on the best practices you selected, AWS WA Tool identifies areas of high and medium risk as measured against the AWS Well-Architected Framework. The Improvement items section shows the recommended improvement items identified in the workload. The questions are ordered based on the pillar priority that is set, with any high risk items listed first followed by any medium risk items.

4. **Make Improvements and Measure Progress**. After deciding what improvement actions to take, update the Improvement status to indicate that improvements are in progress. After making changes, you can return to the Improvement plan and see the effect those changes had on the workload. 

Security
========

.. figure:: /intro_d/security.png

	Security Pillar

`Security pillar <https://d1.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf>`_

Reliability
===========

.. figure:: /intro_d/reliability.png

	Reliability Pillar

`Reliability Pillar <https://d1.awsstatic.com/whitepapers/architecture/AWS-Reliability-Pillar.pdf>`_

`Chaos Monkey <https://github.com/Netflix/chaosmonkey>`_ is a Netflix resiliency tool that helps applications tolerate random instance failures.

`Bees with Machine Guns! <https://github.com/newsapps/beeswithmachineguns>`_ is a utility for arming (creating) many bees (micro EC2 instances) to attack (load test) targets (web applications).

`La crisis con Amazon AWS <https://gallir.wordpress.com/2011/08/10/la-crisis-con-amazon-aws/>`_.

Cost Optimization
=================

.. figure:: /intro_d/cost.png

	Cost Optimization Pillar

`Cost Optimization Pillar <https://d1.awsstatic.com/whitepapers/architecture/AWS-Cost-Optimization-Pillar.pdf>`_

Operational Excellence
======================

.. figure:: /intro_d/operational.png

	Operational Excellence Pillar

`Operational Excellence Pillar <https://d1.awsstatic.com/whitepapers/architecture/AWS-Operational-Excellence-Pillar.pdf>`_

Performance efficiency
======================

.. figure:: /intro_d/performance.png

	Performance efficiency Pillar

`Performance efficiency Pillar <https://d1.awsstatic.com/whitepapers/architecture/AWS-Performance-Efficiency-Pillar.pdf>`_

AWS Global Infrastructure
*************************

AWS Data Centers
================

`Learn how we secure AWS data centers by design <https://aws.amazon.com/compliance/data-center/>`_

AWS Availability Zones
======================

An Availability Zone (AZ) consists of several datacenters, all of them linked via intra-AZ connections and each with with redundant power supplies, networking and connectivity, housed in separated facilitiess. All AZ are connected among them through inter-AZ connections and to the exterior via Transit Center connections. AZs are represented by a region code followed by a letter identifier.

.. csv-table:: AWS Availability Zones List
   :file: intro_d/azs.csv
   :widths: 20, 40, 40
   :header-rows: 1

AWS Regions
===========

`Global Infrastructure <https://aws.amazon.com/about-aws/global-infrastructure/#reglink-pr>`_

`AWS Global infrastructure interactive map <https://infrastructure.aws/>`_

The global infrastructure that supports AWS cloud platform is distributed in several separate geographic areas around the world. These areas are called **regions** which consist of two or more **Availability Zones** (AZ) - most of the regions have 3 AZs. Currently, these are the following regions represented by a region code:

.. csv-table:: AWS Region List
   :file: intro_d/regions.csv
   :widths: 20, 40, 40
   :header-rows: 1

.. Note:: Available Regions.

   AWS GovCloud (US-West) account provides access to the AWS GovCloud (US-West) Region only. An Amazon AWS (China) account provides access to the Beijing and Ningxia Regions only. 

   You can't describe or access additional Regions from an AWS account, such as AWS GovCloud (US-West) or the China Regions.

   To use a Region introduced after March 20, 2019, you must enable the Region. For more information, see `Managing AWS Regions <https://docs.aws.amazon.com/general/latest/gr/rande-manage.html>`_ in the AWS General Reference.

.. Note:: Enabled Regions.

   If the Region is enabled by default, the output includes the following:

   *"OptInStatus": "opt-in-not-required"*

   If the Region is not enabled, the output includes the following:

   *"OptInStatus": "not-opted-in"*

   After an opt-in Region is enabled, the output includes the following:

   *"OptInStatus": "opted-in"*

.. figure:: /intro_d/connectivity.png
   :name: fig-connectivity
   :target: /intro_d/connectivity.png
   :alt: Intra-Region connectivity

   Intra-Region connectivity

`AWS re:Invent 2016: Tuesday Night Live with James Hamilton <https://www.youtube.com/watch?v*AyOAjFNPAbA>`_

AWS Edge Locations
==================

`Amazon CloudFront Key Features <https://aws.amazon.com/cloudfront/features>`_

