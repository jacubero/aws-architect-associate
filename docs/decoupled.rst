Building decoupled architectures
################################

Amazon SQS
**********

Asynchronous messaging
======================

If loose-coupling is important, especially in a system that requires high resilience and has unpredictable scale, another option is asynchronous messaging. Asynchronous messaging is a fundamental approach for integrating independent systems, or building up a set of loosely coupled systems that can operate, scale, and evolve independently and flexibly. As Tim Bray said, "If your application is cloud-native, or large-scale, or distributed, and doesn't include a messaging component, that's probably a bug."

When you have a monolithic application, all the communication among the different components occur internally. When you decouple the application into a microservices architecture, the communication among them can be done by messaging solutions.

In the messaging process we have several actors: the producers, the message, and the consumers. When sending messages is up to the producers and the consumers to define what the format and the contents are. You can also send attributes along with your messages, that are key/values pairs that you want to attach to your messages. This attributes can have a business meanings (for instance: ``CustomerId=1234``, ``MessageType=NewBooking``) or technical meaning (for instance: ``SourceHost=ec2-203-0-113-25.compute-1.amazonaws.com``, ``ProgramName=WebServer-PID:9989``). The payload can be encrypted but the attributes cannot. The attributes can be used to filter messages.

The AWS messaging services can be classified in terms of the use:

* **Modern application development**, which are ideal for born-in-the-cloud apps. They have simple APIs and offer unlimited throuhput. We have Amazon SQS for dealing queues, Amazon SNS for subscribing to topics, Amazon Kinesis for dealing streams.

* **App migration**, which are API-compatible, feature-rich and use standard protocols. We have Amazon MQ as a message broker.

`AWS re:Invent 2018: Choosing the Right Messaging Service for Your Distributed App (API305) <https://www.youtube.com/watch?time_continue=2&v=4-JmX6MIDDI&feature=emb_logo>`_ 

Basic Amazon SQS Architecture
=============================

Distributed Queues
------------------

There are three main parts in a distributed messaging system: the components of your distributed system, your queue (distributed on Amazon SQS servers), and the messages in the queue.

In the following scenario, your system has several producers (components that send messages to the queue) and consumers (components that receive messages from the queue). The queue (which holds messages A through E) redundantly stores the messages across multiple Amazon SQS servers.

.. figure:: /decoupled_d/SQSArchOverview.png
   :align: center

	 Amazon SQS architecture

Message Lifecycle
-----------------

The following scenario describes the lifecycle of an Amazon SQS message in a queue, from creation to deletion.

.. figure:: /decoupled_d/sqs-message-lifecycle-diagram.png
   :align: center

	 Amazon SQS message lifecycle

1. A producer (component 1) sends message A to a queue, and the message is distributed across the Amazon SQS servers redundantly.

2. When a consumer (component 2) is ready to process messages, it consumes messages from the queue, and message A is returned. While message A is being processed, it remains in the queue and isn't returned to subsequent receive requests for the duration of the visibility timeout.

3. The consumer (component 2) deletes message A from the queue to prevent the message from being received and processed again when the visibility timeout expires.

.. Note::

	Amazon SQS automatically deletes messages that have been in a queue for more than maximum message retention period. The default message retention period is 4 days. However, you can set the message retention period to a value from 60 seconds to 1,209,600 seconds (14 days) using the ``SetQueueAttributes`` action.

Amazon SQS Standard Queues
==========================

Amazon SQS offers standard as the default queue type. Standard queues support a nearly unlimited number of transactions per second (TPS) per API action (``SendMessage``, ``ReceiveMessage``, or ``DeleteMessage``). Standard queues support at-least-once message delivery. However, occasionally (because of the highly distributed architecture that allows nearly unlimited throughput), more than one copy of a message might be delivered out of order. Standard queues provide best-effort ordering which ensures that messages are generally delivered in the same order as they're sent.

You can get duplicate messages for instance in this scenario:

1. A producer sends a message to the queue.

2. There is a networking problem when the producer was calling send message.

3. The queue stores the message durably.

4. The producer gets a timeout. It doesn't know if SQS got the message or it didn't.

5. The producer retry the sent.

6. SQS standard will store a duplicate of the message.

When you want to consume messages, the only thing you want to do is to call receive message and provide the queue URL. You do not have to tell SQS which message you want to receive, it is the responsibility of SQS to select the best message to give to you. 

When the consumer gets the receive message, the SQS get the message and gives it to the consumer. The consumer can start working on it, but notice that the message is still in the queue. It is not immediately removed, it is invisible, and you can control the invibility timeout. This invisibility timeout makes sure that if another consumer wants to fetch another message, SQS won't give you this particular message because some consumer is already working on it.

