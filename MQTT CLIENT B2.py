import paho.mqtt.publish as publish

def publish_command(device_id, action):
    topic = f"home/{device_id}/control"
    publish.single(topic, action, hostname="mqtt-broker.local")