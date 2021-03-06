Amazon EC2
##########

Resources
*********

Instances
=========

Inside AWS physical servers, there are hypervisors on which guest virtual machines live, called Elastic Compute Cloud (EC2) instances. AWS provides various configurations of CPU, memory, storage, and networking capacity for your instances, known as *instance types*. In 2007, AWS provide only one instance type called M1, since then a lot of instances types have been launched by AWS (175 instances type since 2007 to 2018). This continued rapid pace of innovation has been possible thanks to the `AWS Nitro System <https://aws.amazon.com/ec2/nitro/>`_.

.. figure:: /ec2_d/ec2.png
   :align: center

	 Amazon EC2

Amazon EC2 instance types
-------------------------

An exammple of an API name of an EC2 instance type is ``M5d.xlarge``.  The first character (in this example ``M``) identifies the instance family. Each instance family is designed for an specific workload needs in terms of CPU, memory, storage and network performance. Amazon EC2 families define different ratios among CPU, memory, storage and network performance. Below you an find the current instance families together with the letters associated with them, and the meaning of each of the letters:

* **General Purpose**: ``A`` : ARM, ``T``: Turbo(Burstable), ``M``: Most Scenarios.

* **Compute Optimized**: ``C``: Compute.

* **Memory Optimized**: ``R``: Random-access memory, ``X``: Extra-large memory (approx 4 TB DRAM), ``U``: High memory (purpose built to run large in-memory databases), ``Z``: High frequency.

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

.. figure:: /ec2_d/nomenclature.png
   :align: center

	 Amazon EC2 instance types nomenclature

`Amazon EC2 instance types <https://aws.amazon.com/ec2/instance-types/>`_ 

`Introducing Elastic Fabric Adapter <https://aws.amazon.com/about-aws/whats-new/2018/11/introducing-elastic-fabric-adapter/>`_

`EC2 Instance Types & Pricing <http://ec2pricing.net/>`_

`EC2Instances.info <https://www.ec2instances.info/>`_

.. _secAMI:

Amazon Machine Images (AMIs)
----------------------------

AMI is the software required to launch an EC2 instance. There are 3 different types:

* **Amazon maintained** AMIs which offer a broad set of Linux and Windows images.

* **Marketplace maintained** AMIs managed and maintained by AWS Marketplace partners.

* **Your machine images** are AMIs you have created from Amazon EC2 instances. You can maintain them as private in your account, shared with other accounts and even made them public to the community.  

You can copy an Amazon Machine Image (AMI) within or across an AWS region using the AWS Management Console, the AWS command line tools or SDKs, or the Amazon EC2 API, all of which support the ``CopyImage`` action. You can copy both Amazon EBS-backed AMIs and instance store-backed AMIs. You can copy encrypted AMIs and AMIs with encrypted snapshots.

Amazon EC2 uses public–key cryptography to encrypt and decrypt login information. Public–key cryptography uses a public key to encrypt a piece of data, such as a password, then the recipient uses the private key to decrypt the data. The public and private keys are known as a key pair.

To log in to your instance, you must create a key pair, specify the name of the key pair when you launch the instance, and provide the private key when you connect to the instance. On a Linux instance, the public key content is placed in an entry within ``~/.ssh/authorized_keys``. This is done at boot time and enables you to securely access your instance using the private key instead of a password.

The appropriate user names for connecting to a newly created Amazon EC2 instance are as follows:

* For an Amazon Linux AMI, the user name is ``ec2-user``.

* For a RHEL AMI, the user name is ``ec2-user`` or ``root``.

* For an Ubuntu AMI, the user name is ``ubuntu`` or ``root``.

* For a Centos AMI, the user name is ``centos``.

* For a Debian AMI, the user name is ``admin`` or ``root``.

* For a Fedora AMI, the user name is ``ec2-user``.

* For a SUSE AMI, the user name is ``ec2-user`` or ``root``.

`Amazon Machine Images (AMI) <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html>`_

`How do I create an Amazon Machine Image (AMI) from my EBS-backed EC2 instance? <https://www.youtube.com/watch?time_continue=5&v=vSKWBBrEbNQ&feature=emb_logo>`_

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

