The simplest architectures
##########################

`AWS Storage Services Overview <https://d1.awsstatic.com/whitepapers/AWS%20Storage%20Services%20Whitepaper-v9.pdf>`_

* **Block storage** is data organized as an array of unrelated blocks. Host file system places data on disk. AWS provides block storage with Amazon EBS.

* **File storage** is unrelated data blocks managed by a file (serving) system. Native file system places data on disk. For example NTFS for Microsoft storage. Data stored in a file system contains attributes such as permissions, file owner and they are stored as metadata in the file system. AWS provides file storage with Amazon EFS.

* **Object storage**. It is a flat system which stores data as objects which encapsulates the attributes, metadata, and other properties. It stores the data, data attributes, metadata, and object IDs as objects. It provides API access to data. It is metadata driven, policy-based, etc. It allows you to store ilimitedless amount of data and scales easily. Content type, permissions and the file owner are stored as metadata in a file system. There are more metadata that can be stored as object. You can create custom metadata named values that can be used for such things as analytics. AWS provides object storage with Amazon S3.

Each storage option has a unique combination of performance, durability, cost and interface.

Amazon S3
*********

Amazon S3 Overview
==================

`Introduction to Amazon Simple Storage Service (S3) <https://www.qwiklabs.com/focuses/8582?parent=catalog>`_

It is intentionally built with a minimum feature set focusing on simplicity and robutness: It is a highly durable, highly available, high performant object storage service. It provides you an easy-to-use, scalable object storage service that is payable as you go and integrates with other AWS services and 3rd party solutions. Main characteristics:

* You pay for what you use. You don't need to preprovision the size of your Amazon S3 for your data.

* It is designed for 11 nines of durability.

* It is performant system that is highly scalable.

* It has different storage classes and transitions targets:

	* S3 Standard.

	* S3 Standard - Infrequent Access.

	* S3 One Zone - Infrequent Access.

	* and the possibility to automatically transition data to Amazon Glacier.

Amazon S3 stores the data as objects within buckets. An object consists of data and optionally any metadata that describes that file.

Object Storage Classes
----------------------

Consider the type of data, the resiliency requirements and usage pattern in order to decide which object storage class is best suited to your needs.

The first and default option is **Amazon S3 Standard** designed for the active data or hot workloads, it provides milliseconds access and has the highest cost of the 3 classes. If you don't know what your access patterns are or you need frequent retrieval, start with S3 Standard. Some common use cases are Big Data analysis, Content distribution and Web site hosting.

As your data ages and it's accessed less, you can use **Amazon S3 Standard - IA**. It is designed for colder or less frequently accessed data that requires milliseconds access. For example, you can leverage the Standard IA class to store detailed application logs that you analyze infrequently. It provides the same performance, throughput and low latency as the Standard storage class. It is lower in storage costs but along with storage costs, there is a retrieval cost associated with object access higher than with Amazon S3 Standard. Some common use cases are backup storage, DR, data that doesn't change frequently.

**Amazon S3 One Zone - IA** is ideal for customers who want a lower-cost option for infrequently accessed data, require similar milliseconds access but don't require the same durability and resiliency as the previous classes. It costs less than the previous classes as it stores data in only 1 AZ. It has the same associated retrieval cost as Amazon S3 Standard - IA. It is a good choice for example for storing secondary backup copies of on-premises data, or easily recreated data, or storage use of Amazon S3 Cross Region replication target from another AWS S3 Region.

Amazon Glacier is suitable for archiving data where data access in frequent. Archive data is not available for real-time access. You must restore the objects before you can access them. It is storage service designed for long-term archival storage and asynchronous retrieval from minutes to hours. For example you can leverage Amazon Glacier for storing long-term backup archives. The cost of storage for Amazon Glacier is less than the other storage classes and has also an additional cost for data retrieval. There are 3 retrieval options ranging in time from minutes to hours.

S3 Standard, S3 Standard-IA and Glacier replicates its data across at least to 3 different AZs within a single region. If you do not need this resiliency, S3 One Zone-IA is stored in 1 AZ. If this AZ is destroyed, you will lose your data.

.. figure:: /simplest_d/classes.png
   :align: center

   Comparing Object Storage Classes

