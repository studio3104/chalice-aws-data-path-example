from chalice import Chalice

import boto3


app = Chalice(app_name='chalice-aws-data-path-example')
personalize = boto3.client('personalize')


@app.lambda_function(name='AWSDataPathExample')
def lambda_handler(event, context):
    print(personalize)
