import boto3


route_table_id = 'rtb-0c90c8df56c99a88c'
internet_gateway = 'igw-0359124b54a0bc4dc'

ec2 = boto3.client('ec2')


ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway,
    RouteTableId=route_table_id,
)
