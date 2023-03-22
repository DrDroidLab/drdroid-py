# Doctor Droid - Python SDK for custom events

This is a library that will allow developers to push custom stateful events to Doctor Droid Platform.
Read more [here](https://docs.drdroid.io/docs).

## Install the SDK

Run this command to get the latest stable version of the SDK.

```
pip install drdroid-sdk
```
## Env vars

| Env Var Name       | Description                                 | Default                   |
|--------------------|---------------------------------------------|---------------------------|
| DRDROID_HOSTNAME   | Ingestion endpoint for the events collected | https://ingest.drdroid.io |
| DRDROID_AUTH_TOKEN | Authentication token for platform           | ---                       |
| DRDROID_DEBUG      | Enable debug logs for sdk                   | False                     |


## Configuration
Identify the auth token needed for the events to be published to the platform by visiting [site](https://app.drdroid.io)
Once auth token is available, you can set the env var as:
```shell
export DRDROID_AUTH_TOKEN=<TOKEN>
```


## Start sending events
A global instance of `DrDroid` is created by default based on the config provided through the env vars.
The global instance can then be used to publish events by directly calling the `publish` api.

```python
import pydoctordroid

pydoctordroid.publish("Order_Created", {"ID": "13432", "City": "BLR", "IS_COD": False})
```

Alternatively, you can import the module in your python file and create a DrDroid object.
```python
from pydoctordroid import DrDroid
dr = DrDroid()
```

You can then send events in the following format:

```
dr.publish('Event_Name', Attribute_KeyValue_Dict)
```

For example, creating events for an order placement workflow could look like:

```python
dr.publish("Order_Created", {"ID": "13432", "City": "BLR", "IS_COD": False})
```

If you want to publish with a certain timestamp and not default to the current system time, you can pass _event_time_ in
epoch time format (milliseconds).

```python
dr.publish("Order_Created", {"ID": "13432", "City": "BLR", "IS_COD": False}, event_time=datetime.now())
```


## View your workflows

Once your events have been published, you can view the workflow these events in your DrDroid account @ [https://app.drdroid.io](https://app.drdroid.io).

Visit [Doctor Droid website](https://drdroid.io?utm_param=github-py) for getting early access.
Go through our [documentation](https://docs.drdroid.io?utm_param=github-py) to learn more.

For any queries, reach out at [dipesh@drdroid.io](mailto:dipesh@drdroid.io).
