Adding a compute layer
######################

.. _secEC2:

Adding Compute with Amazon EC2
******************************

Amazon EC2 allows to create and run virtual machines on AWS cloud. AWS calls these virtual machines *instances*. AWS provides various configurations of CPU, memory, storage, and networking capacity for your instances, known as *instance types*.

.. figure:: /compute_d/ec2.png

	Amazon EC2

Launching Amazon EC2 instances with Amazon Machine Images (AMIs)
================================================================


Launching Amazon EC2 instances with user data
=============================================


Amazon EC2 and storing data
===========================

`AWS re:Invent 2018: [REPEAT 1] Deep Dive on Amazon Elastic Block Storage (Amazon EBS) (STG310-R1) <https://www.youtube.com/watch?v=BuJa6Vl8cn8>`_


`AWS re:Invent 2018: [REPEAT 1] Deep Dive on Amazon Elastic File System (Amazon EFS) (STG301-R1) <https://www.youtube.com/watch?v=4FQvJ2q6_oA>`_

Amazon EC2 instance types
=========================

.. figure:: /compute_d/instancetypes.png


.. csv-table:: Instance Types List
   :file: /compute_d/instance_types.csv
   :widths: auto
   :header-rows: 1

Script:

.. literalinclude:: compute_d/describe_instance_types.py
  :language: python


Amazon EC2 pricing options
==========================

* **On-Demand**: Pay by the hour, no long-term commitments.

* **Reserved**: pay upfront, 50-75% lower hourly rate.

* **Spot**: Bid for unused EC2 capacity.

* **Dedicated**: Dedicated to a single customer, isolated at hardware level.

Amazon EC2 considerations
=========================


`Instance Lifecycle <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html>`_


`Resource Locations <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resources.html>`_


Security groups operate at the instance level.

Security groups disallow all traffic unless there are specific allow rules for the traffic in the security group. They only provide for allow rules.

Security groups evaluate all the rules on the group before deciding how to handle traffic.

Changes to a security group take place immediately.

For all new AWS accounts, 20 instances are allowed per region. However, you can increase this limit by requesting it via AWS support.

Instances within a VPC with a public address have that address released when it is stopped and are reassigned a new IP when restarted.

All EC2 instances in the default VPC have both a public and private IP address.

`AWS re:Invent 2018: [REPEAT 1] Amazon EC2 Foundations (CMP208-R1) <https://www.youtube.com/watch?time_continue=1&v=vXBeO9vQAI8&feature=emb_logo>`_
