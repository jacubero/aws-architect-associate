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

An IAM role is similar to a user in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Also, a role does not have standard long-term credentials (password or access keys) associated with it. Instead, if a user assumes a role, temporary security credentials are created dynamically and provided to the user.

You can use roles to delegate access to users, applications, or services that don't normally have access to your AWS resources. For example, you might want to grant users in your AWS account access to resources they don't usually have, or grant users in one AWS account access to resources in another account. Or you might want to allow a mobile app to use AWS resources, but not want to embed AWS keys within the app (where they can be difficult to rotate and where users can potentially extract them). Sometimes you want to give AWS access to users who already have identities defined outside of AWS, such as in your corporate directory. Or, you might want to grant access to your account to third parties so that they can perform an audit on your resources.

Permissions happens in a separate object known as the **policy document**. A policy specifies resources and the operations that can be perform on these resources. It is a JSON document and attaches either a permanent named user or to a group of users, or to a role. It lists the specific API or wilcard group of APIs that are white-listed.

Identities in AWS exist in these forms:

* **IAM users**: Users created within the account. IAM users are created with no permissions by default. 

* **Roles**: Temporary identities used by EC2 instances, Lambdas, and external users.

* **Federation**: Users with Active Directory identities or other corporate credentials have role assigned in IAM.

* **Web Identity Federation**: Users with web identities from Amazon.com or other Open ID provier have role assigned using Security Token System (STS).

Amazon Resource Names (ARNs) uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS, such as in IAM policies, Amazon Relational Database Service (Amazon RDS) tags, and API calls.

`Secure Access to AWS Services Using AWS Identity and Access Management (IAM) Roles <https://www.youtube.com/watch?v=wY7FOFaPNuE&feature=emb_logo>`_ 

`How to Enable Multi-Factor Authentication (MFA) for Your AWS User Account <https://www.youtube.com/watch?v=A3AObXBJ4Lw&feature=emb_logo>`_


`AWS re:Invent 2018: [REPEAT 1] Become an IAM Policy Master in 60 Minutes or Less (SEC316-R1) <https://www.youtube.com/watch?time_continue=2&v=YQsK4MtsELU&feature=emb_logo>`_

`Deep Dive on AWS Single Sign-On - AWS Online Tech Talks <https://www.youtube.com/watch?v=8jyhsnh0ALQ>`_

SAML 2.0-based Federation
-------------------------

AWS supports identity federation with SAML 2.0 (Security Assertion Markup Language 2.0), an open standard that many identity providers (IdPs) use, such as Active Directory. This feature enables federated single sign-on (SSO), so users can log into the AWS Management Console or call the AWS API operations without you having to create an IAM user for everyone in your organization. By using SAML, you can simplify the process of configuring federation with AWS, because you can use the IdP's service instead of writing custom identity proxy code.

If your identity store is not compatible with SAML 2.0, then you can build a custom identity broker application to perform a similar function. The broker application authenticates users, requests temporary credentials for users from AWS, and then provides them to the user to access AWS resources.

The application verifies that employees are signed into the existing corporate network's identity and authentication system, which might use LDAP, Active Directory, or another system. The identity broker application then obtains temporary security credentials for the employees.

To get temporary security credentials, the identity broker application calls either ``AssumeRole`` or ``GetFederationToken`` to obtain temporary security credentials, depending on how you want to manage the policies for users and when the temporary credentials should expire. The call returns temporary security credentials consisting of an AWS access key ID, a secret access key, and a session token. The identity broker application makes these temporary security credentials available to the internal company application. The app can then use the temporary credentials to make calls to AWS directly. The app caches the credentials until they expire, and then requests a new set of temporary credentials.

.. figure:: /security_d/enterprise-authentication-with-identity-broker-application.diagram.png
   :align: center

	Enterprise authentication with identity broker application

AWS Organizations
*****************

AWS Organizations offers policy-based management for multiple AWS accounts. With Organizations, you can create groups of accounts, automate account creation, apply and manage policies for those groups. Organizations enables you to centrally manage policies across multiple accounts, without requiring custom scripts and manual processes. It allows you to create Service Control Policies (SCPs) that centrally control AWS service use across multiple AWS accounts.

.. figure:: /security_d/organizations.png
   :align: center

   AWS Organizations

You can use an IAM role to delegate access to resources that are in different AWS accounts that you own. You share resources in one account with users in a different account. By setting up cross-account access in this way, you don't need to create individual IAM users in each account. In addition, users don't have to sign out of one account and sign into another in order to access resources that are in different AWS accounts.

