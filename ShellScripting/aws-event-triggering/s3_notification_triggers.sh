#!/bin/bash
#author : Bimal Rai ( raibimal.com.np )

#for debugger mode

set -x

#store the AWS ID in a variable

aws_account_id=$(aws sts get-caller-identity --query "Account" --output text)

#print the AWS ID

echo"AWS ID is : $aws_account_id"

#set  aws region and bucket name

AWS_REGION="us-east-1"
bucket_name="Bimalkhimdung-bucket"
lambda_function_name="s3-lambda-function"
role_name="s3-lambda-sns"
email_address="bimalkhimdung@gmail.com"

#crate iam role for the project

role_response=$(aws iam create-role --role-name $role_name s3-lambda-sns --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com",
                "s3.amazonaws.com",
                "sns.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": ""
        }
    ]
}')

# extract the role arn from the response and store it in a variable

role_arn=$(echo $role_response | jq -r '.Role.Arn')


#print the role arn

echo"Role ARN is : $role_arn"

#attach permissions to the role

aws iam attach-role-policy --role-name $role_name --policy-arn arn:aws:iam::aws:policy/AWSLambda_FullAccess
aws iam attach-role-policy --role-name $role_name --policy-arn arn:aws:iam::aws:policy/AmazonSNSFullAccess

#create the s3 bucket and capture the output in a variable

bucket_output=$(aws s3api create-bucket --bucket $bucket_name --region $AWS_REGION --create-bucket-configuration LocationConstraint=$AWS_REGION)

#print the ouput from the varibale

echo"Bucket cration output : $bucket_output"

#Upload a file to the bucket

aws s3 cp ./example_file.txt s3://"$bucket_name"/example_file.txt

#create a Zip file to upload Lamda function

Zip -r s3-lambda-function.zip ./s3-lambda-function

sleep 5

#create a Lambda function
aws lambda create-funaction \
    --region $AWS_REGION \
    --function-name $lambda_function_name \
    --runtime "python3.8" \
    --handler "s3-lambda-function/s3-lambda-function.lambda_handler" \
    --memory-size 128 \
    --timeout 30 \
    --role "arn:aws:iam::$aws_account_id:role/$role_name"
    --zip-file fileb://s3-lambda-function.zip

#add permissions to s3 bucket to invoke lambda

aws lambda add-permission \
    --function-name $lambda_function_name \
    --statement-id s3-lambda-sns-permission \
    --action lambda:InvokeFunction \
    --principal s3.amazonaws.com \
    --source-arn arn:aws:s3:::$bucket_name \
    --source-account $aws_account_id

#create an s3 event trigger for the lambda function

lamdaFunction="arn:aws:lambda:$AWS_REGION:$AWS_ID:function:s3-lambda-function"

aws s3api put-bucket-notification-configuration \
    --region $AWS_REGION \
    --bucket $bucket_name \
    --notification-configuration '{
        "LambdaFunctionConfigurations": [
            {
                "LambdaFunctionArn": "'$lamdaFunction'"
                "Events": ["s3:ObjectCreated:*"]
            }
        ]
        }'

#create an sns topic and save  the topic arn in a variable

topic_arn=$(aws sns create-topic --name s3-lambda-sns --output json | jq -r '.TopicArn')


#print the topicArn

echo "Topic ARN is : $topic_arn"

#trigger SNS topic using Lambda function

#add Sns publish permisiion to the lambda function

aws sns subscribe \
    --topic-arn $topic_arn \
    --protocol email \
    --notification-endpoint "$email_address"

#publish SNS

aws sns publish \
    --topic-arn "$topic_arn "\
    --subject " A new object has been uploaded"
    --message "File has been created in S3 bucket"
