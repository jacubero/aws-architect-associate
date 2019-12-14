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

session = boto3.Session()

session.get_available_services()

f = csv.writer(open("available_services.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["Number", "Service"])

for item, service in (enumerate(session.get_available_services(), 1)):
    f.writerow([item, service])
