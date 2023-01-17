# Doctor Droid - Python SDK for custom events

This is a library that will allow developers to push custom stateful events to Doctor Droid Platform. 
Read more [here](https://kenobi.drdroid.io/docs).

## Install the SDK
Run this command to get the latest stable version of the SDK.
```
pip install pydoctordroid
```

## Setup the configuration
You will need to setup local environment variables wherever your application is running that needs to send the events. You will get these from Doctor Droid platform, but for demo, setup them by running the following:
```
export ORG_NAME=DRD
export DRDROID_HOSTNAME=http://apidemo1.drdroid.io:8080
```

## Start sending events
After the configurations are done, you can import the module in your python file and create a DroidEvents object.
```
from pydoctordroid import codemarkers
dr = codemarkers.DroidEvents()
```

You can then send events in the following format:
```
dr.publish(WorkFlow_Name, WorkFlow_State, Attribute_KeyValue_Pairs)
```

For example, creating events for an order placement workflow could look like:
```
dr.publish("Order", "Created", (("ID", "13432"), ("City", "BLR"), ("IS_COD", False)))
```

If you want to publish with a certain timestamp and not default to the current system time, you can pass _event_time_ in epoch time format (seconds).
```
dr.publish("Order", "Created", (("ID", "13432"), ("City", "BLR"), ("IS_COD", False)), event_time=1673439411)
```

## View your workflows
Once your events have been published, you can view the workflow these events are creating and how it resembles the actual business flow for your customers or internal processes. Check out this URL - [http://demo1.drdroid.io](http://demo1.drdroid.io)

Visit [Doctor Droid website](https://drdroid.io?utm_param=github-py) for getting early access and the [integration documentation](https://kenobi.drdroid.io?utm_param=github-py) for some use-cases it can solve. 

For any queries, reach out at [dipesh@drdroid.io](mailto:dipesh@drdroid.io).
