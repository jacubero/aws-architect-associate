Cloud computing
###############

In this section, I outline the definition of cloud computing given by NIST and map its essential characteristics, service and deployment models with the AWS offering. 

Definition
**********

The National Institute of Standards and Technology (NIST) comprehensively outlined the definition of Cloud Computing in their September 2011 `NIST SP 800-145 <https://csrc.nist.gov/publications/detail/sp/800-145/final>`_ publication:

	*Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction.*

This cloud model is composed of five essential characteristics, three service models, and four deployment models.

Essential Characteristics
*************************

1. On-demand self-service
=========================

*A consumer can unilaterally provision computing capabilities, such as server time and network storage, as needed automatically without requiring human interaction with each service provider.*

To access Amazon Web Services (AWS) Cloud services, you can use the AWS Management Console, the AWS Command Line Interface (CLI), or the AWS Software Development Kits (SDKs). These services are provisioned automatically without any human intervention from AWS staff.

When you create a user, that user has no permissions by default. To give your users the permissions they need, you attach policies to them. It applies also to controlling user access to the AWS Management Console, AWS CLI or AWS SDKs.

2. Broad network access
=======================

*Capabilities are available over the network and accessed through standard mechanisms that promote use by heterogeneous thin or thick client platforms (e.g., mobile phones, tablets, laptops, and workstations).*

The AWS Management Console has been designed to work on tablets as well as other kinds of devices:

* Horizontal and vertical space is maximized to show more on your screen.

* Buttons and selectors are larger for a better touch experience.

The AWS Management Console is also available as an app for Android and iOS. This app provides mobile-relevant tasks that are a good companion to the full web experience. For example, you can easily view and manage your existing Amazon EC2 instances and Amazon CloudWatch alarms from your phone.

You can download the AWS Console mobile app from Amazon Appstore, Google Play, or iTunes.

3. Resource pooling
===================

*The provider’s computing resources are pooled to serve multiple consumers using a multi-tenant model, with different physical and virtual resources dynamically assigned and reassigned according to consumer demand. There is a sense of location independence in that the customer generally has no control or knowledge over the exact location of the provided resources but may be able to specify location at a higher level of abstraction (e.g., country, state, or datacenter). Examples of resources include storage, processing, memory, and network bandwidth.*

The global infrastructure that supports AWS cloud platform is distributed in several separate geographic areas around the world. These areas are called regions which consist of two or more Availability Zones (AZ) - most of the regions have 3 AZs -. Currently, these are the following regions:

.. csv-table:: AWS Region List
   :file: cloud_d/regions.csv
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


.. csv-table:: AWS Availability Zones List
   :file: cloud_d/azs.csv
   :widths: 20, 40, 40
   :header-rows: 1

Every region has two redundant transit centers which provide connectivity to the region to the rest of the world. An Availability Zone (AZ) consists of several datacenters (it normally ranges from 2 to 8), all of them linked via intra-AZ connections. All AZ are connected among them through inter-AZ connections and to the exterior via Transit Center connections. Several AZ has more than 300K servers.

.. figure:: /cloud_d/connectivity.png
   :name: fig-connectivity
   :target: /cloud_d/connectivity.png
   :alt: Intra-Region connectivity

	Intra-Region connectivity

.. Hint:: More information on `AWS re:Invent 2016: Tuesday Night Live with James Hamilton <https://www.youtube.com/watch?v*AyOAjFNPAbA>`_

AWS services aren’t replicated across regions by default unless you choose to do so. Each region is completely independent from the rest and is designed to be completely isolated from the other regions. This achieves the greatest possible fault tolerance and stability. Availability Zones are built to be independent and physically separated from one another. Data center locations are carefully selected to mitigate environmental risks, such as flooding, extreme weather, and seismic activity. A detailed description of AWS data centers secure design and controls can be found at `AWS data centers controls <https://aws.amazon.com/compliance/data-center/controls/?nc1*h_ls>`_.

`Global infrastructure <https://infrastructure.aws/>`_.

