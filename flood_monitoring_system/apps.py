from django.apps import AppConfig
import ttn
import base64

class FloodMonitoringSystemConfig(AppConfig):
    name = 'flood_monitoring_system'

    def ready(self):

        app_id = "kentwatersensors"
        access_key = "ttn-account-v2.7j6Z9OduNwFW7il2Sd28YYF4Q-8l9rDDPaNRFw06-GM"
        port = "1883"
        address = "eu.thethings.network"

        def uplink_callback(msg, client):
            print("Received uplink from ", msg.dev_id)
            print("--------------")
            print(msg.hardware_serial)
            print(msg.metadata.time)
            print(msg.payload_raw)
            tst = int(base64.b64decode(msg.payload_raw).encode('hex'), 16) # in millimeters
            print(str(tst))
            print(msg.metadata.altitude)
            print(msg.metadata.longitude)
            print(msg.metadata.latitude)
            print("--------------")

        print("start mqtt detection")

        mqtt_client = ttn.MQTTClient(app_id, access_key, mqtt_address=address)
        mqtt_client.set_uplink_callback(uplink_callback)

        mqtt_client.set_uplink_callback(uplink_callback)
        mqtt_client.connect()
