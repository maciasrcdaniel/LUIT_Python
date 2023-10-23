import boto3

def create_instance(client, ami_id, sg_group_id, key_pair_name, user_data=None): 
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName=key_pair_name,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            sg_group_id
        ], 
        UserData=user_data
    )
    
    print(response['Instances'][0]['InstanceId'])


    
ami_id = 'ami-0df435f331839b2d6'
sg_group_id = 'sg-02dfc12af2ed31096'
key_pair_name = 'Key from boto3'

user_data='''#!/bin/bash
    apt update -y 
    apt-get install -y apache2
    systemctl start apache2
    systemctl enable apache2'''

ec2 = boto3.client('ec2')
create_instance(ec2, ami_id, sg_group_id, key_pair_name, user_data)





