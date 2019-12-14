# Copyright 2010-2019 Jose Antonio Alvarez Cubero. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License. 

import csv
import boto3

def list_services(iter_marker=''):
    """List the AWS services in the AWS account's default region.

    :param iter_marker: Marker used to identify start of next batch of services to retrieve
    :return: List of services
    :return: String marking the start of next batch of services to retrieve. Pass this string as the iter_marker
        argument in the next invocation of list_services().
    """

    pricing = boto3.client('pricing')

    services = pricing.describe_services(MaxResults=100, NextToken=iter_marker)
    marker = services.get('NextToken')       # None if no more clusters to retrieve
    return services['Services'], marker

def main():

    f = csv.writer(open("services.csv", "wb+"))
    f.writerow(["ServiceCode", "AttributeNames"])

    services, marker = list_services()

    while True:
        for service in services:
  	    service_list = []
            service_list.append(service["ServiceCode"]) 
            str_list='; '.join(map(str,service["AttributeNames"]))
            service_list.append(str_list)
            f.writerow(service_list)

        # If no more services exist, exit loop, otherwise retrieve the next batch
        if marker is None:
            break
        services, marker = list_services(iter_marker=marker)


if __name__ == '__main__':
    main()
