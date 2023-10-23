import boto3


cidrblock = '10.0.0.1/24'
vpcid = 'vpc-074242d0754b30cba'

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(
    CidrBlock=cidrblock,
    VpcId=vpcid
)

print(subnet['Subnet']['SubnetId'])