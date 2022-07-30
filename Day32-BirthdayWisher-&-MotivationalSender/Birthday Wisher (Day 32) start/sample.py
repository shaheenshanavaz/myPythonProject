# from smart_open import open
# # stream lines from an S3 object
# for line in open('s3://commoncrawl/robots.txt'):
#     print(repr(line))
#     break

import smtplib
import datetime as dt
import random

# importing the boto3 library
import boto3
# connect to S3 using boto3 client
s3_client = boto3.client(service_name='s3')
# get S3 object
result = s3_client.get_object(Bucket='quotesbucket', Key='quotes.txt')
#Read a text file line by line using splitlines object
for line in result["Body"].read().splitlines():
    each_line = line.decode('utf-8')
    quote = random.choice(each_line)
    print(each_line)
user = "shaheenpython@gmail.com"
password = "asdf@1234"
quote = ""
# with open("quotes.txt") as file:
#    line = file.readlines()
#    quote = random.choice(line)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= user, password = password)
    recipients = ["shaheen.shanavaz94@gmail.com", "anupbdn@gmail.com"]
    connection.sendmail(from_addr=user,
                        to_addrs=", ".join(recipients),
                        msg=f"Subject: Today's Positivity Quotes\n\n {quote} ")
    now = dt.datetime.now()

