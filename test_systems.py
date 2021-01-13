# IT cloud deployment tests
import boto3
import socket

client = boto3.client('ec2')
ec2_pipeline = {}
ec2_dev = {}
ec2_prod = {}

def test_socket(host, port):
    s = socket.socket()
    try:
        s.settimeout(2)
        s.connect((host, port)) 
    except Exception as e: 
        return False
    finally:
        s.close()
    return True    


def test_get_pipeline_instance():
    global ec2_pipeline
    ec2_pipeline = client.describe_instances(
        Filters=[{
            'Name': 'tag:Name',
            'Values': ['IT-PIPELINE']
            }])['Reservations'][0]['Instances'][0]
    assert ec2_pipeline['PublicIpAddress']

# Tests for pipeline instance
def test_pipeline_public_web():
    assert test_socket( ec2_pipeline['PublicIpAddress'], 80 ) == False

def test_pipeline_private_web():
    assert test_socket( ec2_pipeline['PrivateIpAddress'], 80 ) == False

def test_pipeline_public_ssh():
    assert test_socket( ec2_pipeline['PublicIpAddress'], 22 )

def test_pipeline_private_ssh():
    assert test_socket( ec2_pipeline['PrivateIpAddress'], 22 )

# Tests for dev instance
def test_get_dev_instance():
    global ec2_dev
    ec2_dev = client.describe_instances(
        Filters=[{
            'Name': 'tag:Name',
            'Values': ['IT-DEV']
            }])['Reservations'][0]['Instances'][0]
    assert ec2_dev['PublicIpAddress']

def test_prod_dev_web():
    assert test_socket( ec2_dev['PublicIpAddress'], 80 ) == False

def test_dev_private_web():
    assert test_socket( ec2_dev['PrivateIpAddress'], 80 )

def test_dev_public_ssh():
    assert test_socket( ec2_dev['PublicIpAddress'], 22 ) == False

def test_dev_private_ssh():
    assert test_socket( ec2_dev['PrivateIpAddress'], 22 )

# Tests for prod instance
def test_get_prod_instance():
    global ec2_prod
    ec2_prod = client.describe_instances(
        Filters=[{
            'Name': 'tag:Name',
            'Values': ['IT-PROD']
            }])['Reservations'][0]['Instances'][0]
    assert ec2_prod['PublicIpAddress']

def test_prod_public_web():
    assert test_socket( ec2_prod['PublicIpAddress'], 80 )

def test_prod_private_web():
    assert test_socket( ec2_prod['PrivateIpAddress'], 80 )

def test_prod_public_ssh():
    assert test_socket( ec2_prod['PublicIpAddress'], 22 ) == False

def test_prod_private_ssh():
    assert test_socket( ec2_prod['PrivateIpAddress'], 22 ) == False


