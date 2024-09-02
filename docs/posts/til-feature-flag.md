---
date: 2024-07-17
authors:
  - silvio
categories:
  - Solutions
tags:
  - Python
  - AWS
---

# F3: flexible feature flags

I am still working on a legacy codebase, so even the smallest change feels slippery and made me fearful. When I was about to implement a _not-so-small_ change in a data processing procedure taking place as one of the first steps of a bigger pipeline, as a painkiller I decided to ask a [feature flag](https://en.wikipedia.org/wiki/Feature_toggle) to come to the rescue!

<!-- more -->

A bit of context: the pipeline provides to some end users the capability to trigger a job execution on AWS, where each job execution consists in several services glued together in both reckless and daring manners (often at the same time!) and the end users control job attributes which are written to a DynamoDB table.

I had two requests about the feature flag:

- the end users must be fully autonomous in turning on and off the feature toggle;
- the feature flag value must be _local_ i.e., based on the single execution, instead of global.

Satisfying both the requests wasn't that easy, but I finally came up with the following solution:

```python
import boto3

def toggle_feature(job_id: Optional[str] = None) -> None:
    import my_library

    my_library.JOB_ID = job_id
    logger.info(f"JOB_ID: {getattr(my_library, 'JOB_ID')}")

    dynamodb = boto3.resource('dynamodb')
    my_library.IS_FEATURE_ENABLED = (
        dynamodb
        .Table(...)
        .get_item(
            Key={'job_id': str(getattr(my_library, 'JOB_ID'))}
        )
        .get('Item', dict())
        .get("is_feature_enabled", False)
    )

    logger.info(f"Feature toggle value: {my_library.IS_FEATURE_ENABLED}")
```

The main ideas are:

- in the Python library handling all the backend code, add a new global attribute `IS_FEATURE_ENABLED`;
- move all the new lines of code behind a guard clause `if my_library.IS_FEATURE_ENABLED: execute_new_code()`;
- introduce a new attribute `is_feature_enabled` for each job in the DynamoDB table, where users can store the feature toggle value;
- at each backend code load, call `toggle_feature` function to set the feature flag value according to the job attributes on the DynamoDB jobs table.
