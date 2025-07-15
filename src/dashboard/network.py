# Network communication (MQTT/OPC UA)
# Netzwerkkommunikation
import paho.mqtt.client as mqtt
import json

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "sorting/status"

def publish_status(status, object_type):
    """
    Publishes system status and object type to MQTT broker.
    """
    client = mqtt.Client()
    client.connect(BROKER, PORT)
    payload = json.dumps({"status": status, "object_type": object_type})
    client.publish(TOPIC, payload)
    client.disconnect()

if __name__ == "__main__":
    # Example usage
    publish_status("Running", "Red")
