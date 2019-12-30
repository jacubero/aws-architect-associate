Building decoupled architectures
################################

Decoupling your architecture
****************************

Decoupling with Amazon SQS
**************************

`AWS re:Invent 2018: Choosing the Right Messaging Service for Your Distributed App (API305) <https://www.youtube.com/watch?time_continue=2&v=4-JmX6MIDDI&feature=emb_logo>`_ 

Decoupling with Amazon SNS
**************************

Amazon SNS
==========

The most important characteristics of SNS are the following:

* It is a flexible, fully managed pub/sub messaging and mobile communications service.

* It coordinates the delivery of messages to subscribing endpoints and clients, therefore enabling you to send different information to different subscribers.

* It is easy to setup, operate and send realiable communications. 

* It allows you to decouple and scale microservices, distributed systems and serverless communications.

Amazon SNS allows you to have pub/sub messaging for different systems in Amazon, like AWS Lambda, HTTP/S and Amazon SQS. Amazon SNS Mobile Notifications allows you to do similar publishing but to different mobile systems, like ADM, APNS, Baidu, GCM, MPNS, and WNS.

AWS Budget
==========

AWS Budgets gives you the ability to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.

Budgets can be tracked at the monthly, quarterly, or yearly level, and you can customize the start and end dates. You can further refine your budget to track costs associated with multiple dimensions, such as AWS service, linked account, tag, and others. Budget alerts can be sent via email and/or Amazon Simple Notification Service (SNS) topic.

You can also use AWS Budgets to set a custom reservation utilization target and receive alerts when your utilization drops below the threshold you define. RI utilization alerts support Amazon EC2, Amazon RDS, Amazon Redshift, and Amazon ElastiCache reservations.

Budgets can be created and tracked from the AWS Budgets dashboard or via the Budgets API.
