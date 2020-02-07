Automation
##########

AWS CloudFormation
******************

AWS CloudFormation is a Infrastructure as code that enables provisioning and management the entire lifecycle of your AWS infrastructure. The process to execute Infrastructure as code with CloudFormation is the following:

1. Code your CloudFormation template in YAML or JSON directly or use sample templates.

2. Upload local files or from an S3 bucket.

3. Create a stack using console, API, or CLI.

4. Stacks and resources are provisioned.

The following scenarios demonstrate how AWS CloudFormation can help: Simplify infrastructure management, quickly replicate your infrastructure, easily control and track changes to your infrastructure.

The benefits you get from CloudFormation are:

1. As group of resources get deployed or update your resources, if one of your resources fails, Cloud Formation keeps your state and is able to rollback to the last known good state.

2. CloudFormation knows about stabilization of resources. When a resource has been created, it is guaranteed that you can do a describe or a list to the resources.

There is no additional charge for AWS CloudFormation. You only pay for the AWS resources that are created (e.g. Amazon EC2 instances, Elastic Load Balancing load balancers, etc.)

`AWS CloudFormation Deep Dive and Recent Enhancements <https://www.youtube.com/watch?v=d6SJPMdBShI&feature=emb_logo>`_

Template Anatomy
================

A template is a JSON- or YAML-formatted text file that describes your AWS infrastructure. The following examples show an AWS CloudFormation template structure and its sections.

JSON
----

The following example shows a JSON-formatted template fragment.

.. code-block:: JSON

	{
	  "AWSTemplateFormatVersion" : "version date",

	  "Description" : "JSON string",

	  "Metadata" : {
	    template metadata
	  },

	  "Parameters" : {
	    set of parameters
	  },

	  "Mappings" : {
	    set of mappings
	  },

	  "Conditions" : {
	    set of conditions
	  },

	  "Transform" : {
	    set of transforms
	  },

	  "Resources" : {
	    set of resources
	  },

	  "Outputs" : {
	    set of outputs
	  }
	}

YAML
----

The following example shows a YAML-formatted template fragment.

.. code-block:: YAML

	---
	AWSTemplateFormatVersion: "version date"

	Description:
	  String

	Metadata:
	  template metadata

	Parameters:
	  set of parameters

	Mappings:
	  set of mappings

	Conditions:
	  set of conditions

	Transform:
	  set of transforms

	Resources:
	  set of resources

	Outputs:
	  set of outputs

Template Sections
-----------------

Templates include several major sections. The Resources section is the only required section. Some sections in a template can be in any order. However, as you build your template, it can be helpful to use the logical order shown in the following list because values in one section might refer to values from a previous section.

Enterprise management
=====================

**Drift detection** allows you to detect if configuration changes were made to your stack resources outside of CloudFormation via the AWS Management Console, CLI, and SDKs. you can use the diff viewer in the console to pinpoint the changes. It supports the most commonly used resources. You can define automatic drift alerts via AWS Config rule. You can remediate by updating the live configuration values to match the template values.

**Stacksets** extends the functionality of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation.

**Dynamic references** provide a compact, powerful way for you to specify external values that are stored and managed in other services, such as the Systems Manager Parameter Store, in your stack templates. When you use a dynamic reference, CloudFormation retrieves the value of the specified reference when necessary during stack and change set operations. CloudFormation currently supports the following dynamic reference patterns:

* *ssm*, for plaintext values stored in AWS Systems Manager Parameter Store

* *ssm-secure*, for secure strings stored in AWS Systems Manager Parameter Store

* *secretsmanager*, for entire secrets or specific secret values that are stored in AWS Secrets Manager

Developer productivity
======================

`CloudFormation Linter <https://github.com/aws-cloudformation/cfn-python-lint>`_ is an open source tool that allows you to validate CloudFormation YAML/JSON templates against the CloudFormation spec and additional checks. Includes checking valid values for resource properties and best practices. CloudFormation Linter has plugins for Atom, VisualStudio Code, Sublime, and VIM. It can be run headless in pipelines. It can process multiple files. It can handle conditions/Fn:if. It has SAM local integration.

The `AWS CloudFormation Template Schema <https://github.com/aws-cloudformation/aws-cloudformation-template-schema>`_ is intended to improve the authoring experience for our customers. It is a simple code process which converts our existing Resource Specifications files into a JSON Schema formatted document. This schema can be integrated into many publicly available IDEs such as Visual Studio Code & PyCharm to provide inline syntax checking and code completion.

