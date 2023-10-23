import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()


for rt in response['RouteTables']:
    print(rt['VpcId'], rt['RouteTableId'])
    
    if 'Associations' in rt: 
        for associations in rt['Associations']:
            if 'SubnetId' in associations: 
                print(associations['SubnetId'], associations['RouteTableAssociationId'])
                
        for routes in rt['Routes']:
            if 'DestinationCidrBlock' and 'GatewayId' in routes: 
                print(routes['DestinationCidrBlock'], routes['GatewayId'])