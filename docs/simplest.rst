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

`Amazon S3 Storage Classes <https://aws.amazon.com/s3/storage-classes/>`_

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

.. figure:: /simplest_d/font.png
   :align: center

   CORS use case example

* Javascript in one domain's web pages (http://www.example.com) wants to use resources from your S3 bucket by using the endpoint ``website.s3.amazonaws.com``. The browser will allow such cross-domain access only if CORS is enabled on your bucket.

With CORS support in S3, you can build web applications with S3 and selectively allow cross-origin access to your S3 resources.

To enable CORS, create a CORS configuration XML file with rules that identify the origins that you will allow to access your bucket, the operations (HTTP methods) that you will support for each origin, and other operation-specific information. You can add up to 100 ules to the configuration. You can apply the CORS configuration to the S3 bucket by using the AWS SDK.

Managing access
---------------

`Access control in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-overview.html>`_

Access policies
^^^^^^^^^^^^^^^

By default, all S3 resources (buckets, objects, and related sub-resources) are private, only the resource owner, and AWS account that created it, can access the resource. The resource owner can optionally grant access permissions to others by writing and access policy. By default, any permission that is not granted Allow access is an implicit Deny. There are 2 types of access policies: resource-based and user-based policies. 

* Access policies which are attached to your resources (buckets and objects) are referred to as resource-based policies. For example: bucket policies and ACLs are resource-based policies.

.. code-block:: JSON

	{
	    "Version": "2012-10-17",
	    "Statement": [
	        {
	            "Action": [
	                "s3:GetObject",
	                "s3:ListBucket"
	            ],
	            "Effect": "Allow",
	            "Resource": "arn:aws:s3:::MYEXAMPLEBUCKET",
	            "Principal": {
	            	"AWS": [
	            		"arn:aws:iam::123456789012:user/testuser"
	            	]
	            }
	        }
	    ]
	}

* Access policies which are attached to users in your account are called user policies. 

.. code-block:: JSON

	{
	    "Version": "2012-10-17",
	    "Statement": [
	        {
	            "Action": [
	                "s3:GetObject",
	                "s3:ListBucket"
	            ],
	            "Effect": "Allow",
	            "Resource": "arn:aws:s3:::<bucket_name>/<key_name>",
	        }
	    ]
	}

You may choose to use resource-based policies, user policies, or some combination of these to manage permissions to your S3 resources. Both bucket policies and user policies are written in JSON format and not easily distinguishable by looking at the policy itself, but by looking at what the policy is attached to, it should help you figure out which type of policy it is. The `AWS Policy Generator <https://awspolicygen.s3.amazonaws.com/policygen.html>`_ is a tool that enables you to create policies that control access to AWS products and resources.

Access Control Lists
^^^^^^^^^^^^^^^^^^^^

ACLs are coarse grained and you can only apply rules at the bucket or object level. They are much more limited in the fact that you can only use ACLs to grant access to other AWS accounts and not IAM users in the same account where the bucket resides.

.. figure:: /simplest_d/ACL.png
   :align: center

   ACL expanded view

Data at rest encryption
-----------------------

For data at rest protection in S3 you have 2 options: Server-Side Encryption and Client-Side Encryption. 

When using server-side encryption, your request S3 to encrypt your object saving it on disks in its data centers and decrypt it when you download the object. With server side encryption there are a few ways in which you can choose to implement the encryption. You have 3 server-side encryption options for your S3 objects:

* SSE-S3 with keys that are managed by S3.

* SSE-KMS with keys that are managed by AWS KMS.

* SSE-C with keys that you manage.

Additionally using Default Encryption, you can encrypt all your objects with SSE-S3 or SSE-KMS.

Client side encryption happens before your daa is uploaded. You an encrypt your data before uploading into your S3 bucket.

Data Transfer
-------------

You may need a variety of tools to move or transfer data in and out the cloud, depending on your data size and time to transfer. These are the options:

* **AWS Direct Connect** is a dedicated network connection from your on-premises data center to AWS for higher throughput an secure data transfer without traversing Internet.

* **AWS Storage Gateway**, either with or without AWS Direct Connect. This is a virtual appliance that lets you connect to your bucket as an NFS mount point.

* **Third-party connectors (ISV connectors)**. Amazon partners can help you move your data to the cloud. The simplest way to do that may be via a connector embedded in your backup software. With this approach, your backup catalog stays consistent, so you maintain visibility and control across jobs that span disk, tape and cloud.

* You can stream data into S3 via **Amazon Kinesis Firehose**, a fully managed streaming service. Because it captures and automatically loads streaming data into S3 and Amazon Redshift, you get near real-time analytics with the business intelligence tools you're already using.

