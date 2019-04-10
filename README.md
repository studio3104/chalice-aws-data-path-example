# chalice-aws-data-path-example

## Usage

Before performing commands below, you gotta have appropriately configured your `~/.aws/config` and `~/.aws/credentials`

### Create the function

```sh
$ pip install chalice
```

```sh
$ chalice deploy
Creating deployment package.
Updating policy for IAM role: chalice-aws-data-path-example-dev
Updating lambda function: chalice-aws-data-path-example-dev-AWSDataPathExample
Resources deployed:
  - Lambda ARN: arn:aws:lambda:ap-northeast-1:************:function:chalice-aws-data-path-example-dev-AWSDataPathExample
```

### Delete the function

```sh
$ chalice delete
Deleting function: arn:aws:lambda:ap-northeast-1:************:function:chalice-aws-data-path-example-dev-AWSDataPathExample
Deleting IAM role: chalice-aws-data-path-example-dev
```
