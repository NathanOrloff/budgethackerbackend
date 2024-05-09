import boto3
from botocore.exceptions import ClientError
import logging
import constants

def pretty_print_response(response):
  print(json.dumps(response, indent=2, sort_keys=True, default=str))

def format_error(e):
    response = json.loads(e.body)
    return {'error': {'status_code': e.status, 'display_message':
                      response['error_message'], 'error_code': response['error_code'], 'error_type': response['error_type']}}

def format_success(payload=None, retcode=200):
    return {'success': True, 'payload': payload, 'retcode': retcode}


def store_access_token(key, access_token):
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=constants.REGION
    )
    success = False
    try:
        client.create_secret(
            Name=key,
            SecretString=access_token,
        )
        success = True
    except ClientError as e:
        logging.error(f"Unable to create key - {e}")
    
    return success

def get_access_token(key):
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=constants.REGION
    )
    access_token = None
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=key
        )
        access_token = get_secret_value_response['SecretString']
    except ClientError as e:
        logging.error(f"Unable to retrieve key - {e}")
    
    return access_token


def delete_access_token(key):
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=constants.REGION
    )
    success = False
    try:
        client.delete_secret(
            SecretId=key
        )
        success = True
    except ClientError as e:
        logging.error(f"Unable to delete key - {e}")
    
    return success
