Networking in AWS
########################################

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

VPC DHCP
--------

It is not supported to use an specific DHCP that you provide, you have to use the DHCP given by AWS. You need to configure the DHCP options set as show below and attach it to your VPC.

.. figure:: /networks_d/options.png
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

.. figure:: /networks_d/sg.png
   :align: center

	 Example of AWS VPC with 3 security groups

The correct way to deal with these scenarios is by tiering security groups. The ``sg_ELB_Frontend`` allow traffic from any IP address via HTTPS. The ``sg_Web_Frontend`` allow traffic from only from ELB_Frontend via port 8443 by using the ``sg_ELB_Frontend`` ID as the source in the security group.

.. figure:: /networks_d/tieringsg.png
   :align: center

	 Tiering security groups

.. figure:: /networks_d/elb.png
   :align: center

	 ELB Frontend security group

.. figure:: /networks_d/web.png
   :align: center

	 Web Frontend security group

The *Port* field can be a number or a range (for example: 1000-2000). You cannot define Ports separated by commas (for example: 1000,1001,1002). Instead, you have to define different rules for each of this ports and define a range of addresses if they are contiguous. You can have a maximum of 50 rules per security group and up to 5 security groups attached to each interface of the EC2 instance.

Network ACLs
------------

Network ACLs are stateless firewall rules. If you have a client that wants to communicate with an EC2 instance within a subnet in which the NACLs applied, some inbound rules allowing this traffic need to be presnt. When the EC2 replies, the outbound rules of the NACLs applied as well because it is a stateless firewall. As the response can use ephemeral ports, the outbound rules should allow all ports. 

With NACLs, you can define ALLOW and DENY rules. The default ACLs allow all traffic in and all traffic out. Most customers use NACLs rules with DENY. In security groups, there are no ALLOW, if it is not allowed, is denied by default. They have a rule number that defines the priority, that is, the order in which they are applied.

`AWS re:Invent 2018: Your Virtual Data Center: VPC Fundamentals and Connectivity Options (NET201) <https://www.youtube.com/watch?time_continue=1&v=jZAvKgqlrjY&feature=emb_logo>`_

Amazon VPC: Route tables and gateways
=====================================

VPC subnets route table
-----------------------

The route tables allows you to route to some gateway. The route table get applied to router of the subnet itself (+1 of the subnet itself). The default gateway of the EC2 instance (``0.0.0.0/0``) always will be pointing to the router of the subnet. In this router, you will have a route table with an entry with destination the VPC CIDR blocks and the target local. Local means that you can route to every resource in the VPC. The local entry in the route table has priority over the rest of the routes. The other entry in the route table has a destination ``0.0.0.0/0`` and target the internet gateway. The **internet gateway** allow an EC2 instance to route traffic to Internet or any resource in the Internet route traffic to the EC2 instance.

.. figure:: /networks_d/internetg.png
   :align: center

	 Example of a route table

VPC: Gateways
-------------

A **NAT gateway** is a managed address translation gateway. 

IPv6 addresses on EC2 instances are public addresses, so that if we connect them to internet gateway there would be reachable from Internet. The **egress-only internet gateway** is a gateway for IPv6 only, that allows EC2 instances with IPv6 addresses to reach Internet, but they are not reachable from Internet.

**VPC peering connection**

VPC Routing: Public subnet
--------------------------

What makes a subnet public is its route table. It has an entry with destination ``0.0.0.0/0`` and target the Internet Gateway. You would need a public IP address attached to the network interface of EC2 instance in this subnet. The packets coming from the EC2 instance to the Internet Gateway have a private IP address and they are translated to the public IP address attached to it thanks to the Internet Gateway.

.. figure:: /networks_d/public.png
   :align: center

	  Example of public subnet route table

You do not need to manage the Internet Gateway. It scales out or in depending on the amount the traffic it has to handle. The maximum throughtput it can support is 5Gbps.

VPC Routing: Private subnet
---------------------------

If an EC2 in a private subnet wants to communicate to the Internet, this subnet needs to be attached to a NAT gateway which lives in a public subnet. There is an entry in the route table in which the destination is ``0.0.0.0/0`` ad the target is the NAT gateway. 

