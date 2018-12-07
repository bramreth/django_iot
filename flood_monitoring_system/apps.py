from django.apps import AppConfig
import ttn
import base64, time, datetime
import _thread, threading

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
            print(msg.metadata.altitude)
            print(msg.metadata.longitude)
            print(msg.metadata.latitude)
            MQTTData = MqttWaterLevelData()
            MQTTData.hardware_serial = msg.hardware_serial
            MQTTData.longitude = msg.metadata.longitude
            MQTTData.latitude = msg.metadata.latitude
            MQTTData.altitude = msg.metadata.altitude
            MQTTData.river_height_mm = int.from_bytes(base64.b64decode(""+msg.payload_raw+""), 'big')  # int(base64.b64decode(msg.payload_raw).encode('hex'), 16)
            dt = ""+msg.metadata.time+"" #daytime
            d = dt.split("T")[0]   #day
            t = dt.split(".")[0].split("T")[1] #time
            MQTTData.time = int(time.mktime(time.strptime(d+" "+t, '%Y-%m-%d %H:%M:%S'))) * 1000 #timestamp milliseconds
            MQTTData.save()
            print("-------------")

        print("start mqtt detection")

        mqtt_client = ttn.MQTTClient(app_id, access_key, mqtt_address=address)
        mqtt_client.set_uplink_callback(uplink_callback)
        mqtt_client.connect()

        def query_environment_api(url, delay):
            from flood_monitoring_system.models import environmental_agency_flood_data
            while(1):
                print(_thread.get_ident())
                time.sleep(2)
        try:
            print(threading.current_thread())
            _thread.start_new_thread(query_environment_api, ("https://environment.data.gov.uk/flood-monitoring/id/stations?RLOIid=1143", 900))
        except:
            print("Error starting thread")
