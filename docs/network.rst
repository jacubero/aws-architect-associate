Networking in AWS
#################

Design and implement AWS networks
*********************************

.. _secVPC:

Amazon Virtual Private Cloud (VPC)
==================================

A VPC can span multiple AZs inside of a region. The subnets that you create within the VPC are going to bound to an AZ. You can have multiple subnets inside an AZ. You cannot define a VPC that goes beyond a region, but there are ways that allows you to communicate different VPCs.

VPC IP addressing
-----------------

The VPC IP addressing can be either in IPv4 and IPv6. The IPv4 address can be choosen by the customer but the IPv6 address is chosen from AWS range as a ``/56`` and the customer can define ``/64`` subnets inside these ``/56`` global address. 

Each one of the EC2 instances that you launch has an IPv4 address and optionally can have an IPv6 address. What cannot happen is that an EC2 instance has only an IPv6 address, it must have an IPv4 address. As a consequence, the IPv6 addresses within an ``/56`` subnet has to have an associated IPv4 address.

When you create a VPC, you must specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, ``10.0.0.0/16``. This is the primary CIDR block for your VPC. To add a CIDR block to your VPC, the following rules apply:

* The VPC block size is between a ``/16`` netmask (65536 IP addresses) and ``/28`` netmask (16 IP addresses). 

* The CIDR block must not overlap with any existing CIDR block that's associated with the VPC.

* You cannot increase or decrease the size of an existing CIDR block once it is created.

* After you've created your VPC, you can associate secondary CIDR blocks with the VPC. You can have a maximum of 6 CIDR blocks per VPC. You have a limit on the number of routes you can add to a route table. You cannot associate a CIDR block if this results in you exceeding your limits.

* The CIDR block must not be the same or larger than the CIDR range of a route in any of the VPC route tables. For example, if you have a route with a destination of 10.0.0.0/24 to a virtual private gateway, you cannot associate a CIDR block of the same range or larger. However, you can associate a CIDR block of 10.0.0.0/25 or smaller.

* Within these blocks, you can create subnets, that can be public or private. The IP address that you use determine that if it possible to make it publicly routable. You should create subnets with a publicly routable CIDR block that falls outside of the private IPv4 address ranges specified in RFC 1918.

* When you create a subnet with an IP address range within the VPC CIDR blocks, there are some reserved IPs addresses that the customer cannot use. They are the +0,+1,+2,+3 of the subnet together with the broadcast address of the subnet. For example, for the IPv4 range ``10.0.0.0/24`` they would be:

* ``10.0.0.0`` as the network address.

* ``10.0.0.1`` for the VPC router.

* ``10.0.0.2`` for the DNS server. For VPCs with multiple CIDR blocks, the IP address of the DNS server is located in the primary CIDR. AWS also reserve the base of each subnet range plus two for all CIDR blocks in the VPC. 

* ``10.0.0.3`` for future use.

* ``10.0.0.255``: Network broadcast address. AWS do not support broadcast in a VPC.
 
To calculate the total number of IP addresses of a given CIDR Block, you simply need to follow the 2 easy steps below. Let's say you have a CIDR block /27: 

1. Subtract 32 with the mask number :  :math:`(32 - 27) = 5`

2. Raise the number 2 to the power of the answer in Step 1 : :math:`2^5 = 32`

The answer to Step 2 is the total number of IP addresses available in the given CIDR netmask. Don't forget that in AWS, the first 4 IP addresses and the last IP address in each subnet CIDR block are not available for you to use, and cannot be assigned to an instance.

IPv6 addressing
---------------

If you want to use IPv6 addresses in EC2 instances, it is necessary to work as dual stack, as you cannot disable IPv4 support for your VPC and subnets. The amount of IPv6 addresses you can use is limited by the number of IPv4 address you have.

There are 2 types of IPv6 addresses:

* **Global Unicast Address (GUA)**. AWS assignes a fixed size ``/56`` GUA per VPC which is random assigned. Each subnet that you create must have a ``/64`` range. If IPv6 is enabled, EC2 instances has a GUA automatically/manually assigned at or after launch.

* **Link Local Address (LLA)**. In IPv6 world, there are no MAC addresses and as a consequence it is no necessary to do NAT. In IPv4, NAT is needed in order to cover the shortage of available public IPv4 addresses, but in IPv6 there is no a foreseeable shortage of IPv6 addresses. LLA is also assigned to EC2 instance. It has a link-local prefix: ``fe80::/64`` and is a modified EUI-64 format obtained through a 48-bit MAC address. The LLA is used to communicate with the VPC router and to talk with other instances only within a subnet. You cannot cross a subnet with LLAs.

Bring Your Own IP Addresses (BYOIP)
-----------------------------------

You can bring part or all of your public IPv4 address range from your on-premises network to your AWS account. You continue to own the address range, but AWS advertises it on the internet. After you bring the address range to AWS, it appears in your account as an address pool. You can create an Elastic IP address from your address pool and use it with your AWS resources, such as EC2 instances, NAT gateways, and Network Load Balancers.

.. Important::

	BYOIP is not available in all Regions.

The following requirements have to be met:

* The address range must be registered with your Regional internet registry (RIR), such as the American Registry for Internet Numbers (ARIN), Réseaux IP Européens Network Coordination Centre (RIPE), or Asia-Pacific Network Information Centre (APNIC). It must be registered to a business or institutional entity and can not be registered to an individual person.

* The most specific address range that you can specify is /24.

* You can bring each address range to one Region at a time.

* You can bring five address ranges per Region to your AWS account.