Using Amazon S3
===============

Buckets
-------

Amazon S3 uses buckets to store your data. Before you can transfer data into Amazon S3, you must first create a bucket. The data that is transfer is stored as objects in the bucket. When creating bucket you don't pre-determine size, apy for what you use.

One factor that you must consider when creating a bucket is the region where the bucket will be created. Wherever region the bucket is created in is where your data resides. You consider the location to optimize latency, minimize cost and comply with regulations.

Data in Amazon S3 do not expands regions automatically, although you can replicate your bucket to other regions if needed. This feature is called Cross-Region replication.

When you create a bucket, the bucket is owned by the AWS account that created it and the bucket ownership is not transferable. There is no limit in the number of object that can be stored in a bucket. There is no difference in performance whether you use many or just a few. You can store all of your objects in a single bucket or you can organize them across several buckets. You cannot create a bucket within another bucket. By default, you can create 100 buckets under each of your AWS accounts. If you need additional buckets, you can increase your bucket limit by submitting a service limit increase.

When naming your bucket, there are some rules you need to follow: the name of your bucket must globally unique and to be DNS-compliant. Be aware of uppercase letters in your bucket name, all names should be lowercase. The rules for DNS-compliant names are:

* Bucket names must be 3 and 63 characters long.

* Bucket names can contain lowercase letters, numbers, and hyphens. Each label must start and end with a lowercase letter or a number.

* Bucket names must not be formatted as an IP address.

* It is recommended that you do not use periods in bucket names.

Objects
-------

The file and metadata that you upload or create are essentially containerized in an object. Knowning the parts that make up an object is useful when you need to find accessed object in your bucket or when you create policies to secure your data.

If we have an object called ``mybucket/mydocs/mydocument.doc``. The *key* is the name we assigned to an object, in this example: ``mydocs/mydocument.doc``. You will use the object key to retrieve the object. Although you can use any UTF-8 characters in an object name, using the key naming best practices helps ensure maximum compatibility with other applications. The following object key name guideliens will helps you compliance with DNS, website characters, XML parsers and other APIs:

* Alpahnumeric characters: 0-9, a-z, A-Z.

