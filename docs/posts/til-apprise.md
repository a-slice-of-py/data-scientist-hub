---
date: 2024-07-16
authors:
  - silvio
categories:
  - Solutions
tags:
  - Python
  - AWS
---

# A simple notification pattern based on `apprise`

In my current role I try to learn and experiment with side projects whenever I can. One of these regards the need to notify a developer as soon as an update has been made to internal tools (e.g. the latest release of a private Python library, a new page in the team's knowledge base, etc.).

After some research I came up with a simple solution based on a [pub-sub architecture](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern), [Microsoft Teams webhook](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnethttps://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnet) and the awesome [Apprise](https://github.com/caronc/apprise).

<!-- more -->

![](../assets/apprise-only-light.svg#only-light)
![](../assets/apprise-only-dark.svg#only-dark)

As shown in the diagram, the solution consists in:

- Git repositories as _publishers_, each with a dedicated topic;
- a worker as the single _subscriber_;
- forward passing of each commit metadata from the publishers to the subscriber, which format the metadata in Markdown and publish the message to a dedicated Microsoft Teams channel through Apprise.

I implemented this blueprint with AWS services: CodeCommit repos forward commit events to a Lambda function thanks to several EventBridge rules, and the function reads the target webhook stored in Secrets Manager.

!!! tip "The cherry on top!"
    Since Apprise support Markdown format, if the committer inserts Markdown syntax in the [commit body](https://www.conventionalcommits.org/en/v1.0.0/#summary), all the worker has to do is read the commit message, parse the body and forward it as a message to the recipient!

    In my case, I implemented the worker to search for a `@teams` tag within the commit message and applying the following two rules:
    
    1. if the tag is not found, do not notify anything _(to prevent unwanted spam to the recipients)_;
    2. if the tag is found, everything before must be ignored, and the notification body is made only of what follows the tag within the commit message _(to allow splitting between short commit message and rich commit text to be forwarded as notification message)_.
