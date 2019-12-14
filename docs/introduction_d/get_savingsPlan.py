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
import json
import csv
import re

savingsPlanTypes = ["AWSComputeSavingsPlan"]

def download_savingsPlan(savingsPlanType):
    """ Download the savingsPlan file for the service defined by savingsPlanType. Reference:
    https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/using-ppslong.html#download-savingsPlans.

    :param savingsPlanType: Savings Plan
     """

    URL_ROOT = 'https://pricing.us-east-1.amazonaws.com'
    URL_GLOBAL = URL_ROOT + '/savingsPlan/v1.0/aws/' + savingsPlanType + '/current/index.json'

    with requests.Session() as s:
        savingsPlanGlobal = s.get(URL_GLOBAL)
        savingsPlanGlobal_json = savingsPlanGlobal.json()

    for version in savingsPlanGlobal_json["versions"]:
        m = re.search('AWSComputeSavingsPlan/(.+?)/region_index.json',version["offerVersionUrl"])
        if m:
     	    version_number = m.group(1)
            URL_REGION = URL_ROOT + version["offerVersionUrl"]
            with requests.Session() as s:
    	        savingsPlanRegion = s.get(URL_REGION)
                savingsPlanRegion_json = savingsPlanRegion.json()

	    for region in savingsPlanRegion_json["regions"]:
                filename = version_number + "-" + region["regionCode"] + ".csv"
                JSON_URL = URL_ROOT + region["versionUrl"]
                CSV_URL=JSON_URL.replace(".json", ".csv")
                
                with requests.Session() as s:
                    savingsPlan = s.get(CSV_URL)

                    with open(filename, 'wb') as f:
                        f.write(savingsPlan.content)

def main():

    # Retrieves all Savings Plans 
    for savingsPlanType in savingsPlanTypes:
                
        download_savingsPlan(savingsPlanType)
 

if __name__ == '__main__':
    main()
