import boto3

ec2 = boto3.client('ec2') 

# required AMI and instance type
# ami-0df435f331839b2d6
# t2.micro

response = ec2.describe_instance_types(
    Filters=[
        {
            'Name': 'free-tier-eligible',
            'Values': [
                'true',
            ]
        },
    ]
)


for instanceType in response['InstanceTypes']:
    print(instanceType['InstanceType'])

