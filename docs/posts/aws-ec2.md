---
date: 2022-01-19
authors:
  - silvio
categories:
  - TIL
tags:
  - AWS
---

# Amazon EC2 instance debug

<!-- more -->

To check instance initialization:

- establish an SSH connection;
- inspect logs located at `/var/log/cloud-init-output.log` as suggested [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html#user-data-console).
