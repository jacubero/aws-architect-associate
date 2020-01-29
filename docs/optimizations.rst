Optimizations and review
########################

AWS Trusted Advisor
*******************

AWS Trusted Advisor is an online tool that provides you real time guidance to help you provision your resources following AWS best practices. AWS Trusted Advisor analyzes your AWS environment and provides best practice recommendations in 5 categories:

* Cost Optimization

* Performance

* Security

* Fault Tolerance

* Service Limits

The status of the check is shown by using color coding on the dashboard page: 

* Green: no problem detected.

* Yellow: investigation recommended.

* Red: action recommended.

For each check, you can review a detailed description of the recommended best practice, a set of alert criteria, guidelines for action, and a list of useful resources on the topic. 

`Architecting for the Cloud <https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf>`_

`Fault-Tolerant Components on AWS <https://d1.awsstatic.com/whitepapers/aws-building-fault-tolerant-applications.pdf>`_

AWS Budgets
***********

AWS Budgets gives you the ability to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.

Budgets can be tracked at the monthly, quarterly, or yearly level, and you can customize the start and end dates. You can further refine your budget to track costs associated with multiple dimensions, such as AWS service, linked account, tag, and others. Budget alerts can be sent via email and/or Amazon Simple Notification Service (SNS) topic.

You can also use AWS Budgets to set a custom reservation utilization target and receive alerts when your utilization drops below the threshold you define. RI utilization alerts support Amazon EC2, Amazon RDS, Amazon Redshift, and Amazon ElastiCache reservations.

Budgets can be created and tracked from the AWS Budgets dashboard or via the Budgets API.

AWS Config
**********

AWS Config is a service that enables customers to assess, audit, an evaluate the configurations of AWS resources. AWS Config continuously monitors and records AWS resource configurations and allows customers to automate the evaluation of recorded configurations against desired configurations and notify you if something is not compliant. 

With Config, customers can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine the overall compliance against the configurations specified in their internal or best-practices guidelines. This enables customers to simplify compliance auditing, security analysis, change management, and operational troubleshooting.

In addition, AWS Config can compare configuration changes against best-practices configuration rules, which are available from AWS. Any deviations can generate notification or automated remediation events that trigger actions using services like AWS Lambda. Config can also be used to track resource inventory of the environment.

When you set up AWS Config, you complete the following:

* Specify the resource types that you want AWS Config to record.

* Set up an S3 bucket to receive a configuration snapshot on request and configuration history.

* Set up an SNS topic to send configuration stream notifications.

* Grant AWS Config the permissions it needs to access S3 bucket and the SNS topic.

* Specify the rules that you want AWS Config to use to evaluate compliance information for the recorded resource types.