`Taskcat <https://github.com/aws-quickstart/taskcat>`_ is an open source tool that tests AWS CloudFormation templates. It deploys your AWS CloudFormation template in multiple AWS Regions and generates a report with a pass/fail grade for each region. You can specify the regions and number of Availability Zones you want to include in the test, and pass in parameter values from your AWS CloudFormation template. taskcat is implemented as a Python class that you import, instantiate, and run.

An example of pipeline for deploying AWS Cloudformation templates is illustrated below.

.. figure:: /automation_d/cpipeline.png
   :align: center
   
	CloudFormation pipeline

**Macros** allows you to write short-hand, abbreviated instructions that expand automatically before deployment. For instance you can use it to:

* Add utility functions, iteration loops, string, ...

* Ensure resources are defined to comply with stardards.

* Easy to share code to reuse across stacks.

The key benefit of macros is once deployed, downstream users can be isolated from program details. Macros are AWS Lambda functions and can use all supported languages. You can run macros without change sets. You have `Macro examples <https://github.com/awslabs/aws-cloudformation-templates/tree/02b38813a38806d1a897b94496b79e156c96b94b/aws/services/CloudFormation/MacrosExamples>`_.

**AWS CDK (Cloud Development Kit)** supports TypeScript/JavaScript, Java, .NET, Python. 

AWS OpsWorks
************

AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. Chef and Puppet are automation platforms that allow you to use code to automate the configurations of your servers. OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments. OpsWorks has three offerings - AWS Opsworks for Chef Automate, AWS OpsWorks for Puppet Enterprise, and AWS OpsWorks Stacks.

`Controlling User Session Access to Instances in AWS System Manager Session Manager <https://www.youtube.com/watch?v=nzjTIjFLiow&feature=emb_logo>`_ 

`How do I troubleshoot issues deleting instances when using AWS OpsWorks Stacks? <https://www.youtube.com/watch?v=LgncEGEf7d0&feature=emb_logo>`_

A little more hands off
***********************

AWS Elastic Beanstalk
*********************

AWS Elastic Beanstalk is a PaaS with the following features:

* It allows a quick deployment of your applications. Any code that you have previously written on some specific language can be simply placed over the platform. 

* It reduces the management complexity. You don't need to manage the whole system.

* It is possible to keeps full control over it, allowing you to choose the instance type, the DB and adjust Auto Scaling according to your needs. Besides, it allows you to update your application, access server log files, and enables HTTPS on the load balancer according to the needs of your application.

* It supports a large range of platforms: Packer Builder; Single container, multicontainer, or preconfigured Docker; Go; Java SE; Java with Tomcat; .NET on Windows Server with IIS; Node.js; PHP; Python; Ruby. 

The steps to deploy and update your servers are based only on the creation of your application. After that, you upload the versions to BeanStalk, then launch all the needed environments in the cloud according to the needs of your application. After that, you can manage your environment, and if you need to write a new version, you just update the version.

.. figure:: /automation_d/deployupdates.png
   :align: center

	Deployment and updates

AWS Elastic Beanstalk stores your application files and optionally, server log files in Amazon S3. If you are using the AWS Management Console, the AWS Toolkit for Visual Studio, or AWS Toolkit for Eclipse, an Amazon S3 bucket will be created in your account and the files you upload will be automatically copied from your local client to Amazon S3. Optionally, you may configure Elastic Beanstalk to copy your server log files every hour to Amazon S3. You do this by editing the environment configuration settings.

With CloudWatch Logs, you can monitor and archive your Elastic Beanstalk application, system, and custom log files from Amazon EC2 instances of your environments. You can also configure alarms that make it easier for you to react to specific log stream events that your metric filters extract. The CloudWatch Logs agent installed on each Amazon EC2 instance in your environment publishes metric data points to the CloudWatch service for each log group you configure. Each log group applies its own filter patterns to determine what log stream events to send to CloudWatch as data points. Log streams that belong to the same log group share the same retention, monitoring, and access control settings. You can configure Elastic Beanstalk to automatically stream logs to the CloudWatch service.

`AWS re:Invent 2017: Manage Your Applications with AWS Elastic Beanstalk (DEV305) <https://www.youtube.com/watch?v=NhsELnv28NU>`_