The virtual devices for instance store volumes are named as ``ephemeral[0-23]``. Instance types that support one instance store volume have ``ephemeral0``. Instance types that support two instance store volumes have ``ephemeral0`` and ``ephemeral1``, and so on until ``ephemeral23``.

If you create an AMI from an instance, the data on its instance store volumes aren't preserved and aren't present on the instance store volumes of the instances that you launch from the AMI. You can specify instance store volumes for an instance only when you launch it. You can't detach an instance store volume from one instance and attach it to a different instance.

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

If the instance is stopped, its **Elastic IP address** is disassociated from the instance if it is an EC2-Classic instance. Otherwise, if it is an EC2-VPC instance, the Elastic IP address remains associated. By default, all AWS accounts are limited to 5 Elastic IP addresses per region for each AWS account, because public (IPv4) Internet addresses are a scarce public resources. AWS strongly encourages you to use and EIP primarily for load balancing use cases, and use DNS hostnames for all other inter-node communication.

If you feel your architecture warrants additional EIPs, you would need to complete the Amazon EC2 Elastic IP Address Request Form and give reasons as to your need for additional addresses.

When you launch an EC2 instance into a default VPC, AWS provides it with public and private DNS hostnames that correspond to the public IPv4 and private IPv4 addresses for the instance.

However, when you launch an instance into a non-default VPC, AWS provides the instance with a private DNS hostname only. New instances will only be provided with public DNS hostname depending on these two DNS attributes: the DNS resolution and DNS hostnames, that you have specified for your VPC, and if your instance has a public IPv4 address.

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

It is recommended that you launch the number of instances that you need in the placement group in a single launch request and that you use the same instance type for all instances in the placement group. If you try to add more instances to the placement group later, or if you try to launch more than one instance type in the placement group, you increase your chances of getting an insufficient capacity error.

If you stop an instance in a placement group and then start it again, it still runs in the placement group. However, the start fails if there isn't enough capacity for the instance.

If you receive a capacity error when launching an instance in a placement group that already has running instances, stop and start all of the instances in the placement group, and try the launch again. Restarting the instances may migrate them to hardware that has capacity for all the requested instances.

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

Instance metadata is the data about your instance that you can use to configure or manage the running instance. You can get the instance ID, public keys, public IP address and many other information from the instance metadata by firing a URL command in your instance to this URL:

`<http://169.254.169.254/latest/meta-data/>`_

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

You can use Run Command from the console to configure instances without having to login to each instance. AWS Systems Manager Run Command lets you remotely and securely manage the configuration of your managed instances. A managed instance is any Amazon EC2 instance or on-premises machine in your hybrid environment that has been configured for Systems Manager. Run Command enables you to automate common administrative tasks and perform ad hoc configuration changes at scale. You can use Run Command from the AWS console, the AWS Command Line Interface, AWS Tools for Windows PowerShell, or the AWS SDKs. Run Command is offered at no additional cost.

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

* Seamless integration with AWS Systems Manager and AWS Organizations.

* Free service for all customers.

Monitoring
==========

Troubleshooting
===============

Troubleshooting Instance Launch Issues
--------------------------------------

Instance Terminates Immediately
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**: Your instance goes from the pending state to the terminated state immediately after restarting it.

**Cause**: The following are a few reasons why an instance might immediately terminate:

* You've reached your EBS volume limit.

* An EBS snapshot is corrupt.

* The root EBS volume is encrypted and you do not have permissions to access the KMS key for decryption.

* The instance store-backed AMI that you used to launch the instance is missing a required part (an image.part.xx file).

Connecting to Your Instance
---------------------------

Error connecting to your instance: Connection timed out
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you try to connect to your instance and get an error message ``Network error: Connection timed out`` or ``Error connecting to [instance], reason: -> Connection timed out: connect``, try the following:

* Check your security group rules. You need a security group rule that allows inbound traffic from your public IPv4 address on the proper port.

* Check the route table for the subnet. You need a route that sends all traffic destined outside the VPC to the internet gateway for the VPC.

* Check the network access control list (ACL) for the subnet. The network ACLs must allow inbound and outbound traffic from your local IP address on the proper port. The default network ACL allows all inbound and outbound traffic.

