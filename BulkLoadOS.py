import boto3
import json

# S3 client
#s3 = boto3.client('s3')

# OpenSearch client
opensearch = boto3.client('opensearch',            endpoint_url='http://localhost:9200',
                         aws_access_key_id='admin',
                         aws_secret_access_key='admin'
                         
                        )
try:
    response = opensearch.list_tags()

    # Print the indices
    print("Indices in OpenSearch domain:")
    for index in response['IndexNames']:
        print(index)
    print("Successfully connected to OpenSearch")
except Exception as e:
    print("Failed to connect to OpenSearch: ", e)
# S3 bucket name and file name
bucket_name = 'my-bucket'
file_name = 'my-data.json'

# Download the JSON file from S3
#s3.download_file(bucket_name, file_name, '/tmp/data.json')

# Open the JSON file
with open('/Users/ravi/Downloads/Linkedin_profile_collector_20230116_060016.1673848814776.1_1.json', "r") as file:
    data = json.load(file)

# Create the actions for the Bulk API
actions = []
for item in data:
    action = {
        "index": {
            "_index": "ES_Test"
        }
    }
    actions.append(action)
    actions.append(item)

# Use the Bulk API to index the data
response = opensearch.bulk(index='ES_Test', body=actions)