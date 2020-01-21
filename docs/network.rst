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