.. figure:: /networks_d/private.png
   :align: center

	  Example of private subnet route table

The NAT gateway allows the EC2 with a private address to reach the Internet but the EC2 instance is not reachable from the Internet. The NAT gateway requires an Elastic IP address that will be used to translate the private address of the EC2 instance. Even if you are using a NAT gateway, you are still passing through an Internet Gateway to reach the Internet. You have one Internet Gateway per VPC but you can have multiple NAT gateways inside you VPC. The reason to have more than one is that they are highly available within an AZ, not across AZs. 

A NAT gateway separate subnets and can scale up to 45 Gbps. There is a limit of 55000 connections towards the same destination. If you need more thant 45 Gbps or more than 55000 connections towards the same destination, then you will need more than one NAT gateway. In that case, you will need another subnet with a different route table that will point towards the second NAT gateway.

EC2 instance as in-line next-hop
--------------------------------

If you want to implement you own NAT gateway or IDS or IPS, ... by using an EC2 instance, then you will need to use it as in-line next-hop. There are several methods to implement it.

Method 1
^^^^^^^^

You will need to define an entry in the route table with destination ``0.0.0.0/0`` and the target is an ENI (Elastic Network Interface) of an EC2 instance within a public subnet. This EC2 instance has reachability to the Internet via an Internet Gateway.

.. figure:: /networks_d/method1.png
   :align: center

	  EC2 instance as in-line next-hop: Method 1

The responsible for translating the private address of the EC2 to the public address is the Internet Gateway. 

Method 2
^^^^^^^^

Another method is to configure a route inside the EC2 and redirects it to another EC2 instance inside the same subnet. The latter EC2 instance sends the traffic to the default gateway (``+1`` of subnet network) and its route table has the entry for destination ``0.0.0.0/0`` pointing to the Internet Gateway. The responsible for translating the private address of the EC2 to the public address is the Internet Gateway. 

.. figure:: /networks_d/method2.png
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

* You can apply a security groups.

* You access over AWS Direct Connect, but no through AWS VPN.

* It makes requests to the service using endpoint-specific DNS hostnames. Optionally, you can use Amazon Route 53 DNS private hosted zone to make requests to the service using its default public DNS name.

The characteristics of an **Gateway VPC endpoint** are the following:

* It supports multiple AZs.

* It supports the use of endpoint policies.

* It cannot be accessed neither over AWS Direct Connect nor over VPN.

* It makes requests to the service using its default public DNS name.

An example of creating an Amazon S3 VPC endpoint is the following:

.. code-block:: console

  $ aws ec2 create-vpc-endpoint --vpc-id vpc-40f18d25 --service-name com.amazonaws.us-west-2.s3 --route-table-ids rtb-2ae6a24f

You need an entry in the route table with destination the prefix list for the S3 endpoint and the target the VPC endpoint. 

.. figure:: /networks_d/s3ep.png
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

.. figure:: /networks_d/layers.png
   :align: center

	  Controlling VPC access to Amazon S3

.. Note:: Prefix list.
	You can use prefix list with security groups but not with NACLs.

Amazon EC2 networking
=====================

Elastic network interface
-------------------------

You always have an ENI attached to an instance, it is the default ENI and cannot be modified. You can attach more than one ENI to an EC2 instance and they can be moved to another EC2 instance. In general, the ENIs of an EC2 instance are attached to different subnets. Each ENI have a private IP address and a public IP address, optionally you can have up to 4 private IP addresses and 4 public IP addresses.

.. figure:: /networks_d/eni.png
   :align: center

	  Elastic network interface

The ENIs will be attached to different VPC subnets in the same AZ. The ENIs are used to talk among EC2 instances but also between an EC2 instance and an EBS volume. Some EC2 instance types support EBS optimized dedicated throughput, which allows you to have dedicated throughtput to access an ENS volume.  

.. figure:: /networks_d/dedicated.png
   :align: center

	  EC2 instance types supporting EBS-optimized dedicated throughput

