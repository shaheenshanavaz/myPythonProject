import json

import boto3,random
from botocore.exceptions import ClientError


def send_email():
    # connect to S3 using boto3 client
    s3_client = boto3.client(service_name='s3')
    # get S3 object ,decodes and splits each line --(try to print the result)
    result = s3_client.get_object(Bucket='quotesbucket123', Key='quotes.txt')["Body"].read().decode().splitlines()
    quote = ""
    #randomly gets a line from result
    quote = random.choice(result)
    print(quote)
    SENDER = "shaheenpython@gmail.com"  # must be verified in AWS SES Email
    RECIPIENT = "shaheen.shanavaz94@gmail.com"  # must be verified in AWS SES Email

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-1"

    # The subject line for the email.
    SUBJECT = "Today's Motivational Quote"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Quote of the day - + quote +\r\n"
                 "This email was sent with a Motivational Quote on a sceduled time using Amazon SES and"
                 "AWS SDK for Python (Boto)."
                 )

    # The HTML body of the email. and using a "fstring" to pass python variable in html
    BODY_HTML = f"""<html>
    <head></head>
    <body>
    <h1>Quote of the day - {quote} </h1>
    <p>This email was sent with a Motivational Quote on a sceduled time using
        <a href='https://aws.amazon.com/ses/'> Amazon SES`</a> and
        <a href='https://aws.amazon.com/sdk-for-python/'>
        AWS SDK for Python (Boto)</a>.</p>
    </body>
    </html>
                """

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {

                        'Data': BODY_HTML
                    },
                    'Text': {

                        'Data': BODY_TEXT
                    },
                },
                'Subject': {

                    'Data': SUBJECT
                },
            },
            Source=SENDER
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def lambda_handler(event, context):
    # TODO implement
    send_email()
