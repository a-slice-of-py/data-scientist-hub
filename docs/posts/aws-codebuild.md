---
date: 2021-12-21
authors:
  - silvio
categories:
  - TIL
tags:
  - AWS
  - DevOps
---

# AWS CodeBuild local testing

Suppose you have a CodeBuild project triggered by a push on a given branch of a linked CodeCommit repo. If the build is particularly heavy, you might want to ensure its correctness _before_ an actual commit to the related repo - for example, you might be interested in testing the build process specified in `buildspec.yml` locally.

<!-- more -->

Thankfully, AWS [released in 2018](https://aws.amazon.com/it/blogs/devops/announcing-local-build-support-for-aws-codebuild/) the capability to do so with [AWS CodeBuild agent](https://docs.aws.amazon.com/codebuild/latest/userguide/use-codebuild-agent.html). To use it you must:

1. clone the repo with CodeBuild Docker image
2. build it _(~9 GB, it might take time...)_
3. pull of CodeBuild local agent image
4. finally test a buildspec locally!

!!! warning "Warning 1"
    If you are on Windows, pay attention to EOL conversion after cloning (step 1). During build phase (step 2) you might encounter errors like [this](https://github.com/aws/aws-codebuild-docker-images/issues/390).

!!! warning "Warning 2"
    If you are on Windows, you might fail to actually test anything as reported [here](https://github.com/aws/aws-codebuild-docker-images/issues/145) and [here](https://github.com/aws/aws-codebuild-docker-images/issues/137). A possible workaround consists in switching to WSL2.

!!! hint "Hint 1"
    If your build process is particularly heavy, during the test phase (step 4) it might remain stuck in `Waiting for DOWNLOAD_SOURCE` step. Indeed, the default agent behaviour is to _copy_ the source directory: you can instead _mount it_ by using `-m` option in test script, as suggested [here](https://github.com/aws/aws-codebuild-docker-images/issues/195#issuecomment-485595478).

    Doing so, **each build action which interacts with the file system will actually take place in the source directory**.

!!! hint "Hint 2"
    If you want CodeBuild local agent to use a local named profile, you can execute `codebuild_build.sh` with options `-c -p <PROFILE_NAME>`, as suggested [here](https://github.com/aws/aws-codebuild-docker-images/issues/252).
