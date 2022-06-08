# Lists all users and if they have an access key and the key status
import boto3

# Create IAM client
resource = boto3.resource('iam')
client = boto3.client('iam')
sts_client = boto3.client('sts')
key = 'LastUsedDate'

print ('Check IAM users for Access Keys')

for user in resource.users.all():
    Metadata = client.list_access_keys(UserName=user.user_name)
    if Metadata['AccessKeyMetadata'] :
        for key in user.access_keys.all():
            AccessId = key.access_key_id
            Status = key.status
            LastUsed = client.get_access_key_last_used(AccessKeyId=AccessId)
            if (Status == "Active"):
                if key in LastUsed['AccessKeyLastUsed']:
                    print ("User: " , user.user_name , "Key: " , AccessId , "AK Last Used: " , LastUsed['AccessKeyLastUsed'][key])
                else:
                    print ("User: ", user.user_name, "Key: ", AccessId , "Key is Active but NEVER USED")
            else:
                print ("User: ", user.user_name , "key: ", AccessId , "Keys are InActive")
    else:
        print ("User: ", user.user_name , "No keys for this user")