* If your computer is on a corporate network, ask your network administrator whether the internal firewall allows inbound and outbound traffic from your computer on port 22 (for Linux instances) or port 3389 (for Windows instances).

* Check that your instance has a public IPv4 address. If not, you can associate an Elastic IP address with your instance. 

* Check the CPU load on your instance; the server may be overloaded. AWS automatically provides data such as Amazon CloudWatch metrics and instance status, which you can use to see how much CPU load is on your instance and, if necessary, adjust how your loads are handled. 

To connect to your instance using an IPv6 address, check the following:

* Your subnet must be associated with a route table that has a route for IPv6 traffic (::/0) to an internet gateway.

* Your security group rules must allow inbound traffic from your local IPv6 address on the proper port (22 for Linux and 3389 for Windows).

* Your network ACL rules must allow inbound and outbound IPv6 traffic.

* If you launched your instance from an older AMI, it may not be configured for DHCPv6 (IPv6 addresses are not automatically recognized on the network interface). 

* Your local computer must have an IPv6 address, and must be configured to use IPv6.

Error: unable to load key … Expecting: ANY PRIVATE KEY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you try to connect to your instance and get the error message, ``unable to load key ... Expecting: ANY PRIVATE KEY``, the file in which the private key is stored is incorrectly configured. If the private key file ends in ``.pem``, it might still be incorrectly configured. A possible cause for an incorrectly configured private key file is a missing certificate.

Error: User key not recognized by server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you use PuTTY to connect to your instance:

* Verify that your private key (.pem) file has been converted to the format recognized by PuTTY (.ppk).

* Verify that you are connecting with the appropriate user name for your AMI. See section :ref:`secAMI`.

* Verify that you have an inbound security group rule to allow inbound traffic to the appropriate port. 

Error: Host key not found, Permission denied (publickey), or Authentication failed, permission denied
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you connect to your instance using SSH and get any of the following errors, ``Host key not found in [directory], Permission denied (publickey)``, or ``Authentication failed, permission denied``, verify that you are connecting with the appropriate user name for your AMI and that you have specified the proper private key (.pem) file for your instance. See section :ref:`secAMI`.

Error: Unprotected Private Key File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your private key file must be protected from read and write operations from any other users. If your private key can be read or written to by anyone but you, then SSH ignores your key and you see the following warning message below.

.. code-block:: console

  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  Permissions 0777 for '.ssh/my_private_key.pem' are too open.
  It is required that your private key files are NOT accessible by others.
  This private key will be ignored.
  bad permissions: ignore key: .ssh/my_private_key.pem
  Permission denied (publickey).

If you see a similar message when you try to log in to your instance, examine the first line of the error message to verify that you are using the correct public key for your instance. The above example uses the private key ``.ssh/my_private_key.pem`` with file permissions of ``0777``, which allow anyone to read or write to this file. This permission level is very insecure, and so SSH ignores this key. To fix the error, execute the following command, substituting the path for your private key file.

.. code-block:: console

  [ec2-user ~]$ chmod 0400 .ssh/my_private_key.pem

Error: Private key must begin with "-----BEGIN RSA PRIVATE KEY-----" and end with "-----END RSA PRIVATE KEY-----"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you use a third-party tool, such as ssh-keygen, to create an RSA key pair, it generates the private key in the OpenSSH key format. When you connect to your instance, if you use the private key in the OpenSSH format to decrypt the password, you'll get the error Private key must begin with ``"-----BEGIN RSA PRIVATE KEY-----" and end with "-----END RSA PRIVATE KEY-----"``.

To resolve the error, the private key must be in the PEM format. Use the following command to create the private key in the PEM format:

.. code-block:: console

  ssh-keygen -m PEM

Error: Server refused our key or No supported authentication methods available
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you use PuTTY to connect to your instance and get either of the following errors, ``Error: Server refused our key`` or ``Error: No supported authentication methods available``, verify that you are connecting with the appropriate user name for your AMI. See section :ref:`secAMI`.

You should also verify that your private key (.pem) file has been correctly converted to the format recognized by PuTTY (.ppk).