When the consumer successfully consumes the message, call the delete message on the message that it got, which actually achieves the removal of the message. Only when the consumer acknowledges that it successfully consumed the message, the message is removed from the queue. This guarantees that the message is consumed at least once.

When the consumer has a problem consuming the message, the easiest solution for the consumer is just forget about the message and do nothing. What happen next is that the invisibility timeout on the message it was working on expires, and the message is available for consumption again.

Amazon SQS Visibility Timeout
-----------------------------

When a consumer receives and processes a message from a queue, the message remains in the queue. Amazon SQS doesn't automatically delete the message. Because Amazon SQS is a distributed system, there's no guarantee that the consumer actually receives the message (for example, due to a connectivity issue, or due to an issue in the consumer application). Thus, the consumer must delete the message from the queue after receiving and processing it.

.. figure:: /decoupled_d/sqs-visibility-timeout-diagram.png
   :align: center

	 Amazon SQS visibility timeout

Immediately after a message is received, it remains in the queue. To prevent other consumers from processing the message again, Amazon SQS sets a visibility timeout, a period of time during which Amazon SQS prevents other consumers from receiving and processing the message. The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours. 

Message Ordering
----------------

A standard queue makes a best effort to preserve the order of messages, but more than one copy of a message might be delivered out of order. If your system requires that order be preserved, we recommend using a FIFO (First-In-First-Out) queue or adding sequencing information in each message so you can reorder the messages when they're received.

At-Least-Once Delivery
----------------------

Amazon SQS stores copies of your messages on multiple servers for redundancy and high availability. On rare occasions, one of the servers that stores a copy of a message might be unavailable when you receive or delete a message.

If this occurs, the copy of the message isn't deleted on that unavailable server, and you might get that message copy again when you receive messages. Design your applications to be idempotent (they should not be affected adversely when processing the same message more than once).

Amazon SQS FIFO (First-In-First-Out) Queues
===========================================

FIFO queues have all the capabilities of the standard queue. FIFO (First-In-First-Out) queues are designed to enhance messaging between applications when the order of operations and events is critical, or where duplicates can't be tolerated. FIFO queues also provide exactly-once processing but have a limited number of transactions per second (TPS):

* By default, with batching, FIFO queues support up to 3,000 messages per second (TPS), per API action (``SendMessage``, ``ReceiveMessage``, or ``DeleteMessage``). To request a quota increase, submit a support request.

* Without batching, FIFO queues support up to 300 messages per second, per API action (``SendMessage``, ``ReceiveMessage``, or ``DeleteMessage``).

.. Note::

	Amazon SNS isn't currently compatible with FIFO queues.

	The name of a FIFO queue must end with the .fifo suffix. The suffix counts towards the 80-character queue name quota. To determine whether a queue is FIFO, you can check whether the queue name ends with the suffix.

Typically what you need is to process messages in sequence for specific subgroup of messages, such as Customer ID, but you can work with multiple customers in parallel. To send the message to the FIFO queue, the producer must to tell what the message group for which the message belongs to. It is just a tag that you put in the message and it is not necessary to pre-create this group. There is no limitation of the number of messages that you can send.

Image an scenario where:

1. A producer sends a message to the queue.

2. There is a networking problem when the producer was calling send message.

3. The queue stores the message durably.

4. The producer gets a timeout. It doesn't know if SQS got the message or it didn't.

5. The producer retry the sent.

6. SQS keeps track of the identifiers of the messages sent to it in the last 5 minutes, even if they are already consumed. As a consequence, it is able to detect that it is retry of sending the same message and no duplicate is introduced in the queue. An OK is returned to the producer, because the message is already present.

When the consumer calls receive and FIFO decides the group you are are going to get messages.

Amazon SNS
**********

The most important characteristics of SNS are the following:

* It is a flexible, fully managed pub/sub messaging and mobile communications service.

* It coordinates the delivery of messages to subscribing endpoints and clients, therefore enabling you to send different information to different subscribers.

* It is easy to setup, operate and send realiable communications. 

* It allows you to decouple and scale microservices, distributed systems and serverless communications.

Amazon SNS allows you to have pub/sub messaging for different systems in Amazon, like AWS Lambda, HTTP/S and Amazon SQS. Amazon SNS Mobile Notifications allows you to do similar publishing but to different mobile systems, like ADM, APNS, Baidu, GCM, MPNS, and WNS.

