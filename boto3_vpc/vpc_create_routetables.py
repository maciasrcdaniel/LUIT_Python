import boto3



vpc_id = 'vpc-074242d0754b30cba'


ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable['RouteTable']['RouteTableId'])