You can use the consolidated billing feature in AWS Organizations to consolidate payment for multiple AWS accounts or multiple AISPL accounts. With consolidated billing, you can see a combined view of AWS charges incurred by all of your accounts. You can also get a cost report for each member account that is associated with your master account. Consolidated billing is offered at no additional charge. AWS and AISPL accounts can't be consolidated together.

.. figure:: /security_d/BillingBitsOfOrganizations.png
   :align: center

   AWS Organizations consolidated billing

AWS Security Token Service
**************************

AWS Security Token Service (AWS STS) is the service that you can use to create and provide trusted users with temporary security credentials that can control access to your AWS resources. Temporary security credentials work almost identically to the long-term access key credentials that your IAM users can use.

In this diagram, IAM user Alice in the Dev account (the role-assuming account) needs to access the Prod account (the role-owning account). Here’s how it works:

1. Alice in the Dev account assumes an IAM role (WriteAccess) in the Prod account by calling AssumeRole.

2. STS returns a set of temporary security credentials.

3. Alice uses the temporary security credentials to access services and resources in the Prod account. Alice could, for example, make calls to Amazon S3 and Amazon EC2, which are granted by the WriteAccess role.

.. figure:: /security_d/sts.png
   :align: center

	AWS Security Token Service

Amazon Cognito
**************

You can use Amazon Cognito to deliver temporary, limited-privilege credentials to your application so that your users can access AWS resources. Amazon Cognito identity pools support both authenticated and unauthenticated identities. You can retrieve a unique Amazon Cognito identifier (identity ID) for your end user immediately if you're allowing unauthenticated users or after you've set the login tokens in the credentials provider if you're authenticating users.

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

.. figure:: /security_d/standard.png
   :align: center

	AWS Shield Standard

AWS Shield Standard protects applications running on AWS by providing always-on detection and automatic inline mitigations of DDoS attacks, to minimize application downtime and performance degradation. All AWS customers benefit from the automatic protections of AWS Shield Standard, at no additional charge. It defends against most common, frequently ocurring network and transport layer DDoS attacks that target web sites or applications. It integrates with Amazon CloudFront and Amazon Route 53, to provide comprehensive availability protection against many types of infrastructure attacks. 

A combination of traffic signatures, anaomaly alogorithms and other analysis techniques are employed to detect malicious traffic in real-time. Automated mitigation techniques are built into this service, applied inline to your applications so there is no latency impact. Several techniques, such as deterministic packet filtering and priority-based traffic shaping are used to automatically mitigate attacks without impacting your applications. You can mitigate application layer attacks by writing rules using AWS WAF, only paying for what you use. It is a self service and there is no need to engage AWS support to receive protection against DDoS attacks.

AWS Shield Advanced
===================

.. figure:: /security_d/advanced.png
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

DoS attack mitigation techniques
================================

Apart from using the managed DDoS protection service AWS Shield, you can protect your system from DoS attack by doing the following:

* Use an Amazon CloudFront service for distributing both static and dynamic content.

* Use an Application Load Balancer with Auto Scaling groups for your EC2 instances then restrict direct Internet traffic to the rest of resources by deploying them to a private subnet.

* Setup alerts in Amazon CloudWatch to look for high ``Network In`` and CPU utilization metrics.

`Best Practices for DDoS Mitigation on AWS <https://www.youtube.com/watch?v=HnoZS5jj7pk&feature=emb_logo>`_

AWS Certificate Manager
***********************

AWS Certificate Manager lets you import third-party certificates from the AWS Certificate Manager console, as well as programmatically. If AWS Certificate Manager is not available in your region, use AWS CLI to upload your third-party certificate to the IAM certificate store.

.. figure:: /security_d/acm.png
   :align: center

	AWS Certificate Manager

Amazon Inspector
****************

Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. The service automatically assesses applications for vulnerabilities or deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed report with prioritized steps for remediation.

It is agent-based, API-driven, and delivered as a service. This makes it easy for you to build right into your existing DevOps process, decentralizing and automating vulnerability assessments, and empowering your DevOps teams to make security assessment an integral part of the deployment process.

CloudHSM
********

Attempting to log in as the administrator more than twice with the wrong password zeroizes your HSM appliance. When an HSM is zeroized, all keys, certificates, and other data on the HSM is destroyed. You can use your cluster's security group to prevent an unauthenticated user from zeroizing your HSM.

Amazon does not have access to your keys nor to the credentials of your Hardware Security Module (HSM) and therefore has no way to recover your keys if you lose your credentials. Amazon strongly recommends that you use two or more HSMs in separate Availability Zones in any production CloudHSM Cluster to avoid loss of cryptographic keys.