* **Amazon Kinesis Video Streams** makes it easy to securely stream video from connected devices to AWS for analytics, machine learning, and other processing. Kinesis Video Streams automatically provisions and elastically scales all the infrastructure needed to ingest streaming video data from millions of devices. Kinesis Video Streams uses S3 as the underlying data store, which means your data is stored durably and reliably. You can set and control retention periods for data stored in your streams.

* **Amazon Kinesis Data Streams** enables you to build custom applications that process or analyze streaming data for specialized needs. Kinesis Data Streams can continously capture and store TBs of data per hour from hundreds of thousands of sources such as website clickstreams, financial transactions, social media feeds, IT logs, and location-tracking events. You can also emit data from Kinesis Data Streams to other AWS services such as S3, Amazon Redshift, EMR, AWS Lambda.

* **Amazon S3 Transfer Acceleration** is used for fast, easy, and secure transfers of files over long distances. It takes advantage of CloudFront's globally distributed edge locations, routing data to S3 over an optimized network path. Transfer Acceleration works well for customers who either transfer data to a central location from all over the world, or who transfer significant amounts of data across continents regularly. It can also help yu better utilize your available bandwidth when uploading to S3.

* For large data migrations where transferring over a network would be too time consuming or costly, use **AWS Snowball, Snowball Edge or Snowmobile**. These are for petabyte-scale and exabyte-scale data transport that use secure appliances to transfer large amounts of data into and out of AWS. 

Bear in mind that you can also use these methods for exporting your data. `Cloud Data Migration <https://aws.amazon.com/cloud-data-migration/>`_.

.. code-block:: console
	:caption: Create a bucket and upload data to Amazon S3 using the CLI

	c:\mydata> aws s3 mb s3://myappbucket6353 --region us-east-1
	make_bucket: myappbucket6353

	c:\mydata> aws s3 ls
	2013-07-11 17:08:50 mybucket
	2013-07-24 14:55:44 myappbucket6353

	c:\mydata> aws s3 cp c:\mydata s3://myappbucket6353 --recursive 
	upload: myDir/test1.txt to s3://myappbucket635/myDir/test1.txt
	upload: myDir/test2.txt to s3://myappbucket635/myDir/test1.txt
	upload: test3.txt to s3://myappbucket635/test3.txt

	c:\mydata> aws s3 ls s3://myappbucket6353
	                           PRE myDir/
	2013-07-25 17:06:27         88 test3.txt

Amazon S3 Select
----------------

S3 Select is a new S3 capability designed to pull out only the data you need from an object using a SQL expression, dramatically improving the performance and reducing the cost of applications that need to access data in S3. Most applications have to retrieve the entire objetct and then filter ut only the required data for further analysis. S3 Select enables applications to offload the heavy lifting of filtering and accessing data inside objects to the S3 service. By reducing the volume of daa that has to be loaded and processed by your applications, S3 Select can improve the performance of most applications that frequently access data from S3 by up to 400%.

Amazon S3 Select works like a GET request as it is an API call. But where Amazon S3 Select is different is we are asking for data within an object that matches a set of criteria, rather than just asking to get an entire object. You can use Amazon S3 Select through the available Presto connector, with AWS Lambda, or from any other application using the S3 Select SDK for Java or Python. In the query, you use an standard SQL expression.

Amazon S3 Select works on objects stored in delimited test (CSV, TSV) or JSON format. It also works with objects that are compressed with GZIP, and server-side encrypted objects. You can specify the format of the results as either delimited test (CSV, TSV) or JSON, and you can determine how the records in the result will be delimited. To retreive the information you need, you pass SQL expressions to S3 in the request. Amazon S3 Select supports a subset of SQL as listed in bale below. 

.. figure:: /simplest_d/select.png
   :align: center

   SQL queries with Amazon S3 Select

`Selecting Content from Objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/selecting-content-from-objects.html>`_

There are a few ways you can use Amazon S3 Select. You can perform SQL queries using AWS SDKs, the SELECT Object Content REST API, the AWS CLI, or the Amazon S3 console. When using the Amazon S3 console, it limits the amount of data returned to 40 MB.

Securing your data in Amazon S3
===============================

In the decision process for determining access to your bucket and objects, S3 starts with a default deny to everyone. When you create a bucket, the owner is granted access, and as the owner you can then allow access to other users, groups, roles and resources. When determining the authorization of access to your resource in S3, it is always a union of user policies, resource policies and ACLs. In accordance with the principle of least-privilege decisions default to DENY, and an explicit DENY always trumps an ALLOW. 

.. figure:: /simplest_d/access.png
   :align: center

   Access decision process

For example, assume there is an IAM policy that grants a user access to a bucket. Additionally, there is a bucket policy defined with an explicit DENY for the user to the same bucket. When the user tries to access the bucket, the access is denied.

Keep in mind that if no policy or ACLs specifically grants ALLOW access to a resource the entity will be denied access by default. Only if no policy or ACLs specifies a DENY an one or more policies or ACLs specify an ALLOW will be the request be allowed.

