from umqtt.simple import MQTTClient
import time

client = MQTTClient("pico_001", "broker.emqx.io", 1883)
client.connect()

while True:
    client.publish(b"test/pico", b"hello from pico")
    time.sleep(2)