.. _secEC2pricing:

Pricing options
***************

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

* **Data transfer**. Data transferred between Amazon S3, Amazon Glacier, Amazon DynamoDB, Amazon SES, Amazon SQS, Amazon Kinesis, Amazon ECR, Amazon SNS or Amazon SimpleDB and Amazon EC2 instances in the same AWS Region is free. AWS Services accessed via PrivateLink endpoints will incur standard PrivateLink charges as explained here.

The following illustration represents the transitions between instance states. 

.. figure:: /ec2_d/instance_lifecycle.png
	:align: center

	EC2 instance lifecycle

Below are the valid EC2 lifecycle instance states: 

* ``pending``. The instance is preparing to enter the running state. An instance enters the pending state when it launches for the first time, or when it is restarted after being in the stopped state.

* ``running``. The instance is running and ready for use.

* ``stopping``. The instance is preparing to be stopped. Take note that you will not billed if it is preparing to stop however, you will still be billed if it is just preparing to hibernate.

* ``stopped``. The instance is shut down and cannot be used. The instance can be restarted at any time.

* ``shutting-down``. The instance is preparing to be terminated.

* ``terminated``. The instance has been permanently deleted and cannot be restarted. Take note that Reserved Instances that applied to terminated instances are still billed until the end of their term according to their payment option.

`Instance Lifecycle <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html>`_

The product options are the following:

* **Detailed monitoring**. You can use Amazon CloudWatch to monitor your EC2 instances. By default, basic monitoring is enabled and available at no additional cost. However, for a fixed monthly rate, you can opt for detailed monitoring, which includes 7 preselected metrics recorded once a minute. Partial months are charge on an hourly prorated basis, at a per instance-hour rate.

* **Auto scaling** automatically adjusts the number of EC2 instances in your deployment according to conditions you define. This service is available at no additional charge beyond CloudWatch fees.

* **Elastic IP addresses**. An Elastic IP address doesn’t incur charges as long as the following conditions are true:

  * The Elastic IP address is associated with an Amazon EC2 instance.
  * The instance associated with the Elastic IP address is running.
  * The instance has only one Elastic IP address attached to it.

If you've stopped or terminated an EC2 instance with an associated Elastic IP address and you don't need that Elastic IP address anymore, consider disassociating or releasing the Elastic IP address.

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

.. figure:: /ec2_d/regional.png
	:align: center

	Regional RIs simplify optimization

AWS Cost Explorer generates RI recommendations for AWS services including Amazon EC2, RDS, ElastiCache and Elasticsearch. You can use the *Recommendations* feature to perform "what-if" scenarios comparing costs and savings related to different RI types (standard versus convertible RIs), and RIs term lengths (1 versus 3 years).

Customers can combine regional RIs with on-demand capacity reservations to benefit from billing discounts. On-demand capacity reservations means:

* Reserving capacity for Amazon EC2 instances in a specific Availability Zone for any duration. This ensures access to EC2 capacity when needed, for as long as needed.

* Capacity reservations can be created at any time, without entering into a 1-year or 3-year term commitment, and the capacity is available immediately.

* Capacity reservations can be cancelled at anytime to stop incurring charges.

Capacity reservation is charged the equivalent on-demand rate, regardless of whether the instances are run. Customers can combine regional RIs with capacity reservatins to get billing discounts. If customers do not use a reservation, it is shown as an unused reservation on the customer's EC2 bill.

Zonal RI billing discounts do not apply to capacity reservations. Capacity reservations can't be created in placement groups. Capacity reservations can't be used with dedicated hosts.

Convertible Reserved Instances
------------------------------

Convertible RIs give customers the ability to modify reservations across families, sizes, operating system, and tenancy. The only aspect customer cannot modify is the Region. So, as long as the customer stays in the same Region, they can continue to modify the RIs. Convertibles give customers the opportunity to maximize flexibility and increase savings.

The only time customers cannot convert RIs is between the time the request to exchange is submitted and the time the request to exchange is fulfilled. Typically requests take only a matter of hours to fulfill but could take a up to 2 days.

.. figure:: /ec2_d/convertible.png
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

