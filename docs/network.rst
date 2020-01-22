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

The route tables allows you to route to some gateway. The route table get applied to router of the subnet itself (+1 of the subnet itself). The default gateway of the EC2 instance (``0.0.0.0/0``) always will be pointing to the router of the subnet. In this router, you will have a routing table with an entry with destination the VPC CIDR blocks and the target local. Local means that you can route to every resource in the VPC. The local entry in the routing table has priority over the rest of the routes. The other entry in the routing table has a destination ``0.0.0.0/0`` and target the internet gateway. The **internet gateway** allow an EC2 instance to route traffic to Internet or any resource in the Internet route traffic to the EC2 instance.

.. figure:: /networks_d/internetg.png
   :align: center

	 Example of a routing table

VPC: Gateways
-------------

A **NAT gateway** is a managed address translation gateway. 

IPv6 addresses on EC2 instances are public addresses, so that if we connect them to internet gateway there would be reachable from Internet. The **egress-only internet gateway** is a gateway for IPv6 only, that allows EC2 instances with IPv6 addresses to reach Internet, but they are not reachable from Internet.

**VPC peering connection**

VPC Routing: Public subnet
--------------------------

What makes a subnet public is its routing table. It has an entry with destination ``0.0.0.0/0`` and target the Internet Gateway. You would need a public IP address attached to the network interface of EC2 instance in this subnet. The packets coming from the EC2 instance to the Internet Gateway have a private IP address and they are translated to the public IP address attached to it thanks to the Internet Gateway.

.. figure:: /networks_d/public.png
   :align: center

	  Example of public subnet routing table

You do not need to manage the Internet Gateway. It scales out or in depending on the amount the traffic it has to handle. The maximum throughtput it can support is 5Gbps.

VPC Routing: Private subnet
---------------------------

If an EC2 in a private subnet wants to communicate to the Internet, this subnet needs to be attached to a NAT gateway which lives in a public subnet. There is an entry in the routing table in which the destination is ``0.0.0.0/0`` ad the target is the NAT gateway. 

.. figure:: /networks_d/private.png
   :align: center

	  Example of private subnet routing table

The NAT gateway allows the EC2 with a private address to reach the Internet but the EC2 instance is not reachable from the Internet. The NAT gateway requires an Elastic IP address that will be used to translate the private address of the EC2 instance. Even if you are using a NAT gateway, you are still passing through an Internet Gateway to reach the Internet. You have one Internet Gateway per VPC but you can have multiple NAT gateways inside you VPC. The reason to have more than one is that they are highly available within an AZ, not across AZs. 

A NAT gateway separate subnets and can scale up to 45 Gbps. There is a limit of 55000 connections towards the same destination. If you need more thant 45 Gbps or more than 55000 connections towards the same destination, then you will need more than one NAT gateway. In that case, you will need another subnet with a different routing table that will point towards the second NAT gateway.

EC2 instance as in-line next-hop
--------------------------------

If you want to implement you own NAT gateway or IDS or IPS, ... by using an EC2 instance, then you will need to use it as in-line next-hop. There are several methods to implement it.

Method 1
^^^^^^^^

You will need to define an entry in the routing table with destination ``0.0.0.0/0`` and the target is an ENI (Elastic Network Interface) of an EC2 instance within a public subnet. This EC2 instance has reachability to the Internet via an Internet Gateway.

.. figure:: /networks_d/method1.png
   :align: center

	  EC2 instance as in-line next-hop: Method 1

The responsible for translating the private address of the EC2 to the public address is the Internet Gateway. 

Method 2
^^^^^^^^

Another method is to configure a route inside the EC2 and redirects it to another EC2 instance inside the same subnet. The latter EC2 instance sends the traffic to the default gateway (``+1`` of subnet network) and its routing table has the entry for destination ``0.0.0.0/0`` pointing to the Internet Gateway. The responsible for translating the private address of the EC2 to the public address is the Internet Gateway. 

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

You need an entry in the routing table with destination the prefix list for the S3 endpoint and the target the VPC endpoint. 

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
        "Sid": "Access-to-specific-bucket-only",
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

Virtual Private Gateway
-----------------------


Security in the cloud
*********************


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