* The addresses in the IP address range must have a clean history. We might investigate the reputation of the IP address range and reserve the right to reject an IP address range if it contains an IP address that has poor reputation or is associated with malicious behavior.

* The following are supported:

* ARIN - "Direct Allocation" and "Direct Assignment" network types

* RIPE - "ALLOCATED PA", "LEGACY", and "ASSIGNED PI" allocation statuses

* APNIC – "ALLOCATED PORTABLE" and "ASSIGNED PORTABLE" allocation statuses

To ensure that only you can bring your address range to your AWS account, you must authorize Amazon to advertise the address range. You must also provide proof that you own the address range through a signed authorization message.

A Route Origin Authorization (ROA) is a cryptographic statement about your route announcements that you can create through your RIR. It contains the address range, the Autonomous System numbers (ASN) that are allowed to advertise the address range, and an expiration date. An ROA authorizes Amazon to advertise an address range under a specific AS number. However, it does not authorize your AWS account to bring the address range to AWS. To authorize your AWS account to bring an address range to AWS, you must publish a self-signed X509 certificate in the Registry Data Access Protocol (RDAP) remarks for the address range. The certificate contains a public key, which AWS uses to verify the authorization-context signature that you provide. You should keep your private key secure and use it to sign the authorization-context message.

VPC DHCP
--------

It is not supported to use an specific DHCP that you provide, you have to use the DHCP given by AWS. You need to configure the DHCP options set as show below and attach it to your VPC.

.. figure:: /network_d/dhcp_options.png
   :align: center

	 DHCP options set

If you want to change the DCHP options, the only way to do it is by creating a new DHCP options set and attach it to the VPC. You cannot change a DHCP options set when it is live.

The *Domain name* is the name you will like to have inside your EC2 instance, completing unqualified DNS hostnames. In *Domain name servers* field you can include up to 4 Domain name servers to be configured in the VPC instances. In AWS, there are some DNS servers available. You can use up to 4 *NTP servers*.

When you want to do a DNS request from an instance, you can query the ``+2`` IP address of the subnet to which it belongs to. Another way to do a DNS request is by querying ``169.254.169.253`` which proxies to the ``+2`` DNS resolver.

There are no DNS hostnames automatically assigned for IPv6 addresses. When you launch a EC2 instance you get automatically a private DNS hostname with this form:

.. code-block:: console

	ip-private-ipv4-address.region.compute.internal

And optionally a public DNS hostname with this form:

.. code-block:: console

	ec2-public-ipv4-address.region.amazonaws.com

Security groups
---------------

Security groups are stateful firewalls. When an EC2 instance talk to another EC2 instance needs to create an entry in the connections table in order to cross the stateful firewall. It will look at the outbound rules of the EC2 instance initiating the connection and look at the inbound rules of the EC2 instances receiving the connection. If both the outbound rules of the source EC2 and the inbound rules of the destination EC2 allows the connection, then it is established. When the response from this connection comes back to the firewall, it is allowed.

Suppose you have a VPC as illustred below. Initially, we could think that if we want ELB Frontend to communicate with the web frontend servers, we need to know ELB IP address, which can change dynamically. Analogously, we have the same situation between the Web Frontend and the Back end servers. 

.. figure:: /network_d/sgs.png
   :align: center

	 Example of AWS VPC with 3 security groups

The correct way to deal with these scenarios is by tiering security groups. The ``sg_ELB_Frontend`` allow traffic from any IP address via HTTPS. The ``sg_Web_Frontend`` allow traffic from only from ELB_Frontend via port 8443 by using the ``sg_ELB_Frontend`` ID as the source in the security group.

.. figure:: /network_d/tierings.png
   :align: center

	 Tiering security groups

.. figure:: /network_d/elbsg.png
   :align: center

	 ELB Frontend security group

.. figure:: /network_d/websg.png
   :align: center

	 Web Frontend security group

The *Port* field can be a number or a range (for example: 1000-2000). You cannot define Ports separated by commas (for example: 1000,1001,1002). Instead, you have to define different rules for each of this ports and define a range of addresses if they are contiguous. 

A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. When you launch an instance in a VPC, You can have a maximum of 120 (60 inbound and 60 outbound) rules per security group and up to 5 security groups attached to each network interface of the EC2 instance. Security groups act at the instance level, not the subnet level. Therefore, each instance in a subnet in your VPC could be assigned to a different set of security groups. If you don't specify a particular group at launch time, the instance is automatically assigned to the default security group for the VPC. 

Network ACLs
------------

A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. Network ACLs are stateless firewall rules. If you have a client that wants to communicate with an EC2 instance within a subnet in which the NACLs applied, some inbound rules allowing this traffic need to be present. When the EC2 replies, the outbound rules of the NACLs applied as well because it is a stateless firewall. As the response can use ephemeral ports, the outbound rules should allow all ports. 

With NACLs, you can define ALLOW and DENY rules. The default ACLs allow all traffic in and all traffic out. Most customers use NACLs rules with DENY. In security groups, there are no ALLOW, if it is not allowed, is denied by default. They have a rule number that defines the priority, that is, the order in which they are applied. Network ACL Rules are evaluated by rule number, from lowest to highest, and executed immediately when a matching allow/deny rule is found.

The following are the basic things that you need to know about network ACLs:

* Your VPC automatically comes with a modifiable default network ACL. By default, it allows all inbound and outbound IPv4 traffic and, if applicable, IPv6 traffic.

* You can create a custom network ACL and associate it with a subnet. By default, each custom network ACL denies all inbound and outbound traffic until you add rules.

* Each subnet in your VPC must be associated with a network ACL. If you don't explicitly associate a subnet with a network ACL, the subnet is automatically associated with the default network ACL.