Scheduled Reserved Instances
----------------------------

Scheduled Reserved Instances (Scheduled Instances) enable you to purchase capacity reservations that recur on a daily, weekly, or monthly basis, with a specified start time and duration, for a one-year term. You reserve the capacity in advance, so that you know it is available when you need it. You pay for the time that the instances are scheduled, even if you do not use them.

.. figure:: /ec2_d/ec2_sched_ri_find_sched_2.png
  :align: center

  Scheduled Reserved Instances

Scheduled Instances are a good choice for workloads that do not run continuously, but do run on a regular schedule. For example, you can use Scheduled Instances for an application that runs during business hours or for batch processing that runs at the end of the week.

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

You can choose to have your Spot instances terminated, stopped, or hibernated upon interruption. Stop and hibernate options are available for persistent Spot requests and Spot Fleets with the maintain option enabled. By default, your one-time Spot instances are terminated.

Amazon EC2 Spot instances integrate natively with a number of other AWS services, such as: AWS Batch, Data Pipeline and CloudFormation, Amazon EMR, ECS and EKS.

To use Spot Instances, you create a Spot Instance request that includes the number of instances, the instance type, the Availability Zone, and the maximum price that you are willing to pay per instance hour. If your maximum price exceeds the current Spot price, Amazon EC2 fulfills your request immediately if capacity is available. Otherwise, Amazon EC2 waits until your request can be fulfilled or until you cancel the request.

.. figure:: /ec2_d/spot_lifecycle.png
	:align: center

	Spot instance lifecycle 

You can specify whether Amazon EC2 should hibernate, stop, or terminate Spot Instances when they are interrupted. You can choose the interruption behavior that meets your needs.

Take note that there is no "bid price" anymore for Spot EC2 instances since March 2018. You simply have to set your maximum price instead.

If your Spot instance is terminated or stopped by Amazon EC2 in the first instance hour, you will not be charged for that usage. However, if you terminate the instance yourself, you will be charged to the nearest second. If the Spot instance is terminated or stopped by Amazon EC2 in any subsequent hour, you will be charged for your usage to the nearest second. If you are running on Windows and you terminate the instance yourself, you will be charged for an entire hour.

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

Considerations
**************

Amazon EC2 has a soft limit of 20 instances per region, which can be easily resolved by completing the Amazon EC2 instance request form where your use case and your instance increase will be considered. Limit increases are tied to the region they were requested for.


`Resource Locations <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resources.html>`_


For all new AWS accounts, 20 instances are allowed per region. However, you can increase this limit by requesting it via AWS support.

Instances within a VPC with a public address have that address released when it is stopped and are reassigned a new IP when restarted.

All EC2 instances in the default VPC have both a public and private IP address.

.. list-table:: EC2-Classic vs Default VPC vs Nondefault VPC
   :widths: 20 30 30 30
   :header-rows: 1
   :stub-columns: 1

   * - Characteristic  
     - EC2-Classic 
     - Default VPC 
     - Nondefault VPC
   * - Public IPv4 address (from Amazon's public IP address pool)
     - Your instance receives a public IPv4 address from the EC2-Classic public IPv4 address pool.
     - Your instance launched in a default subnet receives a public IPv4 address by default, unless you specify otherwise during launch, or you modify the subnet's public IPv4 address attribute.
     - Your instance doesn't receive a public IPv4 address by default, unless you specify otherwise during launch, or you modify the subnet's public IPv4 address attribute.
   * - Private IPv4 address
     - Your instance receives a private IPv4 address from the EC2-Classic range each time it's started.
     - Your instance receives a static private IPv4 address from the address range of your default VPC.
     - Your instance receives a static private IPv4 address from the address range of your VPC.
   * - Multiple private IPv4 addresses
     - We select a single private IP address for your instance; multiple IP addresses are not supported.
     - You can assign multiple private IPv4 addresses to your instance.
     - You can assign multiple private IPv4 addresses to your instance.
   * - Elastic IP address (IPv4)
     - An Elastic IP is disassociated from your instance when you stop it.
     - An Elastic IP remains associated with your instance when you stop it.
     - An Elastic IP remains associated with your instance when you stop it.


