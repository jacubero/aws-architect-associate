AWS Identity and Access Management (IAM)
########################################

IAM
***

AWS Identity and Access Management (IAM) is a web service for securely controlling access to AWS services. With IAM, you can centrally manage users, security credentials such as access keys, and permissions that control which AWS resources users and applications can access.

.. image:: /security_d/intro-diagram _policies_800.png
   	:align: center

A **user** is a permanent named operator. It could be a human or it could be a machine. Their credentials are permanent and they stay with that named user until there is a forced rotation, whether it's a name and password, whether it's an access key, secret key combination ,etc. This is my *authentication method* for named users in the system.

A **group** is a collection of users. Groups can have many users, users can belong to many groups.

A **role** is an operation (human or machine) and its credentials are temporary. It is the authentication method for the user.

Permissions happens in a separate object known as the **policy document**. A policy specifies resources and the operations that can be perform on these resources. It is a JSON document and attaches either a permanent named user or to a group of users, or to a role. I lists the specific API or wuilcard group of APIs that are white-listed.

Identities in AWS exist in these forms:

* **IAM users**: Users created within the account. IAM users are created with no permissions by default. 

* **Roles**: Temporary identities used by EC2 instances, Lambdas, and external users.

* **Federation**: Users with Active Directory identities or other corporate credentials have role assigned in IAM.

* **Web Identity Federation**: Users with web identities from Amazon.com or other Open ID provier have role assigned using Security Token System (STS).


`Secure Access to AWS Services Using AWS Identity and Access Management (IAM) Roles <https://www.youtube.com/watch?v=wY7FOFaPNuE&feature=emb_logo>`_ 

`How to Enable Multi-Factor Authentication (MFA) for Your AWS User Account <https://www.youtube.com/watch?v=A3AObXBJ4Lw&feature=emb_logo>`_


`AWS re:Invent 2018: [REPEAT 1] Become an IAM Policy Master in 60 Minutes or Less (SEC316-R1) <https://www.youtube.com/watch?time_continue=2&v=YQsK4MtsELU&feature=emb_logo>`_

`Deep Dive on AWS Single Sign-On - AWS Online Tech Talks <https://www.youtube.com/watch?v=8jyhsnh0ALQ>`_

SAML 2.0-based Federation
-------------------------

AWS supports identity federation with SAML 2.0 (Security Assertion Markup Language 2.0), an open standard that many identity providers (IdPs) use, such as Active Directory. This feature enables federated single sign-on (SSO), so users can log into the AWS Management Console or call the AWS API operations without you having to create an IAM user for everyone in your organization. By using SAML, you can simplify the process of configuring federation with AWS, because you can use the IdP's service instead of writing custom identity proxy code.

AWS Directory Service
*********************

AWS Directory Service provides multiple ways to use Amazon Cloud Directory and Microsoft Active Directory (AD) with other AWS services. Directories store information about users, groups, and devices, and administrators use them to manage access to information and resources. AWS Directory Service provides multiple directory choices for customers who want to use existing Microsoft AD or Lightweight Directory Access Protocol (LDAP)–aware applications in the cloud. It also offers those same choices to developers who need a directory to manage users, groups, devices, and access.

AWS Web Application Firewall (WAF)
**********************************

It helps protect web applications from common web exploits gat could affect application availability, compromise security, or consume excessive resources unexpectedly.

AWS WAF gives customers control over which traffic to allow or block to their web applications by defining customizable web security rules. Customers can use AWS WAF to create rules that block common attack patterns, such as SQL injection or cross-site scripting, as well as rules tailored to their specific application.

New rules can be deployed within minutes in response to changing traffic patterns. Also, AWS WAF includes a full-featured API that customers can use to automate the creation, deployment, and maintenance of web security rules. AWF integrates with services such as CloudFront and ELB, allowing customers to enforce security at the AWS edge, before traffic even reaches customer application infrastructure.

AWS Shield
**********

AWS Shield Standard
===================

AWS Shield is a managed DDoS protection service that safeguards applications running on AWS. There are 2 tiers of AWS Shield: Standard and Advanced.

.. figure:: /appendix_d/standard.png
   :align: center

	AWS Shield Standard

AWS Shield Standard protects applications running on AWS by providing always-on detection and automatic inline mitigations of DDoS attacks, to minimize application downtime and performance degradation. All AWS customers benefit from the automatic protections of AWS Shield Standard, at no additional charge. It defends against most common, frequently ocurring network and transport layer DDoS attacks that target web sites or applications. It integrates with Amazon CloudFront and Amazon Route 53, to provide comprehensive availability protection against many types of infrastructure attacks. 