* You can associate a network ACL with multiple subnets; however, a subnet can be associated with only one network ACL at a time. When you associate a network ACL with a subnet, the previous association is removed.

* A network ACL contains a numbered list of rules that we evaluate in order, starting with the lowest numbered rule, to determine whether traffic is allowed in or out of any subnet associated with the network ACL. The highest number that you can use for a rule is 32766. We recommend that you start by creating rules in increments (for example, increments of 10 or 100) so that you can insert new rules where you need to later on.

* A network ACL has separate inbound and outbound rules, and each rule can either allow or deny traffic.

* Network ACLs are stateless; responses to allowed inbound traffic are subject to the rules for outbound traffic (and vice versa).

`AWS re:Invent 2018: Your Virtual Data Center: VPC Fundamentals and Connectivity Options (NET201) <https://www.youtube.com/watch?time_continue=1&v=jZAvKgqlrjY&feature=emb_logo>`_

Amazon VPC: Route tables and gateways
=====================================

VPC subnets route table
-----------------------

The route tables allows you to route to some gateway. The route table get applied to router of the subnet itself (+1 of the subnet itself). The default gateway of the EC2 instance (``0.0.0.0/0``) always will be pointing to the router of the subnet. In this router, you will have a route table with an entry with destination the VPC CIDR blocks and the target local. Local means that you can route to every resource in the VPC. The local entry in the route table has priority over the rest of the routes. The other entry in the route table has a destination ``0.0.0.0/0`` and target the internet gateway. The **internet gateway** allow an EC2 instance to route traffic to Internet or any resource in the Internet route traffic to the EC2 instance.

.. figure:: /network_d/igw.png
   :align: center

	 Example of a route table

VPC: Gateways
-------------

A **NAT gateway** is a managed address translation gateway. 

IPv6 addresses on EC2 instances are public addresses, so that if we connect them to internet gateway there would be reachable from Internet. The **egress-only internet gateway** is a gateway for IPv6 only, that allows EC2 instances with IPv6 addresses to reach Internet, but they are not reachable from Internet.

VPC Routing: Public subnet
--------------------------

What makes a subnet public is its route table. It has an entry with destination ``0.0.0.0/0`` and target the Internet Gateway. You would need a public IP address attached to the network interface of EC2 instance in this subnet. The packets coming from the EC2 instance to the Internet Gateway have a private IP address and they are translated to the public IP address attached to it thanks to the Internet Gateway.

.. figure:: /network_d/publics.png
   :align: center

	  Example of public subnet route table

You do not need to manage the Internet Gateway. It scales out or in depending on the amount the traffic it has to handle. The maximum throughtput it can support is 5Gbps.

To enable access to or from the Internet for instances in a VPC subnet, you must do the following:

* Attach an internet gateway to your VPC.

* Ensure that your subnet's route table points to the Internet gateway.

* Ensure that instances in your subnet have a globally unique IP address (public IPv4 address, Elastic IP address, or IPv6 address).

* Ensure that your network access control lists and security groups allow the relevant traffic to flow to and from your instance.

VPC Routing: Private subnet
---------------------------

If an EC2 in a private subnet wants to communicate to the Internet, this subnet needs to be attached to a NAT gateway which lives in a public subnet. There is an entry in the route table in which the destination is ``0.0.0.0/0`` ad the target is the NAT gateway. 

.. figure:: /network_d/privates.png
   :align: center

	  Example of private subnet route table

The NAT gateway allows the EC2 with a private address to reach the Internet but the EC2 instance is not reachable from the Internet. The NAT gateway requires an Elastic IP address that will be used to translate the private address of the EC2 instance. Even if you are using a NAT gateway, you are still passing through an Internet Gateway to reach the Internet. You have one Internet Gateway per VPC but you can have multiple NAT gateways inside you VPC. The reason to have more than one is that they are highly available within an AZ, not across AZs. 

You can achieve HA across AZs by launching a NAT gateway in each AZ. If one AZ is down, all subnets associated to that AZ are down. If you have high availability, you would have multiple subnets spanning multiple zones: each zone's private subnets would point to a NAT Gateway in that zone's public subnet, with separate routing tables for each zone.

A NAT gateway separate subnets and can scale up to 45 Gbps. There is a limit of 55000 connections towards the same destination. If you need more thant 45 Gbps or more than 55000 connections towards the same destination, then you will need more than one NAT gateway. In that case, you will need another subnet with a different route table that will point towards the second NAT gateway.

NAT gateway hourly usage and data processing rates apply. Amazon EC2 charges for data transfer also apply. NAT gateways are not supported for IPv6 traffic—use an egress-only internet gateway instead.

To create a NAT gateway, you must specify the public subnet in which the NAT gateway should reside. You must also specify an Elastic IP address to associate with the NAT gateway when you create it. The Elastic IP address cannot be changed once you associate it with the NAT Gateway.

After you've created a NAT gateway, you must update the route table associated with one or more of your private subnets to point Internet-bound traffic to the NAT gateway. This enables instances in your private subnets to communicate with the internet. Each NAT gateway is created in a specific Availability Zone and implemented with redundancy in that zone. You have a limit on the number of NAT gateways you can create in an Availability Zone.

AWS offers two kinds of NAT devices: a NAT gateway or a NAT instance. It is recommended to use NAT gateways, as they provide better availability and bandwidth over NAT instances. The NAT Gateway service is also a managed service that does not require your administration efforts. A NAT instance is launched from a NAT AMI.

Here is a diagram showing the differences between NAT gateway and NAT instance:

