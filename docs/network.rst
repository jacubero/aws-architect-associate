Networking in AWS
########################################

.. _secVPC:

Amazon Virtual Private Cloud (VPC)
**********************************

`AWS re:Invent 2018: Your Virtual Data Center: VPC Fundamentals and Connectivity Options (NET201) <https://www.youtube.com/watch?time_continue=1&v=jZAvKgqlrjY&feature=emb_logo>`_

To add a CIDR block to your VPC, the following rules apply:

* The allowed block size is between a /28 netmask and /16 netmask.

* The CIDR block must not overlap with any existing CIDR block that's associated with the VPC.

* You cannot increase or decrease the size of an existing CIDR block.

* You have a limit on the number of CIDR blocks you can associate with a VPC and the number of routes you can add to a route table. You cannot associate a CIDR block if this results in you exceeding your limits.

* The CIDR block must not be the same or larger than the CIDR range of a route in any of the VPC route tables. For example, if you have a route with a destination of 10.0.0.0/24 to a virtual private gateway, you cannot associate a CIDR block of the same range or larger. However, you can associate a CIDR block of 10.0.0.0/25 or smaller.

* The first four IP addresses and the last IP address in each subnet CIDR block are not available for you to use, and cannot be assigned to an instance.

To calculate the total number of IP addresses of a given CIDR Block, you simply need to follow the 2 easy steps below. Let's say you have a CIDR block /27: 

1. Subtract 32 with the mask number :  :math:`(32 - 27) = 5`

2. Raise the number 2 to the power of the answer in Step #1 : :math:`2^5 = 32`

The answer to Step #2 is the total number of IP addresses available in the given CIDR netmask. Don't forget that in AWS, the first 4 IP addresses and the last IP address in each subnet CIDR block are not available for you to use, and cannot be assigned to an instance.

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