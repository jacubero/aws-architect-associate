Management and Governance Services
##################################

.. _secCloudWatch:

Amazon CloudWatch
*****************

CloudWatch provides the following default metrics: disk read operations, CPU usage, inbound network traffic.

.. _secAWSAutoScaling:

AWS Auto Scaling
****************

If instances are scaling up and down quickly means that the thresholds for adding and removing instances are being met frequently. The simplest way to reduce frequent scaling in an application is to increase the cooldown timers so that scaling down requires greater thresholds of change in the triggers.

AWS Cloud​Formation
******************

`CloudFormation Linter <https://github.com/aws-cloudformation/cfn-python-lint>`_.

`New – Import Existing Resources into a CloudFormation Stack <https://aws.amazon.com/blogs/aws/new-import-existing-resources-into-a-cloudformation-stack/>`_


.. _secCloudTrail:

AWS CloudTrail
**************

.. _secCLI:

AWS Command Line Interface (CLI)
********************************


AWS Config
**********

.. _secConsole:

AWS Management Console
**********************

AWS Systems Manager
*******************

AWS Trusted Advisor
*******************


AWS Well-Architected Tool
*************************

The AWS Well-Architected Tool helps you review your workloads against current AWS best practices and provides guidance on how to improve your cloud architectures. This tool is based on the **AWS Well-Architected Framework**. The AWS Well-Architected Framework has been developed to help cloud architects build secure, high-performing, resilient, and efficient infrastructure for their applications. Based on five pillars — operational excellence, security, reliability, performance efficiency, and cost optimization. — the Framework provides a consistent approach for customers and partners to evaluate architectures, and implement designs that will scale over time.

This is a free tool, available in the `AWS Management Console <https://console.aws.amazon.com/wellarchitected>`_. The process to evaluate a workload consists of 3 steps:

1. **Define a workload** by filling information about the architecture: name, a brief description to document its scope and intented purpose, the environment (production or pre-production), AWS Regions and Non-AWS Regions in which the workload runs, Account IDs (optional), industry type (optional) and industry (optional).

2. **Document the Workload State** by answering a series of questions about your architecture that span the pillars of the AWS Well-Architected Framework: operational excellence, security, reliability, performance efficiency, and cost optimization. After documenting the state of your workload for the first time, you should save a milestone and generate a workload report. A *milestone* captures the current state of the workload and enables you to measure progress as you make changes based on your improvement plan.

3. **Review the Improvement Plan**. Based on the best practices you selected, AWS WA Tool identifies areas of high and medium risk as measured against the AWS Well-Architected Framework. The Improvement items section shows the recommended improvement items identified in the workload. The questions are ordered based on the pillar priority that is set, with any high risk items listed first followed by any medium risk items.

4. **Make Improvements and Measure Progress**. After deciding what improvement actions to take, update the Improvement status to indicate that improvements are in progress. After making changes, you can return to the Improvement plan and see the effect those changes had on the workload. 

