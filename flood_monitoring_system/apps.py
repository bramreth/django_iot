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
            # this likely isnt the best method of passing data to the database, the issue is the whole app isn't
            # ready at the start of this file so we cant import the models until this ready function is called
            # feel free to tell me why im an idiot later.
            from flood_monitoring_system.models import MqttWaterLevelData
            print("Received uplink from ", msg.dev_id)
            print("--------------")
            print(msg.hardware_serial)
            print(msg.metadata.time)
            print(msg.payload_raw)
            # tst = int(base64.b64decode(msg.payload_raw).encode('hex'), 16) # in millimeters
            # print(str(tst))
            print(msg.metadata.altitude)
            print(msg.metadata.longitude)
            print(msg.metadata.latitude)
            tmp = MqttWaterLevelData()
            tmp.time = msg.metadata.time
            tmp.hardware_serial = msg.hardware_serial
            tmp.longitude = msg.metadata.longitude
            tmp.latitude = msg.metadata.latitude
            tmp.altitude = msg.metadata.altitude
            tmp.river_height_mm = msg.payload_raw  # int(base64.b64decode(msg.payload_raw).encode('hex'), 16)
            tmp.save()
            print("!-------------")

        print("start mqtt detection")

        mqtt_client = ttn.MQTTClient(app_id, access_key, mqtt_address=address)
        mqtt_client.set_uplink_callback(uplink_callback)

        mqtt_client.set_uplink_callback(uplink_callback)
        mqtt_client.connect()
