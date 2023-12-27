# boto3

## `put_log_events`

```python
from datetime import datetime

import boto3
from loguru import logger

session = boto3.session.Session(profile_name=..., region_name=...)
client = session.client('logs')
LOG_GROUP_NAME = ...


def _create_log_stream(log_stream_name: str) -> None:
    """Create log stream if not exists already.

    Args:
        log_stream_name (str): log stream name.
    """
    try:
        _ = client.create_log_stream(
            logGroupName=LOG_GROUP_NAME,
            logStreamName=log_stream_name
        )
        logger.info(f'Log stream {log_stream_name} created.')
    except client.exceptions.ResourceAlreadyExistsException:
        logger.info(f'Log stream {log_stream_name} already exists.')


def _put_log_events(log_stream_name: str, log_events: list) -> dict:
    """Put log events on the given log stream.

    Args:
        log_stream_name (str): target log stream name.
        log_events (list): list of strings (events message to log).

    Returns:
        Put operation response.
    """
    # Log events must be in the form {'timestamp': ..., 'message': ...}.
    now = int(datetime.now().timestamp() * 1000)
    _log_events = list(
        map(lambda x: {'timestamp': now, 'message': str(x)}, log_events))
    try:
        response = client.put_log_events(
            logGroupName=LOG_GROUP_NAME,
            logStreamName=log_stream_name,
            logEvents=_log_events
        )
        logger.info(f'First log submitted to log stream {log_stream_name}')
    except client.exceptions.InvalidSequenceTokenException as e:
        # Parse exception to retrieve expected sequence token
        sequence_token = str(str(e).split(': ')[-1])
        response = client.put_log_events(
            logGroupName=LOG_GROUP_NAME,
            logStreamName=log_stream_name,
            logEvents=_log_events,
            sequenceToken=sequence_token
        )
    logger.info(f'Events successfully logged to log stream {log_stream_name}.')
    return response


def put_log_events(log_stream_name: str, log_events: list) -> dict:
    """Put log events on the given log stream.

    This function wraps also the (possible) creation of the log stream beforehand.

    Args:
        log_stream_name (str): target log stream name.
        log_events (list): list of strings (events message to log).

    Returns:
        Put operation response.
    """
    _create_log_stream(log_stream_name)
    return _put_log_events(log_stream_name, log_events)
```
