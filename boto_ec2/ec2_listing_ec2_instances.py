import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances() 

for reservation in response['Reservations']: 
    for instance in reservation['Instances']: 
        print(instance['ImageId'], instance['InstanceId'], instance['InstanceType'],
        instance['State']['Name'])
        
        if 'PublicIpAddress' in instance: 
            print(instance['PublicIpAddress'])
        
        if 'KeyName' in instance: 
            print(instance['KeyName'])
            
        if 'SubnetId' in instance: 
            print(instance['SubnetId'])
            
        if 'VpcId' in instance: 
            print(instance['VpcId'])
       
        if 'Tags' in instance: 
            for tag in instance['Tags']: 
                if tag['Key'] == 'Name': 
                    print(tag['Value'])
        
        for sgroup in instance['SecurityGroups']:
            print(sgroup['GroupId'], sgroup['GroupName'])
            
        if 'IamInstanceProfile' in instance: 
            print(instance['IamInstanceProfile']['Id'], instance['IamInstanceProfile']['Arn'])