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

def list_attribute_values(servicecode, attribute, iter_marker=''):
    """List of attribute values in the AWS account's default region. Attibutes are similar to the details in a Price List API offer file.

    :param iter_marker: Marker used to identify start of next batch of attribute values to retrieve
    :return: List of attribute values
    :return: String marking the start of next batch of attribute values to retrieve. Pass this string as the iter_marker
        argument in the next invocation of list_attribute_values().
    """

    pricing = boto3.client('pricing')

    attribute_values = pricing.get_attribute_values(ServiceCode=servicecode, AttributeName=attribute, MaxResults=100, NextToken=iter_marker)
    marker = attribute_values.get('NextToken')       # None if no more clusters to retrieve
    return attribute_values["AttributeValues"], marker


def main():

    # Retrieves all services
    with open("services.csv", mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        for service in csv_reader:

            # AmazonEC2 is too long
            if (line_count > 0) and (service["ServiceCode"] != "AmazonEC2"):
                attribute_list = service["AttributeNames"].split(";") 

                filename = service["ServiceCode"] + ".csv"
                
                with open(filename, "wb+") as a_file:
                    csv_writer = csv.writer(a_file)
                    csv_writer.writerow(["AttributeName", "AttributeValues"])

                    for a in attribute_list:
                        row_list = []   
                        value_list = []
                        attribute = a.strip()
                        row_list.append(attribute)  

                        attribute_values, marker = list_attribute_values(service["ServiceCode"], attribute)

                        while True:
                            for attribute_value in attribute_values:
                                value_list.append(attribute_value["Value"])

                            str_list='; '.join(map(str,value_list))
                            row_list.append(str_list)
                            csv_writer.writerow(row_list)

                            # If no more attribute_values exist, exit loop, otherwise retrieve the next batch
                            if marker is None:
                                break

                            attribute_values, marker = list_attribute_values(service["ServiceCode"], attribute,iter_marker=marker)

            line_count += 1 

if __name__ == '__main__':
    main()