4. Rapid elasticity
===================

*Capabilities can be elastically provisioned and released, in some cases automatically, to scale rapidly outward and inward commensurate with demand. To the consumer, the capabilities available for provisioning often appear to be unlimited and can be appropriated in any quantity at any time.*

:ref:`secAWSAutoScaling` monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost. Currently, the supported applications are: :ref:`secECS`, :ref:`secEMR`, :ref:`secEC2`, :ref:`secAppStream`, :ref:`secDynamoDB`, :ref:`secRDS`, :ref:`secSageMaker`, :ref:`secComprehend`. 

Any service that you build with adjustable resource capacity can be automatically scaled using the new Custom Resource Scaling feature of Application Auto Scaling. To use Custom Resource Scaling, you register an HTTP endpoint with the Application Auto Scaling service, which will use that endpoint to scale your resource.

5. Measured service
===================

*Cloud systems automatically control and optimize resource use by leveraging a metering capability [1]_ at some level of abstraction appropriate to the type of service (e.g., storage, processing, bandwidth, and active user accounts). Resource usage can be monitored, controlled, and reported, providing transparency for both the provider and consumer of the utilized service.*

:ref:`secCloudWatch` monitors your AWS resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications. A namespace is a container for CloudWatch metrics. For the list of AWS namespaces, see `AWS Services That Publish CloudWatch Metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_.

CloudWatch ServiceLens enhances the observability of your services and applications by enabling you to integrate traces, metrics, logs, and alarms into one place. ServiceLens integrates CloudWatch with :ref:`secXRay` to provide an end-to-end view of your application to help you more efficiently pinpoint performance bottlenecks and identify impacted users. A service map displays your service endpoints and resources as “nodes” and highlights the traffic, latency, and errors for each node and its connections. You can choose a node to see detailed insights about the correlated metrics, logs, and traces associated with that part of the service. This enables you to investigate problems and their effect on the application. 

.. figure:: /cloud_d/ServiceMap.png

	Service Map

You can use Event history in the :ref:`secCloudTrail` console to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. This includes activity made through the :ref:`secConsole`, :ref:`secCLI`, and AWS SDKs and APIs. CloudTrail is enabled by default for your AWS account.

.. [1] Typically this is done on a pay-per-use or charge-per-use basis.

Service Models
**************

Software as a Service (SaaS)
============================

*The capability provided to the consumer is to use the provider’s applications running on a cloud infrastructure [2]_. The applications are accessible from various client devices through either a thin client interface, such as a web browser (e.g., web-based email), or a program interface. The consumer does not manage or control the underlying cloud infrastructure including network, servers, operating systems, storage, or even individual application capabilities, with the possible exception of limited userspecific application configuration settings.*

AWS offers SaaS solutions through `AWS Marketplace <https://aws.amazon.com/marketplace>`_. AWS Marketplace is a digital catalog with thousands of software listings from independent software vendors that make it easy to find, test, buy, and deploy software that runs on AWS.

Platform as a Service (PaaS)
============================

*The capability provided to the consumer is to deploy onto the cloud infrastructure consumer-created or acquired applications created using programming languages, libraries, services, and tools supported by the provider [3]_. The consumer does not manage or control the underlying cloud infrastructure including network, servers, operating systems, or storage, but has control over the deployed applications and possibly configuration settings for the application-hosting environment.*

AWS has a PaaS service called :ref:`secBeanstalk`.

Infrastructure as a Service (IaaS)
==================================

*The capability provided to the consumer is to provision processing, storage, networks, and other fundamental computing resources where the consumer is able to deploy and run arbitrary software, which can include operating systems and applications. The consumer does not manage or control the underlying cloud infrastructure but has control over operating systems, storage, and deployed applications; and possibly limited control of select networking components (e.g., host firewalls).*

Most of AWS services are IaaS.

