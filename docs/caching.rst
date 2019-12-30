Caching
#######

Caching overview
****************

Caching on AWS
**************

CloudFront
==========

To estimate the cost of using CloudFront, you need to consider the following:

* **Traffic distribution**. Data transfer and request pricing vary across geographic regions, and pricing is based on the edge location through which your content is served.

* **Requests**. The number and type of requests made and the geographic region in which the requests are made.

* **Data transfer out**. The amount of data transferred out of your Amazon CloudFront edge locations.

The benefit you get by caching dynamic content is that request and the response ride over the AWS backbone instead the public Internet. 

You can set origins as a S3 for static content. For dynamic content, you can setup as origin EC2 instances, ELB instances, and HTTP servers. It supports SSL so that private content is protected.

Caching your web tier
*********************

Caching your database
*********************

