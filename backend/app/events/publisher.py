from dapr.clients import DaprClient
import json
import logging

logger = logging.getLogger(__name__)

PUBSUB_NAME = "pubsub"

def publish_event(topic: str, data: dict, event_type: str = "com.hackathon.event"):
    """
    Publishes an event to the configured Dapr PubSub component.
    """
    try:
        with DaprClient() as client:
            client.publish_event(
                pubsub_name=PUBSUB_NAME,
                topic_name=topic,
                data=json.dumps(data),
                data_content_type='application/json',
                metadata={"cloudevent.type": event_type}
            )
            logger.info(f"Published event to {topic}: {data}")
    except Exception as e:
        logger.error(f"Failed to publish event to {topic}: {e}")
        raise e