.. figure:: /network_d/Natcomparison.jpg
   :align: center

	  NAT gateway vs NAT instance

EC2 instance as in-line next-hop
--------------------------------

If you want to implement you own NAT gateway or IDS or IPS, ... by using an EC2 instance, then you will need to use it as in-line next-hop. There are several methods to implement it.

Method 1
^^^^^^^^

You will need to define an entry in the route table with destination ``0.0.0.0/0`` and the target is an ENI (Elastic Network Interface) of an EC2 instance within a public subnet. This EC2 instance has reachability to the Internet via an Internet Gateway.

.. figure:: /network_d/m1.png
   :align: center

	  EC2 instance as in-line next-hop: Method 1

The responsible for translating the private address of the EC2 to the public address is the Internet Gateway. 

Method 2
^^^^^^^^

Another method is to configure a route inside the EC2 and redirects it to another EC2 instance inside the same subnet. The latter EC2 instance sends the traffic to the default gateway (``+1`` of subnet network) and its route table has the entry for destination ``0.0.0.0/0`` pointing to the Internet Gateway. The responsible for translating the private address of the EC2 to the public address is the Internet Gateway. 

.. figure:: /network_d/m2.png
   :align: center

	  EC2 instance as in-line next-hop: Method 2

VPC endpoints for AWS services
------------------------------

It allows to communicate with some services directly within your VPC. There are two types of VPC: interface and gateway.

.. list-table:: VPC endpoints for AWS services
    :widths: 30 35 35 
    :header-rows: 1

    * - Endpoint Type

      - Description

      - Supported Services

    * - Interface (powered by PrivateLink)

      - An elastic network interface with a private IP address that serves as an entry point for the traffic destinaed to a supported AWS service.

      - Amazon Kinesis, Elastic Load Balancing API, Amazon EC2 API, AWS Systems Manager, AWS Service Catalog, Amazon SNS, AWS SNS. 

    * - Gateway

      - A gateway that is a target for a specified route in your route table, used for traffic destined to a supported AWS service.

      - Amazon S3, Amazon DynamoDB. 

The characteristics of an **Interface VPC endpoint** are the following:

* There is one interface per AZ. It is an ENI from an EC2 instance which lives in an AZ.

* It does not support endpoint policies.

* You can apply a security group.

* You access over AWS Direct Connect, but no through AWS VPN.

* It makes requests to the service using endpoint-specific DNS hostnames. Optionally, you can use Amazon Route 53 DNS private hosted zone to make requests to the service using its default public DNS name.

.. Note:: Privatelink

	Privatelink is a purpose-built technology desgined to access AWS services, while keeping all the network traffic within the AWS network. There is no need for proxies, NAT gateways or Internet Gateways.

The characteristics of an **Gateway VPC endpoint** are the following:

* It supports multiple AZs.

* It supports the use of endpoint policies.

* It cannot be accessed neither over AWS Direct Connect nor over VPN.

* It makes requests to the service using its default public DNS name.

An example of creating an Amazon S3 VPC endpoint is the following:

.. code-block:: console

  $ aws ec2 create-vpc-endpoint --vpc-id vpc-40f18d25 --service-name com.amazonaws.us-west-2.s3 --route-table-ids rtb-2ae6a24f

You need an entry in the route table with destination the prefix list for the S3 endpoint and the target the VPC endpoint. 

.. figure:: /network_d/s3VPCep.png
   :align: center

	  Creating an Amazon S3 VPC endpoint

That prefix list is built by AWS. It is a logical route destination target that dynamically translates to service IPs. Amazon S3 IP ranges change over time and Amazon S3 prefix lists abstract change.

.. code-block:: console

	$ aws ec2 describe-prefix-lists

	{
	"PrefixLists": [
	  {
	    "PrefixListName": "com.amazonaws.us-east-1.s3",
	    "Cidrs": [
	      "54.231.0.0/17"
	    ],
	    "PrefixListId": "pl-63a5400a"
	  }
	]
	}

The VPC endpoint policy allows you to control VPC access to Amazon S3. An example could be the following:

.. code-block:: JSON

	{
	"Statement": [
	  {
	    "Sid": "vpce-restrict-to-my_secure_bucket",
	    "Principal": "*",
	    "Action": [
	      "s3:GetObject",
	      "s3:PutObject"
	    ],
	    "Effect": "Allow",
	    "Resource": ["arn:aws:s3:::my_secure_bucket",
	                 "arn:aws:s3:::my_secure_bucket/*"]
	  }
	]
	}	

Having a VPC endpoint policy in place does not mean that you have access to a bucket. There are bucket policy that can allow or deny access to it. For instance, you can restrict that the bucket must be accesible only from the S3 VPC endpoint:

.. code-block:: JSON

	{
	  "Version":"2012-10-17",
	  "Statement":[
	    {
	      "Sid":"bucket-restrict-to-specific-vpce",
	      "Principal": "*", 
	      "Action":"s3:*",
	      "Effect":"Deny",
	      "Resource":["arn:aws:s3:::my_secure_bucket",
                     "arn:aws:s3:::my_secure_bucket/*"],
	      "Condition":{"StringNotEquals":{"aws:sourceVpce":["vpce-bc42a4e5"]}}
	    }
	  ]
	}

As a summary, you can control VPC access to Amazon S3 via several security layers:

1. Route table association.

2. VPC endpoint policy.

3. Bucket policy.

4. EC2 security groups with prefix list.

.. figure:: /network_d/layersv.png
   :align: center

	  Controlling VPC access to Amazon S3

.. Note:: Prefix list.
	You can use prefix list with security groups but not with NACLs.