Policies
--------

A policy is an entity in AWS that, when attached to an identity or resource, defines the permissions. AWS evaluates these policies when a principal, such as a user, makes a request. Permissions in the policies determine whether the request is allowed or denied. Policies are stored in AWS as JSON documents attaches to principals as identity-based policies, or to resources as resource-based policies. 

The language elements that are used in a policy are the following:

* **Resources**. The Resource element specifies the buckets or objects that the statement covers. Buckets and objects are the S3 resources for which you can allow or deny permissions. In a policy, you use the Amazon Resource Name (ARN) to identify the resource. For example, your resource could be just the bucket or it could be a bucket and objects, a bucket and subset of objects or even a specific object.

* **Actions**. For each resource, S3 support a set of operations. You identify resource operations you want to allow or deny by using action keywords. You specify a value using a namespace that identifies the service, for example s3, followed by the name of the action. The name must match an action that is supported by the service. The prefix and the action name are case insensitive. You can use wilcards * to allow all operations for a service.

* **Effect**. This is what the effect will be when the user requests the specific action, this can be either allow or deny. If you do not explicitly grant allow access to a resource, access in implcitly denied. You can also explicitly deny access to a resource, which you might do in order to make sure that a user cannot access it, even if a different policy grants access. For example, you may want to explicitly deny the ability to delete objects in a bucket.

* **Principal**. Use the pricipal element to specify the user (IAM user, federated user, or assumed-role user), AWS account, AWS service, or other principal entity that is allowed or denied access to a resource. You specify a principal only in a resource policy, for example a bucket policy. It is the user, account, role, service, or other entity who is the recipient of this permission. When using an IAM policy, the user, group or role to which the policy is attached is the implicit principal.

* **Conditions**. You can optionally add a Condition element (or Condition block) to specify conditions for when a policy is in effect. In the Condition element, you build expressions in which you can use condition operators (equal, less than, etc.) to match the condition in the policy against values in the request. Condition values can include date, time, the IP address of the requester, the ARN of the request source, the user name, user ID, and the user agent of the requester. Some services let you specify additional values in conditions; for examples S3 lets you write condition suing items such as object tags (s3:RequestObjectTag) to grant or deny the appropriate permission to a set of objects. 

`Bucket Policy Examples <https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html>`_ 

`Example IAM Identity-Based Policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html>`_ 

There are some additional elements that can be used in policies: NotPrincipal, NotAction, and NotResource. 

You can use the **NotPrincipal** element to specify and exception to a list of principals. For example, you can deny access to all principals except the one named in the NotPrincipal element. 

Although you can use the NotPrincipal with an Allow, when you use NotPrincipal in the same policy statement as "Effect":"Allow", the permissions specified in the policy statment will be granted to all principals excepts the one(s) specified, including anonymous (unauthenticated) users. It is recommended not yo use NotPrincipal in the same policy statement as "Effect":"Allow".

When creating a policy, combining "Deny" and "NotPrincipal" is the only time that the order in which AWS evaluated principals makes a difference. AWS internally validates the principals from the "top down", meaning that AWS checks the account first and then the user. If an assumed-role user (someone who is using a role rather than an IAM user) is being evaluated, AWS looks ata the account first, then the role, and finally the assumed-role user. The assumed-role user is identified by the role session name that is specified when the user assumes the role. Normally, this order does not have any impact on the results of the policy evaluation. However, when you use both "Deny" and "NotPrincipal", the evaluation order requires you to explicitly include the ARNs for the entities associated with the specified principal. For example, to specify a user, you must explicitly include the ARN for the user's account. To specify an assumed-role user, you must also include both the ARN for the role and the ARN for the account containing the role.

The **NotAction** is an advanced policy element that explicitly matches everything except the expecified list of actions and it can be used with both the Allow and Deny effect. Using NotAction can result in a shorter polciy by listing only a few actions that should not match, rather then including a long list of actions that will match. When using NotAction, you should keep in mind that actions specified in this element are the only actions that are limited. This means that all of the actions or services that are not listed, are allowed if you use the Allow effect, or are denied if you use the Deny effect.

You can use the NotAction element in a statement with "Effect":"Allow" to provide access to all of the actions in an AWS service, except for the actions specified in NotAction. You can also use it with the Resource element to provide access to one or more resources with the exception of the action specified in the NotAction element. 

Be careful using the NotAction and "Effect":"Allow" in the same statement or in a different statement within a policy. NotAction matches all services and actions that are not explicitly listed, and could result in granting users more permissions that you intended.

You can also use the NotAction element in a statement with "Effect":"Deny" to deny access to all of the listed resources except for the actions specified in the NotAction element. This combination does not allow the listed items, but instead explicitly denies the actions not listed. You must still allos actions that you want to allow.


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

