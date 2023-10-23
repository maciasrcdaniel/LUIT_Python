import boto3

ec2 = boto3.client('ec2')


route_table_id = 'rtb-0c90c8df56c99a88c'

ec2.delete_route_table(
    RouteTableId=route_table_id,
)