* Special characters: !, -, _, ., *, `, (, ).

If you utilize any other characters in key names, they may require special handling.

The parts that makes up an object are:

* *Version ID* uniquely identify an object. It is the string that AWS generates when you add an object to a bucket. This is utilized when versioning is enabled on your bucket.

* *Value* is the content that you are storing. It can be any sequence of bytes. Objects size can be 0-5 TB.

* *Metadata* is a set of name/value pairs where you can store information regarding the object. Your applications and data analysis may take advantage of your metadata to identify an classify your data. There are 2 kinds of metadata:

	* System-defined metadata. For every object stored in a bucket, Amazon S3 maintains a set of system metadata of the objects for managing them. For example: creation time and date, size, content type, storage class. Some system metadata can be modified, for more details go to `Object Key and Metadata <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`_

	* User-defined metadata. You provide this optional information as a name-value pair when you send the request to create an object or update the value when you need. User-defined metadata requires a special prefix: ``x-amz-meta-`` when uploadin via the REST API, otherwise S3 will not set the key-value pair as user-defined. You can only set the value of the metadata at the time when you upload it. After you uploaded the object, you cannot modify existing metadata. The only way to modify existing object metadata is to make a copy of the object and set the new metadata value. There is one exception to this: the use of object tags. Object tags are another for of metadata that help with the organization of the data that can be changed at any time.

* *Access control information*. You can control access to the objects stored in Amazon S3. It supports resource access control such as ACLs, bucket policies, and User-based access control.

Another important aspect about objects is that objects are not partially updated. When you make a change to an object or upload a new copy into the bucket which does not have versioning enabled, a new object is created an overwrites the existing object. If you have versioning enabled in your bucket an upload a new copy, a new version of the object is created.

Amazon S3 is a distributed system. If it receives multiple write requests for the same object simultaneously, it overwrites all but the last object written.

Amazon S3 does not provided object locking.

Accessing your data
-------------------

There multiple ways in which you can make your requests to retrieve or add data to your Amazon S3 bucket:

* You can view, upload and download objects through the AWS Console. For large amounts of data this is not the best way to transfer or access the data. The maximum size of a file that you can upload using the console is 78 GB.

* Via AWS CLI.

* Via AWS SDK.

Amazon S3 supports 2 types of URLs to access objects:

* *Path-style URL*. Structure:

.. code-block:: console

	http://<region-specific endpoint>/<bucket name>/<object name>

Example:

.. code-block:: console

	http://s3-eu-west-1.amazonaws.com/mybucket/sensordata.html

* *Virtual-hosted-style*. Structure:

.. code-block:: console

	http://<bucketname>.s3.amazonaws.com/<object key>

Example:

.. code-block:: console

	http://mybucket.s3.amazonaws.com/sensordata.html

It is recommended to use Virtual-hosted-style URLs. It is useful if you are using your S3 bucket to host a static website. You can also publish to the root directory of your bucket virtual server. This ability can be important since many existing applications search for files in this standard location.

You should be aware that when accessing your with HTTP-based URL, if your name your bucket to match your registered domain name such as ``www.example.com`` and set that DNS name as a CNAME alias for ``www.example.com.s3.amazonaws.com`` you can access objects with a customized URL such as:

.. code-block:: console

	http://www.example.com/sensordata.html

When accessing your bucket with a HTTP-based URL, if your bucket has a period in your bucket name it can cause certificate exceptions when accessed. To support HTTP access to your bucket, you should avoid using a period in the bucket name.

How a request is routed
-----------------------

S3 uses DNS to route requests to facilities that can process them. This system works very effectively. However, temporary routing errors can occur. If a request arrives at the wrong Amazon S3 region, S3 responds with a temporary redirect that tells the requester to resend the request to the correct region. If a request is incorrectly formed, S3 uses permanent redirects to provide direction on how to perform the request correctly and S3 will respond with a 400 error.

In the following diagram are the steps of how the DNS request process occurs:

.. figure:: /simplest_d/request.png
   :align: center

   How a request is routed

1. The client makes a DNS request to get an object stored on S3.

2. The client receives one or more IP addresses for facilites that can process the request.

3. The client makes a request to S3 regional endpoint.

4. S3 return a copy of the object.

Operations on Objects
---------------------

PUT
^^^

In order to get an object into a bucket, you will use the PUT operation. You can upload or copy objects of up tp 5 GB in a single PUT operation. For larger objects up to 5 TB, you must use the multipart upload API.

Multipart upload allows you to upload a single object as a set of parts. You can upload each part separately. If one of the parts fails to upload, you can retransmit that particular part without retransmitting the remaining parts. After all the parts of your object are uploaded to the server, you must send a complete multipart upload request that indicates that multipart upload has been completed. S3 then assembles these parts and creates the complete object. You should consider using multipart upload for objects larger than 100 MB. With multipart uploads you can upload parts in parallel to improve throughput, recover quickly from network issues, pause and resume object uploads, and begin an upload before you know the final size of an object.

You can also abort a mulitpart upload. When you abort an upload, S3 deletes all the parts that were already uploaded and frees up storage. S3 retains all parts on the server until you complete or abort the upload. Make sure to complete or abort an upload to avoid unnecessary storage costs related to incomplete uploads. You can also take advantage of lifecyle rules to clean up incomplete multipart uploads automatically. As a best practice, it is recommended to enable the Clean up incomplete multipart uploads in the lifecycle settings even if you are not sure that you are actually making use of multipart uploads. Some applications will default to the use of multipart uploads when uploading files avove a particular, application-dependent, size.

COPY
^^^^

Once your objects are in the bucket you can use the COPY operation to create copies of an object, rename an object, move it to a different S3 location, or to update its metadata.

GET
^^^

Using a GET request you can retrieve a complete object from your bucket. You can also retrieve an object in parts using ranged GETs, by specifying the range of bytes needed. This is useful in scenarios where network connectivity is poor or your application can or must process only subsets of object data.

DELETE
^^^^^^

You can delete a single object or delete multiple objects in single delete request. There are 2 things that can occur when you issue a DELETE request, depending if versioning is enabled or disabled on your bucket.

In a bucket that is not versioning-enabled, you can permanently delete an object by specifying the key that you want to delete. Issuing the delete request permanently removes the object and it is not recoverable, there is no recycle bin type feature in buckets when versioning is disabled.

In a bucket that is versioning-enabled, you can permanently delete an object or a delete marker is created by S3 and the object, depending on how the delete request is made:

* If you specify a key only with the delete request, S3 adds a delete market which becomes the current version of the object. If you try to retrieve an object that has a delete marker, S3 returns a 404 Not Found error. You can recover the object by removing the delete marker from the current version of the object and it will then become available againg for retrieval. 

* You can also permanently delete individual versions of an object, by invoking a delete request with a key and the version ID. To completely remove the object from your bucket, you must delete each individual version.

List Keys
^^^^^^^^^

With object storage such as S3, there is no hierarchy of objects stored in buckets, it is a flat storage system. In order to organize your data you can use prefixes in key names to group similar items. You can use delimiters (any string such as / or _) in key names to organize your keys and create a logical hierarchy. If you use prefixes and delimiters to organize keys in a bucket, you can retrieve subsets of keys that match certain criteria. You can list keys by prefix. You can also retrieve a set of common key prefixes by specifying a delimeter. This implementation of the GET operation returns some or all (up to 1000) of the objects in a bucket.

In the following example, the bucket named scores contains objects with English and Maths scores of students for the year 2017. 

.. code-block:: console

	aws s3api list-objects --bucket scores --query "Contents[].{Key: Key}"

	2017/score/english/john.txt
	2017/score/english/sam.txt
	2017/score/maths/john.txt
	2017/score/maths/sam.txt
	2017/score/summary.txt
	overallsummary.txt

To list keys related to the year 2017 in our scores bucket, specify the prefix of ``2017/``.

.. code-block:: console

	aws s3api list-objects --bucket scores --prefix 2017/ --query "Contents[].{Key: Key}"

	2017/score/english/john.txt
	2017/score/english/sam.txt
	2017/score/maths/john.txt
	2017/score/maths/sam.txt
	2017/score/summary.txt

To retrieve the key for the 2017 scores summary in the scores bucket, specify a prefix of ``2017/score/`` and delimiter of ``/``. The key ``2017/score/summary.txt`` is returned because it contains the prefix ``2017/score/`` and does not contain the delimiter ``/`` after the prefix.

.. code-block:: console

	aws s3api list-objects --bucket scores --prefix 2017/score/ --delimiter / --query "Contents[].{Key: Key}"

	2017/score/summary.txt

To find subjects for which scores are available in our bucket, list the keys by specifying the prefix of `2017/score/`` and delimiter of ``/`` and then you will get a response with the common prefixes.

