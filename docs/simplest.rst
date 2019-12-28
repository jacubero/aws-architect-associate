The simplest architectures
##########################

`AWS Storage Services Overview <https://d1.awsstatic.com/whitepapers/AWS%20Storage%20Services%20Whitepaper-v9.pdf>`_

Amazon S3
*********

`Introduction to Amazon Simple Storage Service (S3) <https://www.qwiklabs.com/focuses/8582?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=4127023>`_

Cost Factors
============

To estimate the cost of using S3, you need to consider the following:

* **Storage**. The number and size of objects stored in your S3 buckets as well as the type of storage (storage class). You can reduce the costs by storing less frequently accessed data at slightly lower levels of redundancy then the Amazon S3 standard storage. It is important to note that each class has different rates.

* **Requests**. The number and type of requests. GET requests incur charges ata different rates than other requests, such as PUT and COPY requests.

* **Data transfer**. The amount of data transferred out of the Amazon S3 region



`Access control in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-overview.html>`_

`Amazon S3 Block Public Access – Another Layer of Protection for Your Accounts and Buckets <https://aws.amazon.com/blogs/aws/amazon-s3-block-public-access-another-layer-of-protection-for-your-accounts-and-buckets/>`_

`AWS re:Invent 2018: [Repeat] Deep Dive on Amazon S3 Security and Management (STG303-R1) <https://www.youtube.com/watch?v=x25FSsXrBqU&feature=youtu.be&t=989+%28>`_

`Using Amazon S3 Block Public Access <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html>`_

`How Do I Block Public Access to S3 Buckets? <https://docs.aws.amazon.com/AmazonS3/latest/user-guide/block-public-access.html>`_

`Using Versioning <https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html>`_

`Locking Objects Using Amazon S3 Object Lock <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`_

`Cross-Origin Resource Sharing (CORS) <https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html>`_ 

`New – AWS Transfer for SFTP – Fully Managed SFTP Service for Amazon S3 <https://aws.amazon.com/blogs/aws/new-aws-transfer-for-sftp-fully-managed-sftp-service-for-amazon-s3/>`_

`Multipart Upload Overview <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>`_

`AWS re:Invent 2018: [REPEAT 2] Best Practices for Amazon S3 and Amazon Glacier (STG203-R2) <https://www.youtube.com/watch?time_continue=16&v=rHeTn9pHNKo&feature=emb_logo>`_ 

Amazon S3 Glacier
*****************

`Amazon S3 Storage Classes <https://aws.amazon.com/s3/storage-classes/>`_

`Coming Soon – S3 Glacier Deep Archive for Long-Term Data Retention <https://aws.amazon.com/about-aws/whats-new/2018/11/s3-glacier-deep-archive/>`_

`Object Lifecycle Management <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html>`_

.. _secStorageClasses:

Storage classes
===============

The typical lifecycle of data is the newer it is, the more frequently it is consumed. Amazon S3 offers a range of storage classes designed for different use cases. These include:

* S3 Standard for general-purpose storage of frequently accessed data.

* S3 Intelligent-Tiering for data with unknown or changing access patterns.

* S3 Standard-Infrequent Access (S3 Standard-IA) and S3 One Zone-Infrequent Access (S3 One Zone-IA) for long-lived, but less frequently accessed data.

* Amazon S3 Glacier and Amazon S3 Glacier Deep Archive for long-term archive and digital preservation.

S3 Intelligent-Tiering
----------------------

The S3 Intelligent-Tiering storage class is designed to optimize costs by automatically moving data to the most cost-effective access tier, without performance impact or operational overhead. 

It works by storing objects in 2 access tiers: one tier that is optimized for frequent access and another lower-cost tier that is optimized for infrequent access. For a small monthly monitoring and automation fee per object, Amazon S3 monitors access patterns of the objects in S3 Intelligent-Tiering and move the ones that have not been accessed for 30 consecutive days to the infrequent access tier.

The S3 Intelligent-Tiering charges a per object monitoring fee to monitor and place an object in the optimal access tier. As a result, on a relative basis, the object fee is less when the objects are larger and thus the amount you can save is potentially higher. In the following image, you can see an example of the potential cost savings for objects stored in S3 Standard versus S3 Intelligent-Tiering. For these calculations, we assumed 10 PB of data, in US-East-1 AWS Region, and a minimum object size of 128 KB.

.. image:: /intro_d/comparison.png

Choosing regions for your architectures
***************************************

`AWS & Sustainability <https://aws.amazon.com/about-aws/sustainability/>`_

`Save yourself a lot of pain (and money) by choosing your AWS Region wisely <https://www.concurrencylabs.com/blog/choose-your-aws-region-wisely/>`_

