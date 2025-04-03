import boto3
import base64

ec2 = boto3.client('ec2', region_name='ap-southeast-5')

def launch_ec2_instance():
    # UserData script (must be base64 encoded)
    user_data_script = """#!/bin/bash
    cd /home/ubuntu/
    sudo wget https://raw.githubusercontent.com/kelvinlee97/Kubernetes/refs/heads/main/kubeadm/kubeadm_init.sh
    """
    
    # Encode the UserData script to base64
    user_data_encoded = base64.b64encode(user_data_script.encode()).decode()

    response = ec2.run_instances(
        ImageId='ami-0d6547c3f05df32d3',  # Ubuntu Server 24.04 LTS (HVM)
        InstanceType='t3.small',
        MinCount=1,
        MaxCount=1,
        KeyName='kelvin_ec2_MY',  # Key pair assigned at launch
        UserData=user_data_encoded,
        SecurityGroupIds=['sg-0d698b6a257640c0a'],  # Security groups(main-sg)
        SubnetId=('subnet-0412c8d413d3a795d'),  # Subnet ID(main-subnet-public1-ap-southeast-5a)
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'kubeadm'}]
        }]
    )
    
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Launched instance: {instance_id}")
    
    # Wait for the instance to be running
    waiter = ec2.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])
    
    # Get instance details and print Public IPv4 address
    instance_info = ec2.describe_instances(InstanceIds=[instance_id])
    public_ipv4 = instance_info['Reservations'][0]['Instances'][0]['PublicIpAddress']
    
    print(f"Public IPv4 address: {public_ipv4}")
    return public_ipv4

launch_ec2_instance()