.. code-block:: console

	aws s3api list-objects --bucket scores --prefix 2017/score/ --delimiter / 

	COMMONPREFIXES 2017/score/english/
	COMMONPREFIXES 2017/score/maths/	
	2017/score/summary.txt

Restricting object access with pre-signed URL
---------------------------------------------

All objects and buckets are private by default. Pre-signed URLs are useful if you want your user to be able to upload a specific object to your bucket without being required to have AWS security credentials or permissions. When you create a pre-signed URL, you must provide your security credentials, bucket name, an object key, an HTTP method (PUT for uploading objects, GET for retreiving objects), and an expiration date and time. The pre-signed URLs are valid only for the specified duration.

Share the pre-signed URL with users who need to access your S3 bucket to put or retrieve objects.

Cross-Origin Resource Sharing
-----------------------------

`Cross-Origin Resource Sharing (CORS) <https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html>`_ defines a way for client web application that are loaded in one domain to interact with resources in a different domain. Consider the following examples:

* You want to host a web font in your S3 bucket. A web page in a different domain may try to use this web font. Before the browser loads this web page, it will perform a CORS check to make sure that the domain from which the page is being loaded is allowed to access resources from your S3 bucket.

* Javascript in one domain's web pages (http://www.example.com)



`Access control in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-overview.html>`_

`Amazon S3 Block Public Access – Another Layer of Protection for Your Accounts and Buckets <https://aws.amazon.com/blogs/aws/amazon-s3-block-public-access-another-layer-of-protection-for-your-accounts-and-buckets/>`_

