import boto3 


ec2 = boto3.client('ec2')

route_table_id = 'rtb-0c90c8df56c99a88c'
subnet_id = 'subnet-0a53a9466863b60e7'

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id
)

print(association['AssociationId'])
