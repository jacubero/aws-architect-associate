Networking and Content Delivery Services
########################################

Amazon VPC
**********

Route propagation with respect to a virtual private gateway is a routing option that automatically propagates routes to the route tables so you don't need to manually enter VPN routes. It's most common in a Direct Connect setup.

A custom VPC with instances in a public subnet and a internet gateway attached to it. They can reach internet if the have their outbound traffic directed to the internet gateway on the VPC.

All custom VPCs have a route table and a NACL and will not have an internet gateway. Subnets can communicate with each other across availability zones by default.

A VPC endpoint is a virtual device that provides redundancy via AWS (and automatically). VPC endpoints scale horizontally. VPC endpoint comes in two flavors:

* Interface endpoint, which provides an elastic network interface and a private IP address.

* Gateway endpoint, targeted for a specific route in the route table.

A VPC interface endpoint provides a private IP address for connecting to a specific entry point for a specific AWS service. For instance: A Kinesis data stream, an API gateway. 

Both a NAT instance and a NAT gateway provide for outgoing traffic to route to the internet from instances within a private subnet. NAT gateways are, in general, a better solution than NAT instances.

If you need to increase the performance of a NAT instance then you need to increase the instance size of the NAT instance.

To get a NAT instance working it is necessary to:

* Update the routing table for EC2 instances accessing the public Internet to go through the NAT instance.

* Disable source/destination checks on the instances.

A gateway endpoint handles all traffic for a supported AWS service. For instance: S3, DynamoDB.

Instances that take advantage of a VPC endpoint do not need to have a public IP address or use a NAT instance. Instead, assuming they have a route to the endpoint, they send traffic over the AWS network to the connected service.

VPCs can have a single internet gateway and multiple subnets.

To route traffic from a subnet to the public Internet, you need to set for their instances a route with:

* Dastination=*0.0.0.0/0*, which is the the destination address for the public Internet.

* Target=the VPC internet gateway.

5 VPCs are allowed per region, per account, unless you contact AWS to raise this default limit.

A VPC cannot be changed from dedicated hosting tenancy to default hosting. If you need to do so, yoy have to recreate the VPC.

All VPCs have NACLs, security groups, and route tables automatically created. However, only the default VPC has a default subnet and internet gateway created as well, different from the custom VPC.



Amazon API Gateway
******************


Amazon CloudFront
*****************

CloudFront is a caching mechanism that supports both static and dynamic content.

Amazon Route 53
***************


AWS Direct Connect
******************


AWS Transit Gateway
*******************


Elastic Load Balancing (ELB)
****************************

