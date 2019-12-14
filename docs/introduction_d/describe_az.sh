echo "RegionName,State,ZoneId,ZoneName"

tail -n +2 regions.csv | while IFS=, read -r RegionName State ZoneId ZoneName
do
	aws ec2 describe-availability-zones --region $RegionName | cut -f 2-5 -d$'\t' --output-delimiter=','
done