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