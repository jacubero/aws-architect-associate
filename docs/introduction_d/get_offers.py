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

import requests
import csv

def download_offer(servicecode):
    """ download the offer file for the service defined by servicecode. Reference:
    https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/using-ppslong.html#download-offers.

    :param servicecode: Service code
     """

    CSV_URL = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/' + servicecode + '/current/index.csv'

    with requests.Session() as s:
        offer = s.get(CSV_URL)

        filename = servicecode + ".csv"

        with open(filename, 'wb') as f:
    	    f.write(offer.content)

def main():

    # Retrieves all services
    with open("services.csv", mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        for service in csv_reader:

            if line_count > 0:
                
                download_offer(service["ServiceCode"])
 
            line_count += 1 

if __name__ == '__main__':
    main()
