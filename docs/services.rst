AWS services
############

AWS technology consists of a series of interrelated products or services whose release frecuency varies among services. AWS has significantly increase the number of services and features released during the last years as you can see in figure :ref:`fig-innovation`. You can read `Release Notes <https://aws.amazon.com/releasenotes/>`_ to have a summary of all new features, resolved issues, and known issues in the latest versions of AWS products and services.

.. figure:: /introduction_d/innovation.png
   :name: fig-innovation
   :target: /introduction_d/innovation.png
   :alt: Number of services and features released during the last years

    Number of services and features released during the last years

.. csv-table:: AWS Services List
   :file: introduction_d/services.csv
   :widths: 15, 85
   :header-rows: 1


.. code-block:: console
   :caption: Get available partitions

    >>> import boto3
    >>> session = boto3.Session()
    >>> session.get_available_partitions()
    [u'aws', u'aws-cn', u'aws-us-gov', u'aws-iso', u'aws-iso-b']


.. code-block:: console
   :caption: Get available regions

    >>> session.get_available_regions('ec2')
    [u'ap-east-1', u'ap-northeast-1', u'ap-northeast-2', u'ap-south-1', u'ap-southeast-1', u'ap-southeast-2', u'ca-central-1', u'eu-central-1', u'eu-north-1', u'eu-west-1', u'eu-west-2', u'eu-west-3', u'me-south-1', u'sa-east-1', u'us-east-1', u'us-east-2', u'us-west-1', u'us-west-2']


.. code-block:: console
   :caption: Get available resources

    >>> session.get_available_resources()
    ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']



`Region Table <https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/>`_ 



`Save yourself a lot of pain (and money) by choosing your AWS Region wisely <https://www.concurrencylabs.com/blog/choose-your-aws-region-wisely/>`_