Amazon EC2 networking
=====================

Elastic network interface
-------------------------

An elastic network interface (ENI) is a logical networking component in a VPC that represents a virtual network card. You can attach a network interface to an EC2 instance in the following ways:

* When it's running (hot attach).

* When it's stopped (warm attach).

* When the instance is being launched (cold attach).

You always have an ENI attached to an instance, it is the default ENI and cannot be modified. You can attach more than one ENI to an EC2 instance and they can be moved to another EC2 instance. In general, the ENIs of an EC2 instance are attached to different subnets. Each ENI have a private IP address and a public IP address, optionally you can have up to 4 private IP addresses and 4 public IP addresses.

.. figure:: /network_d/eniv.png
   :align: center

	  Elastic network interface

The ENIs will be attached to different VPC subnets in the same AZ. The ENIs are used to talk among EC2 instances but also between an EC2 instance and an EBS volume. Some EC2 instance types support EBS optimized dedicated throughput, which allows you to have dedicated throughtput to access an ENS volume.  

.. figure:: /network_d/dedicatedi.png
   :align: center

	  EC2 instance types supporting EBS-optimized dedicated throughput

If we need to optimize network performance between 2 EC2 instances, the supported throughput is based on the instace type.

.. figure:: /network_d/perform.png
   :align: center

	  Instance sizing: burstable network performance

The 25 Gigabit and 10 Gigabit performance is measured one way. you have to double that for birdirectional (full duplex). Sometimes the Amazon EC2 network performance is classified as high, moderate or low. It is a function of the instance size, but not all instances are created equal, so it is recommended to test it with iperf or another network performance measurement tool. Burstable network performance are defined in C5, I3 and R4 EC2 instance types. It is supported 5 GB maximum per instance on egress traffic destined outside the VPC. You can go above the 5 GB by using placement groups or VPC endpoints.  

Enhanced networking
-------------------

There are 3 main strategies to get towards the 25 Gbps: Device pass-through, Elastic Network Adapter (ENA) and Intel Data Plane Development Kit (DPDK).

Device pass-through
^^^^^^^^^^^^^^^^^^^

In virtualization, single root input/output virtualization or SR-IOV is a specification that allows the isolation of the PCI Express resources for manageability. It allows PCIe devices to appear as multiple separate physical PCIe devices using Virtual Functions (VF). It provides higher bandwidth, higher packet per second (PPS) performance, and consistently lower inter-instance latencies. Enhanced networking requires a specialized driver, which means:

* Your instance OS must know about it.

* Amazon EC2 must be notified that your instance can use it.

Elastic Network Adapter (ENA)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is the next generation of enhanced networking that supports HW checksums, multi-queue, receive side steering. It can achieve 25 Gbps of throuhput in a placement group. It is an open-source Amazon network driver. There are items for advanced tuning:

* Multiple Tx/Rx queue pairs (the maximum number is advertised by the device through the administration queue).

* CPU cache line optimizes data placement.

* Chacksum offload and TCP transmit segmentation offload (TSO).

* Support for receive-side scaling (RSS) for multi-core scaling.

* Depending on ENA device, support for low-latency queue (LLQ), which saves more microseconds.

.. figure:: /network_d/ena.png
   :align: center

	  Enable the ENA to an EC2 instance

An Elastic Fabric Adapter (EFA) is simply an Elastic Network Adapter (ENA) with added capabilities. It provides all of the functionality of an ENA, with additional OS-bypass functionality. OS-bypass is an access model that allows HPC and machine learning applications to communicate directly with the network interface hardware to provide low-latency, reliable transport functionality.

The OS-bypass capabilities of EFAs are not supported on Windows instances. If you attach an EFA to a Windows instance, the instance functions as an Elastic Network Adapter, without the added EFA capabilities.

Intel Data Plane Development Kit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is a set of libraries and drivers for fast packet processing. It is supported for both the Intel 82599 Virtual Interface and the ENA driver. It is a software accelerator that runs in user space, bypassing the Linux kernel and providing access to NICs, CPUs, and memory for a packet processing application. The DPDK can:

* Receive and send packets within the minimum number of CPU cycles (usually fewer than 80 cycles).

* Develop fast capture algorithms (tcpdump-like)

* Run third-party fast path stacks.

There are some use cases: firewalls, real-time communication processing, HPC, and network appliances. 

Placement groups
----------------

When you want a group of EC2 instances to talk very fast and with high throughtput, you may need to include them inside placement groups. 

When you launch EC2 instances in the same AZ, it doesn't mean that they are going to be in the same data center. An AZ can have more than one data center. To force the EC2 instances to be very close (perhaps in the same rack) and allows you to have full Amazon EC2 bandwidth.

Use placement groups when you need high, consisteng instance-to-instance bandwidth. The maximum network throughput is limited by the slower of the two instances. A placement group can span peered VPCs in the same region (may not get full bi-section bandwidth). It can launch multiple instance types into a placement group. All traffic is limited to 5 Gb/s when exiting VPC.

It is recommended not to have different instance types in a placement group because it is more difficult to launched them very close among them.

Jumbo frames
------------

An standard frame in AWS has a MTU of 1522. It means that your payload has 1522 bytes and the overhead is quite big. In Jumbo frames, what allows you to do is allocate more capacity for the payload (9001 bytes) and a smaller overhead.

.. figure:: /network_d/jumbof.png
   :align: center

	  Jumbo frames

Every single device in between the EC2 instances must support 9001 MTU, which is not going to work when you go out the Internet. It is supported inside VPCs, but if you go through a Virtual Private Gateway or a VPN gateway, then it is not supported.