`AWS re:Invent 2018: [Repeat] Deep Dive on Amazon S3 Security and Management (STG303-R1) <https://www.youtube.com/watch?v=x25FSsXrBqU&feature=youtu.be&t=989+%28>`_

`Using Amazon S3 Block Public Access <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html>`_

`How Do I Block Public Access to S3 Buckets? <https://docs.aws.amazon.com/AmazonS3/latest/user-guide/block-public-access.html>`_

`Using Versioning <https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html>`_

`Locking Objects Using Amazon S3 Object Lock <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`_


`New – AWS Transfer for SFTP – Fully Managed SFTP Service for Amazon S3 <https://aws.amazon.com/blogs/aws/new-aws-transfer-for-sftp-fully-managed-sftp-service-for-amazon-s3/>`_

`Multipart Upload Overview <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>`_

`AWS re:Invent 2018: [REPEAT 2] Best Practices for Amazon S3 and Amazon Glacier (STG203-R2) <https://www.youtube.com/watch?time_continue=16&v=rHeTn9pHNKo&feature=emb_logo>`_ 

Cost Factors
============

To estimate the cost of using S3, you need to consider the following:

* **Storage** (Gbs per month). The number and size of objects stored in your S3 buckets as well as the type of storage (storage class). You can reduce the costs by storing less frequently accessed data at slightly lower levels of redundancy then the Amazon S3 standard storage. It is important to note that each class has different rates.

* **Requests**. The number and type of requests. GET requests incur charges at different rates than other requests, such as PUT and COPY requests.

* **Data transfer**. The amount of data transferred out of the Amazon S3 region. Transfer into Amazon S3 is free. Transfer out from Amazon S3 to Amazon CloudFront or the same region is free of charge as well.

Amazon S3 Glacier
*****************

`Amazon S3 Storage Classes <https://aws.amazon.com/s3/storage-classes/>`_

`Coming Soon – S3 Glacier Deep Archive for Long-Term Data Retention <https://aws.amazon.com/about-aws/whats-new/2018/11/s3-glacier-deep-archive/>`_

`Object Lifecycle Management <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html>`_

.. _secStorageClasses:

Storage classes
===============

The typical lifecycle of data is the newer it is, the more frequently it is consumed. Amazon S3 offers a range of storage classes designed for different use cases. These include:

* **S3 Standard** for general-purpose storage of frequently accessed data.

* **S3 Intelligent-Tiering** for data with unknown or changing access patterns.

* **S3 Standard-Infrequent Access (S3 Standard-IA)** and **S3 One Zone-Infrequent Access (S3 One Zone-IA)** for long-lived, but less frequently accessed data. S3 Standard-IA has lower cost per GB stored and higher cost per PUT, COPY, POST or GET request. It has a 30-day storage minimum.

* **Amazon S3 Glacier** and Amazon **S3 Glacier Deep Archive** for long-term archive and digital preservation.

S3 Intelligent-Tiering
----------------------

The S3 Intelligent-Tiering storage class is designed to optimize costs by automatically moving data to the most cost-effective access tier, without performance impact or operational overhead. 

It works by storing objects in 2 access tiers: one tier that is optimized for frequent access and another lower-cost tier that is optimized for infrequent access. For a small monthly monitoring and automation fee per object, Amazon S3 monitors access patterns of the objects in S3 Intelligent-Tiering and move the ones that have not been accessed for 30 consecutive days to the infrequent access tier.

The S3 Intelligent-Tiering charges a per object monitoring fee to monitor and place an object in the optimal access tier. As a result, on a relative basis, the object fee is less when the objects are larger and thus the amount you can save is potentially higher. In the following image, you can see an example of the potential cost savings for objects stored in S3 Standard versus S3 Intelligent-Tiering. For these calculations, we assumed 10 PB of data, in US-East-1 AWS Region, and a minimum object size of 128 KB.

.. image:: /simplest_d/comparison.png

Choosing regions for your architectures
***************************************

`AWS & Sustainability <https://aws.amazon.com/about-aws/sustainability/>`_

`Save yourself a lot of pain (and money) by choosing your AWS Region wisely <https://www.concurrencylabs.com/blog/choose-your-aws-region-wisely/>`_

