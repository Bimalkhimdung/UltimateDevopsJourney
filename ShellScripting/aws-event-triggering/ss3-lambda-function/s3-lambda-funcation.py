import boto3
import json

def lambda_handler(event, context):
    #extract relevent information form the s3 event trigger
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    #perform desired operations with the uploaded file
    
    print(f"file '{object_key}' is: was uploded to bucket '{bucket_name}'")
    
    #example : send a notifiaction via SNS
    
    sns_client = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-east-1:<account-id>:s3-lambda-sns'
    sns_client.publish(
        
        TopicArn=topic_arn,
        subject='s3 object created',
        message=f"file '{object_key}' is: was uploded to bucket '{bucket_name}'"
        
    )
    
    return {
        
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }