Automation
##########

Why should you automate?
************************

Automating your infrastructure
******************************

AWS CloudFormation
==================

The process to execute Infrastructure as code with CloudFormation is the following:

1. Code your CloudFormation template in YAML or JSON directly or use sample templates.

2. Upload local files or from an S3 bucket.

3. Create a stack using console, API, or CLI.

4. Stacks and resources are provisioned.

The following scenarios demonstrate how AWS CloudFormation can help: Simplify infrastructure management, quickly replicate your infrastructure, easily control and track changes to your infrastructure.



The benefits you get from CloudFormation are:

1. As group of resources get deployed or update your resources, if one of your resources fails, Cloud Formation keeps your state and is able to rollback to the last known good state.

2. CloudFormation knows about stabilization of resources. When a resource has been created, it is guaranteed that you can do a describe or a list to the resources.


`AWS CloudFormation Deep Dive and Recent Enhancements <https://www.youtube.com/watch?v=d6SJPMdBShI&feature=emb_logo>`_

Automating deployments
**********************

`Controlling User Session Access to Instances in AWS System Manager Session Manager <https://www.youtube.com/watch?v=nzjTIjFLiow&feature=emb_logo>`_ 

`How do I troubleshoot issues deleting instances when using AWS OpsWorks Stacks? <https://www.youtube.com/watch?v=LgncEGEf7d0&feature=emb_logo>`_

A little more hands off
***********************

AWS Elastic Beanstalk
=====================

AWS Elastic Beanstalk is a PaaS with the following features:

* It allows a quick deployment of your applications. Any code that you have previously written on some specific language can be simply placed over the platform. 

* It reduces the management complexity. You don't need to manage the whole system.

* It is possible to keeps full control over it, allowing you to choose the instance type, the DB and adjust Auto Scaling according to your needs. Besides, it allows you to update your application, access server log files, and enables HTTPS on the load balancer according to the needs of your application.

* It supports a large range of platforms: Packer Builder; Single container, multicontainer, or preconfigured Docker; Go; Java SE; Java with Tomcat; .NET on Windows Server with IIS; Node.js; PHP; Python; Ruby. 

The steps to deploy and update your servers are based only on the creation of your application. After that, you upload the versions to BeanStalk, then launch all the needed environments in the cloud according to the needs of your application. After that, you can manage your environment, and if you need to write a new version, you just update the version.

.. figure:: /automation_d/deployupdates.png

	Deployment and updates


`AWS re:Invent 2017: Manage Your Applications with AWS Elastic Beanstalk (DEV305) <https://www.youtube.com/watch?v=NhsELnv28NU>`_

