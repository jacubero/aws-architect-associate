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

# Retrieves all regions/endpoints that work with EC2
regions = ec2.describe_regions(AllRegions=True)

f = csv.writer(open("regions.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["RegionName", "Endpoint", "OptInStatus"])

for region in regions['Regions']:
    f.writerow([region["RegionName"], region["Endpoint"], region["OptInStatus"]])
