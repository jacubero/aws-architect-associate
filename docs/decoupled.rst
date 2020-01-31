Building decoupled architectures
################################

Amazon SQS
**********

Asynchronous messaging
======================

If loose-coupling is important, especially in a system that requires high resilience and has unpredictable scale, another option is asynchronous messaging. Asynchronous messaging is a fundamental approach for integrating independent systems, or building up a set of loosely coupled systems that can operate, scale, and evolve independently and flexibly. As Tim Bray said, "If your application is cloud-native, or large-scale, or distributed, and doesn't include a messaging component, that's probably a bug."

When you have a monolithic application, all the communication among the different components occur internally. When you decouple the application into a microservices architecture, the communication among them can be done by messaging solutions.

In the messaging process we have several actors: the producers, the message, and the consumers. When sending messages is up to the producers and the consumers to define what the format and the contents are. You can also send attributes along with your messages, that are key/values pairs that you want to attach to your messages. This attributes can have a business meanings (for instance: ``CustomerId=1234``, ``MessageType=NewBooking``) or technical meaning (for instance: ``SourceHost=``, ``MessageType=NewBooking``)


`AWS re:Invent 2018: Choosing the Right Messaging Service for Your Distributed App (API305) <https://www.youtube.com/watch?time_continue=2&v=4-JmX6MIDDI&feature=emb_logo>`_ 

Amazon SNS
**********

The most important characteristics of SNS are the following:

* It is a flexible, fully managed pub/sub messaging and mobile communications service.

* It coordinates the delivery of messages to subscribing endpoints and clients, therefore enabling you to send different information to different subscribers.

* It is easy to setup, operate and send realiable communications. 

* It allows you to decouple and scale microservices, distributed systems and serverless communications.

Amazon SNS allows you to have pub/sub messaging for different systems in Amazon, like AWS Lambda, HTTP/S and Amazon SQS. Amazon SNS Mobile Notifications allows you to do similar publishing but to different mobile systems, like ADM, APNS, Baidu, GCM, MPNS, and WNS.

