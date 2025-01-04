# Smoke tests for UNH IT class lab assignments
#
# Requirements:  (AWS Linux2 AMI is assumed)
#    yum install python3 -y
#    curl -O https://bootstrap.pypa.io/get-pip.py
#    python3 get-pip.py --user
#    pip install -U pytest
#    pip install boto3
#    curl https://raw.githubusercontent.com/kengraf/UNH-IT/main/test_systems.py -O
#
# Assumptions:
#    3 EC2 instances deployed with "Name" tags of IT-PIPELINE, IT-PROD, IT-DEV.
#    This test should be run from the IT-PIPELINE instance as it checks availibilty
#    of both public and private IPv4 addresses.
#    The "aws configure" process has been completed to allow the use of the boto3 API
#
# Each system is tested only for SSH (socket open on port 22) and HTTP
# (200 status return on port 80).
#
# Successful deployments will result in all tests passing, that includes some
# sockets NOT being open.
# 

import boto3
import socket
import requests

client = boto3.client('ec2')
ec2_pipeline = {}
ec2_dev = {}
ec2_prod = {}

def open_socket(host, port):
    s = socket.socket()
    try:
        s.settimeout(2)
        s.connect((host, port)) 
    except Exception as e: 
        return False
    finally:
        s.close()
    return True    


# Tests for pipeline instance
def test_pipeline_get_instance():
    global ec2_pipeline
    ec2_pipeline = client.describe_instances(
        Filters=[{
            'Name': 'tag:Name',
            'Values': ['IT-PIPELINE']
            }])['Reservations'][0]['Instances'][0]
    assert ec2_pipeline['PublicIpAddress']

def test_pipeline_public_web_closed():
    assert open_socket( ec2_pipeline['PublicIpAddress'], 80 ) == False

def test_pipeline_private_web_closed():
    assert open_socket( ec2_pipeline['PrivateIpAddress'], 80 ) == False

def test_pipeline_public_ssh():
    assert open_socket( ec2_pipeline['PublicIpAddress'], 22 )

def test_pipeline_private_ssh():
    assert open_socket( ec2_pipeline['PrivateIpAddress'], 22 )

# Tests for dev instance
def test_dev_get_instance():
    global ec2_dev
    ec2_dev = client.describe_instances(
        Filters=[{
            'Name': 'tag:Name',
            'Values': ['IT-DEV']
            }])['Reservations'][0]['Instances'][0]
    assert ec2_dev['PublicIpAddress']

def test_prod_dev_web_closed():
    assert open_socket( ec2_dev['PublicIpAddress'], 80 ) == False

def test_dev_private_web():
    response = requests.get(ec2_web['PrivateIpAddress'])
    assert response.status_code == 200

def test_dev_public_ssh_closed():
    assert open_socket( ec2_dev['PublicIpAddress'], 22 ) == False

def test_dev_private_ssh():
    assert open_socket( ec2_dev['PrivateIpAddress'], 22 )

# Tests for prod instance
def test_prod_get_instance():
    global ec2_prod
    ec2_prod = client.describe_instances(
        Filters=[{
            'Name': 'tag:Name',
            'Values': ['IT-PROD']
            }])['Reservations'][0]['Instances'][0]
    assert ec2_prod['PublicIpAddress']

def test_prod_public_web():
    response = requests.get(ec2_prod['PublicIpAddress'])
    assert response.status_code == 200
    
def test_prod_private_web():
    response = requests.get(ec2_prod['PrivateIpAddress'])
    assert response.status_code == 200

def test_prod_public_ssh_closed():
    assert open_socket( ec2_prod['PublicIpAddress'], 22 ) == False

def test_prod_private_ssh_closed():
    assert open_socket( ec2_prod['PrivateIpAddress'], 22 ) == False

