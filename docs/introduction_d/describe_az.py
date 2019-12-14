# Copyright 2019 Jose Antonio Alvarez Cubero. All Rights Reserved.
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

ec2 = boto3.client('ec2')

az_file = csv.writer(open("azs.csv", "wb+"))

parameter_list = ["ZoneName", "ZoneId", "RegionName", "State", "Messages"]
az_file.writerow(parameter_list)

azs = ec2.describe_availability_zones()

for az in azs['AvailabilityZones']:
  az_list = []

  for p in parameter_list:

  	if p in az:
	  az_list.append(az[p])

	else:
	  az_list.append("")
	
  az_file.writerow(az_list)
