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

ec2 = boto3.client('ec2')

# Retrieves all instance types
response = ec2.describe_instance_types()

it_file = csv.writer(open("instance_types.csv", "wb+"))

parameter_list = ["InstanceType", "CurrentGeneration", "FreeTierEligible", "SupportedUsageClasses", "BareMetal", "Hypervisor", "ProcessorInfo", "VCpuInfo", "MemoryInfo", "InstanceStorageSupported", "InstanceStorageInfo", "EbsInfo", "NetworkInfo", "GpuInfo", "FpgaInfo", "PlacementGroupInfo", "HibernationSupported", "BurstablePerformanceSupported", "DedicatedHostsSupported", "AutoRecoverySupported"]
header_list = ["InstanceType", "CurrentGeneration", "FreeTierEligible", "SupportedUsageClasses", "BareMetal", "Hypervisor", "SupportedArchitectures", "SustainedClockSpeedInGhz", "ValidThreadsPerCore", "DefaultCores", "DefaultVCpus", "ValidCores", "DefaultThreadsPerCore", "MemorySizeInMiB", "InstanceStorageSupported", "TotalSizeInGB", "Disks", "EbsOptimizedSupport", "EbsEncryptionSupport", "NetworkPerformance", "MaximumNetworkInterfaces", "Ipv6Supported", "Ipv6AddressesPerInterface", "EnaSupport", "Ipv4AddressesPerInterface", "TotalGpuMemoryInMiB", "Gpus", "TotalFpgaMemoryInMiB", "Fpgas", "PlacementGroupInfo", "HibernationSupported", "BurstablePerformanceSupported", "DedicatedHostsSupported", "AutoRecoverySupported" ]

# Write CSV Header, If you dont need that, remove this line
it_file.writerow(header_list)

for r in response['InstanceTypes']:

	instance_list = []

	for p in parameter_list:
  	  if p in r:
	    str_list = ""
	    str_d = ""

	    if p=="SupportedUsageClasses":
	      str_list='; '.join(map(str,r[p])) 
	      instance_list.append(str_list)
	    elif p=="ProcessorInfo":
	      str_list='; '.join(map(str,r[p]["SupportedArchitectures"])) 
	      instance_list.append(str_list)
	      if "SustainedClockSpeedInGhz" in r[p]:
	        instance_list.append(r[p]["SustainedClockSpeedInGhz"])
	      else:
	      	instance_list.append("")
	    elif p=="VCpuInfo":
	      if "ValidThreadsPerCore" in r[p]:
	        str_list='; '.join(map(str,r[p]["ValidThreadsPerCore"]))
	        instance_list.append(str_list)
	      else:
	      	instance_list.append("")	
	      if "DefaultCores" in r[p]:       
	        instance_list.append(r[p]["DefaultCores"])
	      else:
	      	instance_list.append("")
	      instance_list.append(r[p]["DefaultVCpus"])
	      if "ValidCores" in r[p]:
	        str_list='; '.join(map(str,r[p]["ValidCores"]))
	        instance_list.append(str_list)
	      else:
	      	instance_list.append("")
	      if "DefaultThreadsPerCore" in r[p]:
                instance_list.append(r[p]["DefaultThreadsPerCore"])
	      else:
	      	instance_list.append("")            
	    elif p=="MemoryInfo":
	      instance_list.append(r[p]["SizeInMiB"])
	    elif p=="InstanceStorageInfo":
	      instance_list.append(r[p]["TotalSizeInGB"])
	      disks_list=[]
	      for d in r[p]["Disks"]:
		str_d = str(d["Count"]) + "x" + str(d["SizeInGB"]) + " Gb " + d["Type"]
		disks_list.append(str_d)
	      str_list='; '.join(map(str,disks_list))
	      instance_list.append(str_list)
	    elif p=="EbsInfo":
	      instance_list.append(r[p]["EbsOptimizedSupport"])
	      instance_list.append(r[p]["EncryptionSupport"])
	    elif p=="NetworkInfo":
	      instance_list.append('"{}"'.format(r[p]["NetworkPerformance"]))
	      instance_list.append(r[p]["MaximumNetworkInterfaces"])
	      instance_list.append(r[p]["Ipv6Supported"])
	      instance_list.append(r[p]["Ipv6AddressesPerInterface"])
	      instance_list.append(r[p]["EnaSupport"])
	      instance_list.append(r[p]["Ipv4AddressesPerInterface"])
	    elif p=="GpuInfo":
	      instance_list.append(r[p]["TotalGpuMemoryInMiB"])
	      gpus_list=[]
	      for d in r[p]["Gpus"]:
		str_d = str(d["Count"]) + "x" + str(d["MemoryInfo"]["SizeInMiB"]) + " MiB " + d["Name"] + " " + d["Manufacturer"]
		gpus_list.append(str_d)
	      str_list=';'.join(map(str,gpus_list))
	      instance_list.append(str_list)
	    elif p=="FpgaInfo":
	      instance_list.append(r[p]["TotalFpgaMemoryInMiB"])
	      fpgas_list=[]
	      for d in r[p]["Fpgas"]:
		str_d = str(d["Count"]) + "x" + str(d["MemoryInfo"]["SizeInMiB"]) + " MiB " + d["Name"] + " " + d["Manufacturer"]
		fpgas_list.append(str_d)
	      str_list='; '.join(map(str,fpgas_list))
	      instance_list.append(str_list)
	    elif p=="PlacementGroupInfo":
	      str_list='; '.join(map(str,r[p]["SupportedStrategies"])) 
	      instance_list.append(str_list)
	    else:
	      instance_list.append(r[p])
          elif p=="InstanceStorageInfo" or p=="GpuInfo" or p=="FpgaInfo":
            instance_list.append("")
            instance_list.append("")
	  else:
	    instance_list.append("")
	
	it_file.writerow(instance_list)

