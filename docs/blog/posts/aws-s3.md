---
date: 2021-12-21
authors:
  - silvio
categories:
  - TIL
tags:
  - AWS
---

# AWS S3 presigned URLs

Solutions to common problems when working with S3 presigned URLs.

<!-- more -->

## `SignatureDoesNotMatch` error

The error can be spotted visiting presigned URL and receiving:

```xml
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<Error>
<Code>SignatureDoesNotMatch</Code>
<Message>The request signature we calculated does not match the signature you provided. Check your key and signing method.</Message>
```

A possible solution is given in [this issue](https://github.com/boto/boto3/issues/1644): specifying in s3 client configuration `s3={​​​​​​'addressing_style': 'virtual'}​​​​​​`.

More on the topic [here](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config).

## Credentials and expiration

Even if presigned URL creation lets you specify the URL duration via `ExpiresIn` parameter, you can experience different url durations, capped to 12 hours despite longer requested value.

The reason behind such behaviour is that credentials used to create the presigned url [take precedence](https://aws.amazon.com/it/premiumsupport/knowledge-center/presigned-url-s3-bucket-expiration/) - in terms of validity duration - over any parameters specified at creation time. At each authentication method corresponds a different timeout, which hits the maximum with of 7 days with access key e secret access key authentication.

If a given presigned url has been created by a Lambda function with a standard role, it should have a [`max_session_duration`](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_iam/Role.html#aws_cdk.aws_iam.Role) which defaults to 1 hour. Despite this default, the CDK IAM Role docs states

> [...] Anyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. [...]

As confirmed in [this issue](https://github.com/boto/boto3/issues/2392#issuecomment-616755975), boto3 S3 client - while creating a presigned url - performs a request for a [temporary access token to STS](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html#API_GetSessionToken_RequestParameters), with a default `DurationSeconds` of 12 hours. Moreover, in [this table](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#stsapi_comparison), the only STS access methods with 12 hours default duration seem to be the ones involving tokens.