A combination of traffic signatures, anaomaly alogorithms and other analysis techniques are employed to detect malicious traffic in real-time. Automated mitigation techniques are built into this service, applied inline to your applications so there is no latency impact. Several techniques, such as deterministic packet filtering and priority-based traffic shaping are used to automatically mitigate attacks without impacting your applications. You can mitigate application layer attacks by writing rules using AWS WAF, only paying for what you use. It is a self service and there is no need to engage AWS support to receive protection against DDoS attacks.

AWS Shield Advanced
===================

.. figure:: /appendix_d/advanced.png
   :align: center

	AWS Shield Advanced

Customers can also subscribe to AWS Shield Advanced. It provides additional detection and mitigation against large and sophisticated DDoS attacks. It provides near real-time visibility and integrates with AWS WAF. It gives customers 24x7 access to the AWS DDoS Response Team (DRT) and protection against DDoS-related spikes in their EC2, ELB, CloudFront and Route 53 charges. DRT can be engaged before, during, or after an attack. The DRT will triage incidents, identify root causes, and apply mitigations on your behalf. They can also assist you with post attack analysis. AWS Shield Advanced is available globally on Amazon CloudFront and Amazon Route 53 edge locations.

Using advaced routing techniques, this service tier provides additional capacity to protect against larger DDoS attacks. For application layer attacks, you can use AWS WAF to set up proactive rules like Rate-based Blacklisting to automatically stop bad traffic or respond immediately, all at no additional charge. You'll have complete visibility into DDoS attacks with near real-time notification through Amazon CloudWatch and detailed diagnostics on the management console. AWS Shield Advanced monitors application layer traffic to your Elastic IP addresses, ELB, CloudFront or Route 53 resources. It detects application layer attacks like HTTP floods or DNS query floods by baselining traffic on your resource and identifying anomalies. If any of these services scale up in response to a DDoS attack, AWS will provide service credits for charges due to usage spikes.

Protecting DNS
==============

AWS Shield Standard protects your Amazon Route 53 Hosted Zones from infrastructure layer DDoS attacks, including reflection attacks or SYN floods that frequently target DNS. A variety of techniques, such as header validationss and pritority-based traffic shaping, automatically mitigate these attacks.

AWS Shield Advanced provides greater protection, visibility into attacks on your Route 53 infrastructure, and help from AWS response team for extreme excenarios.

Protecting web applications and APIs
====================================

When using Amazon CloudFront, AWS Shield Standard provides comprehensive protection against infrastructure layer attacks like SYN floods, UDP floods, or other reflection attacks. Always-on detection and mitigation systems automatically scrub bad trafic at layer 3 and 4 to protect your application.

With AWS Shield Advanced the AWS response team actuvely applies any mitigations necessary for sophisticated infrastructure layer 3 or 4 attacks using traffic engineering. Application layer attacks, like HTTP floods, are also protected.

The always-on detection system baselines customers' steady-state application traffic and monitors for anomalies. Using AWS WAF, you can customize any application layer mitigation.

Protecting other applications
=============================

For other custom applications, not based on TCP (for example UDP and SIP), you cannot use services like Amazon CloudFront or ELB. In these cases, you often need to run your application directly on internet-facing EC2 instances.

AWS Shield Standard protects your EC2 instance from common infrastructure layer 3 or 4 attacks, such as UDP reflection attacks that include DNS, NTP, and SSDP reflection attacks. Techniques, such as priority-based traffic shaping, are automatically engaged when a well-defined DDoS attack signature is detected.

With AWS Shield Advanced on Elastic IP address, you have enhanced detection that automatically recognizes the type of AWS resource and size of EC2 instance and applies pre-defined mitigators. You can create custom mitigation profiles, and during the attack, all your Amazon VPC NACLs are automatically enforced at the border of the AWS network, giving you access to additional bandwidth and scrubbing capacity to mitigate large volumetric DDoS attacks. It also protects against SYN floods or other vectors, such as UDP floods.

Amazon Inspector
****************

Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. The service automatically assesses applications for vulnerabilities or deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed report with prioritized steps for remediation.

It is agent-based, API-driven, and delivered as a service. This makes it easy for you to build right into your existing DevOps process, decentralizing and automating vulnerability assessments, and empowering your DevOps teams to make security assessment an integral part of the deployment process.

