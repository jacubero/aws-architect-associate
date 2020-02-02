Microservices and serverless architectures
##########################################

Amazon ECS
**********

Amazon ECS enables you to inject sensitive data into your containers by storing your sensitive data in either AWS Secrets Manager secrets or AWS Systems Manager Parameter Store parameters and then referencing them in your container definition. This feature is supported by tasks using both the EC2 and Fargate launch types. Secrets can be exposed to a container in the following ways:

* To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter.

* To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter.

.. figure:: /microservices_d/ecs-secret.png
   :align: center

   AWS Lambda

Within your container definition, specify ``secrets`` with the name of the environment variable to set in the container and the full ARN of either the Secrets Manager secret or Systems Manager Parameter Store parameter containing the sensitive data to present to the container. The parameter that you reference can be from a different Region than the container using it, but must be from within the same account.

AWS Lambda 
**********

There are 4 main principles that allows us to identify if a service is serverless or not:

* There are no servers to provision or manage.

* It scales with usage.

* You pay for value. You don't need to pay for the time the resource is idle.

* It has availability and fault tolerance built in. In AWS, serverless take advantage of the availability and fault tolerance given by AWS global infrastructure.

.. figure:: /microservices_d/lambda.png
   :align: center

   AWS Lambda

AWS Lambda handles load balacing, auto scaling, failures, security isolation, OS management, ... for you.

Serverless applications have 3 components: the event source, that triggers the AWS Lambda function, which calls some **services**.

* **Event sources** can be changes in changes in data state, requests to endpoints, changes in resource state.

* **Functions** that can be developed in Node.js, Python, Java, C#, Go, Ruby, Runtime API.

The anatomy of a Lambda function is as follows:

* **Handler() function** is the function to be executed upon invocation.

* **Event object** is data sent during Lambda function invocation.

* **Context object** are the methods available to interactwith runtime information (equest ID,log group, more).

AWS Lambda runtime API and layers are features that allow developers to share, discover, and deploy both libraries and languages as part of their serverless applications. Runtime API enables developers to use Lambda with any programming language. Layers let functions easily share code. Upload layer once, reference within any function. Layers promote separation of responsibilities, lets developers focus on writing business logic. Combined, runtime API and layers allow developers to share any programming language or language version with others.

There are 3 types of Lambda execution models:

* **Synchronous (push)**. For instance, an Amazon API Gateway request to AWS Lambda functions and expect some response.

* **Asynchronous (event)**. For instance, a Amazon SNS invocates AWS Lambda function and it makes some task on it without sending nothing to the client.

* **Poll-based**. For instance, Amazon DynamoDB Streams or Amazon Kinesis streams are continously poll and Lambda makes an invocation for you.

The Lambda permission model allows you to establish fine-grained security controls for both execution and invocation:

* **Execution policies**. They define what AWS resources/API calls can this function access via IAM and is used in streaming invocations. For instance: Lambda function A can read from DynamoDB table users.

* **Function policies** are used for sync and async invocations. For example: Actions on bucket X can invoke Lambda function Z.

`Introduction to AWS Lambda & Serverless Applications <https://www.youtube.com/watch?time_continue=4&v=EBSdyoO3goc&feature=emb_logo>`_ 

`Building APIs with Amazon API Gateway <https://www.youtube.com/watch?v=XwfpPEFHKtQ&feature=emb_logo>`_

Environment Variables
---------------------

When you create or update Lambda functions that use environment variables, AWS Lambda encrypts them using the AWS Key Management Service. When your Lambda function is invoked, those values are decrypted and made available to the Lambda code.

.. figure:: /microservices_d/environment.png
   :align: center

   AWS Lambda Environment Variables

Lambda encrypts environment variables with a key that it creates in your account (an AWS managed customer master key). Use of this key is free. You can also choose to provide your own key for Lambda to use instead of the default key.

However, if you wish to use encryption helpers and use KMS to encrypt environment variables after your Lambda function is created, you must create your own AWS KMS key and choose it instead of the default key. The default key will give errors when chosen. Creating your own key gives you more flexibility, including the ability to create, rotate, disable, and define access controls, and to audit the encryption keys used to protect your data.

When you provide the key, only users in your account with access to the key can view or manage environment variables on the function. Your organization may also have internal or external requirements to manage keys used for encryption and control when they are rotated.

You can also encrypt environment variable values client-side before sending them to Lambda, and decrypt them in your function code. This obscures secret values in the Lambda console and API output, even for users who have permission to use the key. In your code, you retrieve the encrypted value from the environment and decrypt it by using the AWS KMS API.

Pricing
=======

You buy compute time in 100ms increments. There is no hourly, daily, or monthly minimums and no per-device fees. You never pay for idle time. The free tier covers 1 million requests and 400,000 GBs of compute every month, every customer.

Lambda exposes only a memory control, with the percentage of CPU core and network capacity allocated to a function proportionally. If your code is CPU, network or memory-bound, then it could be cheaper to choose more memory.

Amazon API Gateway
******************

Amazon API Gateway creates a unified API frontend for multiple microservices. It provides DDos protection and throttling for your backend. It allows you to authenticate and authorize requests to a backend. It can throttle, meter and monitize API usage by third-party developers.

Amazon API Gateway provides throttling at multiple levels including global and by service call. Throttling limits can be set for standard rates and bursts. For example, API owners can set a rate limit of 1,000 requests per second for a specific method in their REST APIs, and also configure Amazon API Gateway to handle a burst of 2,000 requests per second for a few seconds. Amazon API Gateway tracks the number of requests per second. Any request over the limit will receive a 429 HTTP response. The client SDKs generated by Amazon API Gateway retry calls automatically when met with this response. 

You can add caching to API calls by provisioning an Amazon API Gateway cache and specifying its size in gigabytes. The cache is provisioned for a specific stage of your APIs. This improves performance and reduces the traffic sent to your back end. Cache settings allow you to control the way the cache key is built and the time-to-live (TTL) of the data stored for each method. Amazon API Gateway also exposes management APIs that help you invalidate the cache for each stage.

.. figure:: /microservices_d/api-gw-settings.png
   :align: center

   Amazon API Gateway settings

`Building APIs with Amazon API Gateway <https://www.youtube.com/watch?time_continue=91&v=XwfpPEFHKtQ&feature=emb_logo>`_
