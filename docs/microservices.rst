Microservices and serverless architectures
##########################################

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

`Introduction to AWS Lambda & Serverless Applications <https://www.youtube.com/watch?time_continue=4&v=EBSdyoO3goc&feature=emb_logo>`_ 

`Building APIs with Amazon API Gateway <https://www.youtube.com/watch?v=XwfpPEFHKtQ&feature=emb_logo>`_




