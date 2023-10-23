import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-0c90c8df56c99a88c'

route_table = ec2.describe_route_tables(
    RouteTableIds=[
        route_table_id,
    ],
)

for association in route_table['RouteTables'][0]['Associations']:
    if not association['Main']:
        association_id = association['RouteTableAssociationId']
        print(association_id)

        ec2.disassociate_route_table(
            AssociationId=association_id,
        )