.. [2] A cloud infrastructure is the collection of hardware and software that enables the five essential characteristics of cloud computing. The cloud infrastructure can be viewed as containing both a physical layer and an abstraction layer. The physical layer consists of the hardware resources that are necessary to support the cloud services being provided, and typically includes server, storage and network components. The abstraction layer consists of the software deployed across the physical layer, which manifests the essential cloud characteristics. Conceptually the abstraction layer sits above the physical layer.

.. [3] This capability does not necessarily preclude the use of compatible programming languages, libraries, services, and tools from other sources.

Deployment Models
*****************

* **Private cloud**. The cloud infrastructure is provisioned for exclusive use by a single organization comprising multiple consumers (e.g., business units). It may be owned, managed, and operated by the organization, a third party, or some combination of them, and it may exist on or off premises.

* **Community cloud**. The cloud infrastructure is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns (e.g., mission, security requirements, policy, and compliance considerations). It may be owned, managed, and operated by one or more of the organizations in the community, a third party, or some combination of them, and it may exist on or off premises.

* **Public cloud**. The cloud infrastructure is provisioned for open use by the general public. It may be owned, managed, and operated by a business, academic, or government organization, or some combination of them. It exists on the premises of the cloud provider.

* **Hybrid cloud**. The cloud infrastructure is a composition of two or more distinct cloud infrastructures (private, community, or public) that remain unique entities, but are bound together by standardized or proprietary technology that enables data and application portability (e.g., cloud bursting for load balancing between clouds). 

Most of AWS Services are provisioned using a Public cloud deployment model. However, `AWS Outposts <https://aws.amazon.com/outposts/>`_ bring native AWS services, infrastructure, and operating models across on premises and the AWS cloud to deliver a truly consistent hybrid experience. AWS Outposts is designed for connected environments and can be used to support workloads that need to remain on-premises due to low latency or local data processing needs.

AWS Outposts come in two variants: 

1. VMware Cloud on AWS Outposts allows you to use the same VMware control plane and APIs you use to run your infrastructure.

2. AWS native variant of AWS Outposts allows you to use the same exact APIs and control plane you use to run in the AWS cloud, but on premises.

AWS Outposts infrastructure is fully managed, maintained, and supported by AWS to deliver access to the latest AWS capabilities. Getting started is easy, you simply log into the AWS Management Console to order your Outpost, choosing from a wide catalog of Amazon EC2 instances and capacity and EBS storage options.  

Advantages
==========

`The Six Main Benefits of Cloud Computing with Amazon Web Services <https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html>`_ are the following:

* **Trade capital expense for variable expense**. Instead of having to invest heavily in data centers and servers before you know how you’re going to use them, you can pay only when you consume computing resources, and pay only for how much you consume.

* **Benefit from massive economies of scale**. By using cloud computing, you can achieve a lower variable cost than you can get on your own. Because usage from hundreds of thousands of customers is aggregated in the cloud, providers such as AWS can achieve higher economies of scale, which translates into lower pay as-you-go prices.

AWS has executed several price reductings on many products. You can get AWS prices changes information `Using the AWS Price List API <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html>`_. For example the following chart illustres the EC2 price trend



* **Stop guessing capacity**. Eliminate guessing on your infrastructure capacity needs. When you make a capacity decision prior to deploying an application, you often end up either sitting on expensive idle resources or dealing with limited capacity. With cloud computing, these problems go away. You can access as much or as little capacity as you need, and scale up and down as required with only a few minutes’ notice.

* **Increase speed and agility**. In a cloud computing environment, new IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. This results in a dramatic increase in agility for the organization, since the cost and time it takes to experiment and develop is significantly lower.

**Stop spending money running and maintaining data centers**. Focus on projects that differentiate your business, not the infrastructure. Cloud computing lets you focus on your own customers, rather than on the heavy lifting of racking, stacking, and powering servers.

**Go global in minutes**. Easily deploy your application in multiple regions around the world with just a few clicks. This means you can provide lower latency and a better experience for your customers at minimal cost.

For more information about the Six Main Benefits of Cloud Computing with AWS see at `Andy Jassy talk <https://www.youtube.com/watch?v=yMJ75k9X5_8>>`_.
