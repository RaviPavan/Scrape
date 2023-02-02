
import boto3
from botocore.exceptions import ClientError

def copy_file():
    s3 = boto3.resource('s3')
    source= { 'Bucket' : 'brightdatakula','Key':'NDJson/ND_JSON_Linkedin_profile_collector_20230127_113242.1674819070912.1.json'}
    dest ={ 'Bucket' : 'brightdatakula','Key':'/Upload100Files/ND_JSON_Linkedin_profile_collector_20230127_113242.1674819070912.1.json'}
    s3.meta.client.copy(source,dest)

def get_secret():

    secret_name = "opensearchdashboard/credentials"
    region_name = "us-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        print( get_secret_value_response)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    print(secret)
    # Your code goes here.
#get_secret()
#copy_file()

for i in range(500):
    print(i)
    s3 = boto3.resource('s3')
    source= { 'Bucket' : 'brightdatakula','Key':'NDJson/Test.json'}
    dest_filename='Upload100Files/ND_JSON___'+str(i)+'.json'
    s3.meta.client.copy(source,'brightdatakula',dest_filename)