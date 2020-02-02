Caching
#######

Caching overview
****************

CloudFront
**********

CloudFront provides improved latency, packet loss and overall quality. It avoids conflicts and network interconnect capacity. It offers greater operational control.

Lambda@Edge
===========

Lambda@Edge lets you run Lambda functions to customize the content that CloudFront delivers, executing the functions in AWS locations closer to the viewer. The functions run in response to CloudFront events, without provisioning or managing servers. You can use Lambda functions to change CloudFront requests and responses at the following points:

* After CloudFront receives a request from a viewer (viewer request).

* Before CloudFront forwards the request to the origin (origin request).

* After CloudFront receives the response from the origin (origin response).

* Before CloudFront forwards the response to the viewer (viewer response).

.. figure:: /caching_d/cloudfront-events-that-trigger-lambda-functions.png
   	:align: center

	Cloudfront events that trigger Lambda functions


CloudFront signed URLs and signed cookies
=========================================

CloudFront signed URLs and signed cookies provide the same basic functionality: they allow you to control who can access your content. If you want to serve private content through CloudFront and you're trying to decide whether to use signed URLs or signed cookies, consider the following:

Use **signed URLs** for the following cases:

* You want to use an RTMP distribution. Signed cookies aren't supported for RTMP distributions.

* You want to restrict access to individual files, for example, an installation download for your application.

* Your users are using a client (for example, a custom HTTP client) that doesn't support cookies.

Use **signed cookies** for the following cases:

* You want to provide access to multiple restricted files, for example, all of the files for a video in HLS format or all of the files in the subscribers' area of a website.

* You don't want to change your current URLs.

.. figure:: /caching_d/PrivateContent_TwoParts.png
   	:align: center

	Private Content in CloudFront

Pricing
=======

To estimate the cost of using CloudFront, you need to consider the following:

* **Traffic distribution**. Data transfer and request pricing vary across geographic regions, and pricing is based on the edge location through which your content is served.

* **Requests**. The number and type of requests made and the geographic region in which the requests are made.

* **Data transfer out**. The amount of data transferred out of your Amazon CloudFront edge locations.

The benefit you get by caching dynamic content is that request and the response ride over the AWS backbone instead the public Internet. 

You can set origins as a S3 for static content. For dynamic content, you can setup as origin EC2 instances, ELB instances, and HTTP servers. It supports SSL so that private content is protected.

Amazon ElastiCache
******************

Amazon ElastiCache is a web service that makes it easy to deploy, operate, and scale an in-memory data store or cache in the cloud. The service improves the performance of web applications by allowing you to retrieve information from fast, managed, in-memory data stores, instead of relying entirely on slower disk-based databases.

.. figure:: /caching_d/elasticache.png
   	:align: center

	Amazon ElastiCache

Redis
=====

Using Redis ``AUTH`` command can improve data security by requiring the user to enter a password before they are granted permission to execute Redis commands on a password-protected Redis server. Hence, Option 3 is the correct answer.

To require that users enter a password on a password-protected Redis server, include the parameter ``--auth-token`` with the correct password when you create your replication group or cluster and on all subsequent commands to the replication group or cluster.

.. figure:: /caching_d/ElastiCache-Redis-Secure-Compliant.png
   	:align: center

	Amazon ElastiCache authentication and encryption