If we need to optimize network performance between 2 EC2 instances, the supported throughput is based on the instace type.

.. figure:: /networks_d/performance.png
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

.. figure:: /networks_d/jumbo.png
   :align: center

	  Jumbo frames

Every single device in between the EC2 instances must support 9001 MTU, which is not going to work when you go out the Internet. It is supported inside VPCs, but if you go through a Virtual Private Gateway or a VPN gateway, then it is not supported.

.. Note:: 
	Enable the ICMP message Type 3, Code 4 (Destination Unreachable: fragmentation needed and don't fragment set). This setting instructs the original host to adjust the MTU until the packet can be transmitted.

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

.. figure:: /networks_d/vgw.png
   :align: center

	 Extample of VPN connection

In the previous example, the IP addressing of the corporate data center is ``192.168.1.0/24``. In the route table, we can notice that the ``192.168.1.0/24`` has not been propagated so it has to be manually configured and not learned via BGP routing protocol.

You get 2 public IP addresses with a VGW that are across 2 different service providers. The customer gateway located in the corporate data center has only 1 IP address and you have to establish more than 1 VPN connections, unless it is redundant in different service providers. You need to establish 2 IPSec tunnels towards AWS per VGW connection because you 2 endpoints with different IP addresses. You can specify the preshared key of each one of the 2 IPSec tunnels and you can also specify the inside tunnel IP in between the two sides of the VPN.

.. figure:: /networks_d/vgwredundant.png
   :align: center

	 VPN redundancy

As you have 2 tunnels, there is a risk of asymmetric routing. To avoid it and prevents to send traffic from one path and not getting it returned to the other path, you can use BGP with one of these 2 options:

* Prepend an AS path.

* Set the multi-exit discriminator (MED) attribute.

.. figure:: /networks_d/asymmetric.png
   :align: center

	 Avoid asymmetric routing

You can connect from different data centers into the same VGW. One of the features of VGW is that you can use as a CloudHub. AWS VPN CloudHub is an AWS functionality, you only need to establish 2 VPN connections and by doing that you will able to use this CloudHub to send traffic between the 2 corporate data centers and there is no need to have direct connection between the two.

.. figure:: /networks_d/hub.png
   :align: center

	 AWS VPN CloudHub

VGW doesn't initiate IPSec negotiation. AWS uses an on-demand DPD mechanism so that:

* If AWS receives no traffic from a VPN peer for 10 seconds, AWS sends a DPD "R-U-THERE" message.

* If the VPN peer does not respond to 3 successive DPDs, the VPN peer is considered dead and AWS closes the tunnel.

Static VPN (policy-based VPN) is limited to one unique security association (SA) pair per tunnel (one inbound and one outbound). Instead, you should:

* Limit the number of encryption domains (networks) that are allowed access to the VPC and consolidate.

* Configure the policy to allow "any" network (``0.0.0.0/0``) from behind your VPN termination endpoint to the VPC CIDR.


Connecting networks
*******************

`AWS re:Invent 2018: AWS Direct Connect: Deep Dive (NET403) <https://www.youtube.com/watch?v=DXFooR95BYc&feature=emb_logo>`_


Load balancing on AWS
*********************

Elastic Load Balancing (ELB)
============================

`AWS re:Invent 2018: [REPEAT 1] Elastic Load Balancing: Deep Dive and Best Practices (NET404-R1) <https://www.youtube.com/watch?v=VIgAT7vjol8&feature=youtu.be>`_

High availability
*****************

Multi-region high availability and DNS
**************************************

Amazon Route 53
===============

When you sign up for Route 53 the first thing you do is create a Hosted Zone. This is where your DNS data will be kept. When you do that, you receive 4 name servers where you can delegate your domain. Then you specify your Fully Qualified Domain Name, which is the domain you have purchased with a DNS registrar. This could be external, or you can use Route 53 to purchase a domain. Proxy and privacy services are options with Amazon's Route 53 registrar, allowing you to hide partial or all your information within the DNS query.

The Hosted Zone will contain record sets, which are the DNS translations you want to perform for that specific domain