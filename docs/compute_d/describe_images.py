import csv
import boto3

ec2 = boto3.client('ec2')

# Retrieves all image types
response = ec2.describe_images()

it_file = csv.writer(open("images.csv", "wb+"))

parameter_list = ["Architecture", 
		"CreationDate", 
		"ImageId", 
		"ImageLocation", 
		"ImageType", 
		"Public", 
		"KernelId",
		"OwnerId",
		"Platform",
		"ProductCodes",
		"RamdiskId",
		"State",
		"BlockDeviceMappings",
		"Description",
		"EnaSupport",
		"Hypervisor",
		"ImageOwnerAlias",
		"Name",
		"RootDeviceName",
		"RootDeviceType",
		"SriovNetSupport",
		"StateReason",
		"Tags",
		"VirtualizationType"
		]

it_file.writerow(parameter_list)

for r in response['Images']:

	image_list = []

	for p in parameter_list:
		
	  if p in r:
	  	image_list.append(r[p])
	  else:
	    image_list.append("")
	
	it_file.writerow(image_list)