.. Note:: 
	Enable the ICMP message Type 3, Code 4 (Destination Unreachable: fragmentation needed and don't fragment set). This setting instructs the original host to adjust the MTU until the packet can be transmitted.

Multicast
---------

Multicast is a network capability that allows one-to-many distribution of data. With multicasting, one or more sources can transmit network packets to subscribers that typically reside within a multicast group. However, take note that Amazon VPC does not support multicast or broadcast networking.

If you need multicast, then you can use an overlay multicast. An overlay multicast is a method of building IP level multicast across a network fabric supporting unicast IP routing, such as Amazon Virtual Private Cloud (Amazon VPC).

Design and implement hybrid IT network architects ad scale
**********************************************************

In AWS. there are 3 connectivity options: 

* **Public Internet**, via public IPs or elastic IPs, taking into account that traffic out is charged by AWS.

* **VPN**, using IPSec authentication and encryption. It has 2 primary options: AWS managed VPN nad software VPN (Amazon EC2).

* **AWS Direct Connect**, which establishes a private connection with AWS, separate from the Internet. It allows you to have a consistent network experience and the ability to connect through many locations globally. You can have sub-1Gps, 1Gps, 10Gps options.

Depending on the requirements (security, cost, management) that you customer has, the possible options could be different.

Virtual Private Networks
========================

There are mainly 2 types of VPN: site-to-site VPN and client-to-site VPN. In site-to-site VPN, you are connecting the corporate data center over the Internet towards my VPC. In the client-to-site VPN, you have users that use VPN clients to EC2 instances.

Site-to-site VPN
----------------

There are two options of site-to-site VPN:

* Terminating the VPN connection in a **VPN Gatewway (VGW)**, which is an AWS managed service that only supports IPSec protocol to setup VPNs.

* Terminating the VPN connection in 2 endpoints (for HA) on top EC2 instances.

A VGW is a fully managed gateway endpoint for your VPC with built-in multiple AZ HA. You only can have 1 VGW per VPC. It is responsible for hybrid IT connectivity, using VPN and AWS Direct Connect. It is self-sustainable entity that can be created without the requirement of a preexisiting VPC (that is, it can run in detached mode). You have the ability to:

* Attach to nay VPC in the same account and AWS region.

* Detach one VGW and attach another one to a VPC.

* Choose ASN at creation (BYO-ASN).

.. figure:: /network_d/vpngw.png
   :align: center

	 Extample of VPN connection

In the previous example, the IP addressing of the corporate data center is ``192.168.1.0/24``. In the route table, we can notice that the ``192.168.1.0/24`` has not been propagated so it has to be manually configured and not learned via BGP routing protocol.

You get 2 public IP addresses with a VGW that are across 2 different service providers. The customer gateway located in the corporate data center has only 1 IP address and you have to establish more than 1 VPN connections, unless it is redundant in different service providers. You need to establish 2 IPSec tunnels towards AWS per VGW connection because you 2 endpoints with different IP addresses. You can specify the preshared key of each one of the 2 IPSec tunnels and you can also specify the inside tunnel IP in between the two sides of the VPN.

.. figure:: /network_d/vgwred.png
   :align: center

	 VPN redundancy

As you have 2 tunnels, there is a risk of asymmetric routing. To avoid it and prevents to send traffic from one path and not getting it returned to the other path, you can use BGP with one of these 2 options:

* Prepend an AS path.

* Set the multi-exit discriminator (MED) attribute.

.. figure:: /network_d/asym.png
   :align: center

	 Avoid asymmetric routing

You can connect from different data centers into the same VGW. One of the features of VGW is that you can use as a CloudHub. AWS VPN CloudHub is an AWS functionality, you only need to establish 2 VPN connections and by doing that you will able to use this CloudHub to send traffic between the 2 corporate data centers and there is no need to have direct connection between the two.

.. figure:: /network_d/cloudhub.png
   :align: center

	 AWS VPN CloudHub

VGW doesn't initiate IPSec negotiation. AWS uses an on-demand DPD mechanism so that:

* If AWS receives no traffic from a VPN peer for 10 seconds, AWS sends a DPD "R-U-THERE" message.

* If the VPN peer does not respond to 3 successive DPDs, the VPN peer is considered dead and AWS closes the tunnel.

Static VPN (policy-based VPN) is limited to one unique security association (SA) pair per tunnel (one inbound and one outbound). Instead, you should:

* Limit the number of encryption domains (networks) that are allowed access to the VPC and consolidate.

* Configure the policy to allow "any" network (``0.0.0.0/0``) from behind your VPN termination endpoint to the VPC CIDR.

Monitoring
^^^^^^^^^^

You can monitor VPN tunnels using CloudWatch, which collects and processes raw data from the VPN service into readable, near real-time metrics. These statistics are recorded for a period of 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. VPN metric data is automatically sent to CloudWatch as it becomes available. The following metrics are available for your VPN tunnels:

* ``TunnelState``. The state of the tunnel. For static VPNs, 0 indicates DOWN and 1 indicates UP. For BGP VPNs, 1 indicates ESTABLISHED and 0 is used for all other states.

* ``TunnelDataIn``. The bytes received through the VPN tunnel. Each metric data point represents the number of bytes received after the previous data point. Use the Sum statistic to show the total number of bytes received during the period. This metric counts the data after decryption.

* ``TunnelDataOut``. The bytes sent through the VPN tunnel. Each metric data point represents the number of bytes sent after the previous data point. Use the Sum statistic to show the total number of bytes sent during the period. This metric counts the data before encryption.

Connecting networks
*******************

VPC peering connection
======================

A VPC peering connection is a network connection between two VPCs that enables you to route traffic between them using private IP addresses. Instances in either VPC can communicate with each other as if they are within the same network. You can create a VPC peering connection between your own VPCs, with a VPC in another AWS account, or with a VPC in a different AWS Region.

.. figure:: /network_d/peering-intro-diagram.png
   :align: center

	 VPC peering connection

AWS uses the existing infrastructure of a VPC to create a VPC peering connection; it is neither a gateway nor a VPN connection, and does not rely on a separate piece of physical hardware. There is no single point of failure for communication or a bandwidth bottleneck.

`AWS Knowledge Center Videos: "What is VPC Peering?" <https://www.youtube.com/watch?v=i1A1eH8vLtk&feature=emb_logo>`_

The following VPC peering connection configurations are not supported.

* Overlapping CIDR Blocks.

* Transitive Peering.

* Edge to Edge Routing Through a Gateway or Private Connection.

Overlapping CIDR Blocks
-----------------------

You cannot create a VPC peering connection between VPCs with matching or overlapping IPv4 CIDR blocks.

.. figure:: /network_d/overlapping-cidrs-diagram.png
   :align: center

	 Overlapping CIDR Blocks

If the VPCs have multiple IPv4 CIDR blocks, you cannot create a VPC peering connection if any of the CIDR blocks overlap (regardless of whether you intend to use the VPC peering connection for communication between the non-overlapping CIDR blocks only). 

.. figure:: /network_d/overlapping-multiple-cidrs-diagram.png
   :align: center

	 Overlapping CIDR Blocks

This limitation also applies to VPCs that have non-overlapping IPv6 CIDR blocks. Even if you intend to use the VPC peering connection for IPv6 communication only, you cannot create a VPC peering connection if the VPCs have matching or overlapping IPv4 CIDR blocks. Communication over IPv6 is not supported for an inter-region VPC peering connection.

Transitive Peering
------------------

You have a VPC peering connection between VPC A and VPC B (pcx-aaaabbbb), and between VPC A and VPC C (pcx-aaaacccc). There is no VPC peering connection between VPC B and VPC C. You cannot route packets directly from VPC B to VPC C through VPC A.

.. figure:: /network_d/transitive-peering-diagram.png
   :align: center

	 Transitive Peering

Edge to Edge Routing Through a Gateway or Private Connection
------------------------------------------------------------

If either VPC in a peering relationship has one of the following connections, you cannot extend the peering relationship to that connection:

* A VPN connection or an AWS Direct Connect connection to a corporate network.

* An Internet connection through an Internet gateway.

* An Internet connection in a private subnet through a NAT device.

* A VPC endpoint to an AWS service; for example, an endpoint to Amazon S3.

* (IPv6) A ClassicLink connection. You can enable IPv4 communication between a linked EC2-Classic instance and instances in a VPC on the other side of a VPC peering connection. However, IPv6 is not supported in EC2-Classic, so you cannot extend this connection for IPv6 communication.

.. figure:: /network_d/transitive-peering-diagram.png
   :align: center

	 VPC peering connection

For example, if VPC A and VPC B are peered, and VPC A has any of these connections, then instances in VPC B cannot use the connection to access resources on the other side of the connection. Similarly, resources on the other side of a connection cannot use the connection to access VPC B.

`AWS re:Invent 2018: AWS Direct Connect: Deep Dive (NET403) <https://www.youtube.com/watch?v=DXFooR95BYc&feature=emb_logo>`_

Bastion hosts
=============

The best way to implement a bastion host is to create a small EC2 instance which should only have a security group from a particular IP address for maximum security. This will block any SSH Brute Force attacks on your bastion host. It is also recommended to use a small instance rather than a large one because this host will only act as a jump server to connect to other instances in your VPC and nothing else.

.. figure:: /network_d/linux-bastion-hosts-on-aws-architecture.png
   :align: center

	 Bastion hosts

Elastic Load Balancing (ELB)
****************************

In Elastic Load Balancing, there are various security features that you can use such as Server Order Preference, Predefined Security Policy, Perfect Forward Secrecy and many others. 

Perfect Forward Secrecy is a feature that provides additional safeguards against the eavesdropping of encrypted data through the use of a unique random session key. This prevents the decoding of captured data, even if the secret long-term key is compromised. Perfect Forward Secrecy is used to offer SSL/TLS cipher suites for CloudFront and Elastic Load Balancing.

Elastic Load Balancing supports three types of load balancers. You can select the appropriate load balancer based on your application needs.

If you need flexible application management and TLS termination then we recommend that you use Application Load Balancer. If extreme performance and static IP is needed for your application then we recommend that you use Network Load Balancer. If your application is built within the EC2 Classic network then you should use Classic Load Balancer.

Classic Load Balancers 
----------------------

Connection draining
^^^^^^^^^^^^^^^^^^^

To ensure that a Classic Load Balancer stops sending requests to instances that are de-registering or unhealthy while keeping the existing connections open, use connection draining. This enables the load balancer to complete in-flight requests made to instances that are de-registering or unhealthy. 

When you enable connection draining, you can specify a maximum time for the load balancer to keep connections alive before reporting the instance as de-registered. The maximum timeout value can be set between 1 and 3,600 seconds (the default is 300 seconds). When the maximum time limit is reached, the load balancer forcibly closes connections to the de-registering instance.

Sticky sessions
^^^^^^^^^^^^^^^

By default, a Classic Load Balancer routes each request independently to the registered instance with the smallest load. However, you can use the sticky session feature (also known as session affinity), which enables the load balancer to bind a user's session to a specific instance. This ensures that all requests from the user during the session are sent to the same instance.

.. figure:: /network_d/sticky.png
   :align: center

	 Sticky sessions

The key to managing sticky sessions is to determine how long your load balancer should consistently route the user's request to the same instance. If your application has its own session cookie, then you can configure Elastic Load Balancing so that the session cookie follows the duration specified. If your application does not have its own session cookie, then you can configure Elastic Load Balancing to create a session cookie by specifying your own stickiness duration.

Sticky session feature of the Classic Load Balancer can provide session management, however, take note that this feature has its limitations such as, in the event of a failure, you are likely to lose the sessions that were resident on the failed node. In the event that the number of your web servers change when your Auto Scaling kicks in, it's possible that the traffic may be unequally spread across the web servers as active sessions may exist on particular servers. If not mitigated properly, this can hinder the scalability of your applications.

Application Load Balancers 
--------------------------

An Application Load Balancer functions at the application layer, the seventh layer of the Open Systems Interconnection (OSI) model. After the load balancer receives a request, it evaluates the listener rules in priority order to determine which rule to apply, and then selects a target from the target group for the rule action. You can configure listener rules to route requests to different target groups based on the content of the application traffic. Routing is performed independently for each target group, even when a target is registered with multiple target groups.

.. figure:: /network_d/redirect_path.png
   :align: center

	 Application Load Balancer

Application Load Balancers support path-based routing, host-based routing and support for containerized applications.

Application Load Balancers support Weighted Target Groups routing. With this feature, you will be able to do weighted routing of the traffic forwarded by a rule to multiple target groups. This enables various use cases like blue-green, canary and hybrid deployments without the need for multiple load balancers. It even enables zero-downtime migration between on-premises and cloud or between different compute types like EC2 and Lambda.

.. figure:: /network_d/weighted.png
   :align: center

	 Application Load Balancers with Weighted Target Groups routing

Path conditions
^^^^^^^^^^^^^^^

You can use path conditions to define rules that forward requests to different target groups based on the URL in the request (also known as path-based routing). Each path condition has one path pattern. If the URL in a request matches the path pattern in a listener rule exactly, the request is routed using that rule. 

A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.

.. code-block:: console

	A–Z, a–z, 0–9
	_ - . $ / ~ " ' @ : +
	& (using &amp;)
	* (matches 0 or more characters)
	? (matches exactly 1 character)
	Example path patterns

	/img/*
	/js/*
 

`AWS re:Invent 2018: [REPEAT 1] Elastic Load Balancing: Deep Dive and Best Practices (NET404-R1) <https://www.youtube.com/watch?v=VIgAT7vjol8&feature=youtu.be>`_

Cross-zone load balancing
=========================

Cross-zone load balancing reduces the need to maintain equivalent numbers of instances in each enabled Availability Zone, and improves your application's ability to handle the loss of one or more instances. 

When you create a Classic Load Balancer, the default for cross-zone load balancing depends on how you create the load balancer. With the API or CLI, cross-zone load balancing is disabled by default. With the AWS Management Console, the option to enable cross-zone load balancing is selected by default. After you create a Classic Load Balancer, you can enable or disable cross-zone load balancing at any time.

The following diagrams demonstrate the effect of cross-zone load balancing. There are two enabled Availability Zones, with 2 targets in Availability Zone A and 8 targets in Availability Zone B. Clients send requests, and Amazon Route 53 responds to each request with the IP address of one of the load balancer nodes. This distributes traffic such that each load balancer node receives 50% of the traffic from the clients. Each load balancer node distributes its share of the traffic across the registered targets in its scope.

If cross-zone load balancing is enabled, each of the 10 targets receives 10% of the traffic. This is because each load balancer node can route its 50% of the client traffic to all 10 targets.

.. figure:: /network_d/cross_zone_load_balancing_enabled.png
   :align: center

	 Cross-zone load balancing enabled

If cross-zone load balancing is disabled, each of the 2 targets in Availability Zone A receives 25% of the traffic and each of the 8 targets in Availability Zone B receives 6.25% of the traffic. This is because each load balancer node can route its 50% of the client traffic only to targets in its Availability Zone.

.. figure:: /network_d/cross_zone_load_balancing_disabled.png
   :align: center

	 Cross-zone load balancing disabled

Amazon Route 53
***************

When you sign up for Route 53 the first thing you do is create a Hosted Zone. This is where your DNS data will be kept. When you do that, you receive 4 name servers where you can delegate your domain. Then you specify your Fully Qualified Domain Name, which is the domain you have purchased with a DNS registrar. This could be external, or you can use Route 53 to purchase a domain. Proxy and privacy services are options with Amazon's Route 53 registrar, allowing you to hide partial or all your information within the DNS query.

The Hosted Zone will contain record sets, which are the DNS translations you want to perform for that specific domain.

Amazon Route 53's DNS services does not support DNSSEC at this time. However, their domain name registration service supports configuration of signed DNSSEC keys for domains when DNS service is configured at another provider. More information on configuring DNSSEC for your domain name registration can be found `Configuring DNSSEC for a Domain <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-configure-dnssec.html>`_.

Amazon Route 53 currently supports the following DNS record types:

* A (address record)

* AAAA (IPv6 address record)

* CNAME (canonical name record)

* CAA (certification authority authorization)

* MX (mail exchange record)

* NAPTR (name authority pointer record)

* NS (name server record)

* PTR (pointer record)

* SOA (start of authority record)

* SPF (sender policy framework)

* SRV (service locator)

* TXT (text record)