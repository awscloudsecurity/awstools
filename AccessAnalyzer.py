# CIS Amazon Web Services Benchmark v1.3.0 Section 1.21

import boto3

AWS_CONFIG_FILE='~/.aws/config'
AWS_PROFILE = input("Enter a Profile Name ")
AWS_REGION = input("Enter an AWS Region " )
boto3.setup_default_session(profile_name=AWS_PROFILE, region_name=AWS_REGION)

client = boto3.client('accessanalyzer')

print("Checking if the IAM Access Analyzer is enabled for" , AWS_PROFILE)
paginator = client.get_paginator('list_analyzers')
for response in paginator.paginate():
    print(response)


