from django.apps import AppConfig
import ttn
import base64, time, datetime
import _thread, threading
import urllib.request, json


class FloodMonitoringSystemConfig(AppConfig):
    name = 'flood_monitoring_system'

    def ready(self):

        app_id = "kentwatersensors"
        access_key = "ttn-account-v2.mRzaS7HOchwKsQxdj1zD-KwjxXAptb7s9pca78Nv7_U"
        port = "1883"
        address = "lora.kent.ac.uk" #"eu.thethings.network"

        def uplink_callback(msg, client):
            try:
                print("hello?!")
                from flood_monitoring_system.models import MqttWaterLevelData
                print("Received uplink from ", msg.dev_id)
                print("----------------------------------------------------------------------------------------------------------------")
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
                print("----------------------------------------------------------------------------------------------------------------")
            except Exception as error:
                print("Error: ", repr(error))
                raise
        print("start mqtt detection")

        mqtt_client = ttn.MQTTClient(app_id, access_key, mqtt_address=address)
        mqtt_client.set_uplink_callback(uplink_callback)
        mqtt_client.connect()

        def query_environment_api(url, delay):
            from flood_monitoring_system.models import environmental_agency_flood_data
            try:
                with urllib.request.urlopen(url) as json_url:
                    httpStatusCode = json_url.getcode()
                    if httpStatusCode == 200:
                        data = json.loads(json_url.read().decode())
            except:
                httpStatusCode = 0;

            if not httpStatusCode == 200:
                print("================================================================================================================")
                print("----------------------------------------------------------------------------------------------------------------")
                print("No connection to the Environment Agency Real Time flood-monitoring API to gather historic data")
                from flood_monitoring_system.models import Notifications

                NoConnectionNotification = Notifications()
                NoConnectionNotification.type = "REST"
                NoConnectionNotification.message = "Lost connection to the Environment Agency Real Time flood-monitoring API."
                NoConnectionNotification.severity_rating = 4
                NoConnectionNotification.severity_message = "Lost connection"
                NoConnectionNotification.time = datetime.datetime.now()
                NoConnectionNotification.save()

            elif not environmental_agency_flood_data.objects.exists():
                print("================================================================================================================")
                print("----------------------------------------------------------------------------------------------------------------")

                print("Environment Agency Real Time flood-monitoring API data found")
                print("Gathering historic data")
                with urllib.request.urlopen("https://environment.data.gov.uk/flood-monitoring/id/stations/E3966/readings?_sorted") as historic_json_url:
                    historicdata = json.loads(historic_json_url.read().decode())

                print("Saving historic data")
                for reading in historicdata["items"]:
                    print(reading["value"])
                    EnvironmentAgencyData = environmental_agency_flood_data()
                    EnvironmentAgencyData.sensor_id = data["items"][0]["@id"]
                    EnvironmentAgencyData.label = data["items"][0]["label"]
                    EnvironmentAgencyData.town = data["items"][0]["town"]
                    EnvironmentAgencyData.river = data["items"][0]["riverName"]
                    EnvironmentAgencyData.lat = data["items"][0]["lat"]
                    EnvironmentAgencyData.long = data["items"][0]["long"]
                    EnvironmentAgencyData.reading = reading["value"]

                    dt = "" + reading["dateTime"] + ""  # daytime
                    d = dt.split("T")[0]  # day
                    t = dt.split("Z")[0].split("T")[1]  # time

                    EnvironmentAgencyData.time = int(
                        time.mktime(time.strptime(d + " " + t, '%Y-%m-%d %H:%M:%S'))) * 1000
                    EnvironmentAgencyData.save()
                print("Historic data saved")
                print("----------------------------------------------------------------------------------------------------------------")
                print("================================================================================================================")


            while(1):
                try:
                    with urllib.request.urlopen(data["items"][0]["measures"][0]['@id']) as json_url_2:
                        httpStatusCode = json_url_2.getcode()
                        if httpStatusCode == 200:
                            waterdata = json.loads(json_url_2.read().decode())
                except:
                    httpStatusCode = 0;

                if not httpStatusCode == 200:
                    print("================================================================================================================")
                    print("----------------------------------------------------------------------------------------------------------------")
                    print("No connection to the Environment Agency Real Time flood-monitoring API to gather latest reading")
                else:
                    print("================================================================================================================")
                    print("----------------------------------------------------------------------------------------------------------------")
                    print("Queried Environment Agency Real Time flood-monitoring API")
                    print(data["items"][0]["@id"])
                    print(data["items"][0]["label"])
                    print(data["items"][0]["lat"])
                    print(data["items"][0]["long"])
                    print(data["items"][0]["riverName"])
                    print(data["items"][0]["town"])
                    print(waterdata["items"]["latestReading"]["value"])
                    print(waterdata["items"]["latestReading"]["dateTime"])
                    EnvironmentAgencyData = environmental_agency_flood_data()
                    EnvironmentAgencyData.sensor_id = data["items"][0]["@id"]
                    EnvironmentAgencyData.label = data["items"][0]["label"]
                    EnvironmentAgencyData.town = data["items"][0]["town"]
                    EnvironmentAgencyData.river = data["items"][0]["riverName"]
                    EnvironmentAgencyData.lat = data["items"][0]["lat"]
                    EnvironmentAgencyData.long = data["items"][0]["long"]
                    EnvironmentAgencyData.reading = waterdata["items"]["latestReading"]["value"]

                    dt = "" + waterdata["items"]["latestReading"]["dateTime"] + ""  # daytime
                    d = dt.split("T")[0]  # day
                    t = dt.split("Z")[0].split("T")[1]  # time

                    EnvironmentAgencyData.time = int(time.mktime(time.strptime(d + " " + t, '%Y-%m-%d %H:%M:%S'))) * 1000

                    if (int(environmental_agency_flood_data.get_newest("")["pin_data"][0]["time"]) < EnvironmentAgencyData.time):
                        EnvironmentAgencyData.save()
                        print("Environment Agency Real Time flood-monitoring API data SAVED")
                    else:
                        print("Environment Agency Real Time flood-monitoring API data NOT SAVED")
                print("----------------------------------------------------------------------------------------------------------------")
                print("================================================================================================================")
                time.sleep(delay)

        def query_flood_warnings(url, delay):
            from flood_monitoring_system.models import Notifications
            while(1):
                try:
                    with urllib.request.urlopen(url) as flood_data_url:
                        httpStatusCode = flood_data_url.getcode()
                        if httpStatusCode == 200:
                            floodData = json.loads(flood_data_url.read().decode())
                except:
                    httpStatusCode = 0;

                if not httpStatusCode == 200:
                    print("================================================================================================================")
                    print("----------------------------------------------------------------------------------------------------------------")
                    print("No connection to the Environment Agency Real Time flood-monitoring API to gather flood warnings")
                    #DO SOMETHING HERE TO SAVE THIS FACT IN THE NOTIFICATIONS DB
                elif not floodData['items']:
                    print("================================================================================================================")
                    print("----------------------------------------------------------------------------------------------------------------")
                    print("No flood warnings")
                else:
                    print("================================================================================================================")
                    print("----------------------------------------------------------------------------------------------------------------")
                    print("Found flood warnings:")
                    for warning in floodData['items']:
                        print(warning['description'])
                        if warning['description'] == "The Great Stour at Canterbury":
                            Warning = Notifications()
                            Warning.type = "FLOOD"
                            Warning.message = warning['message']
                            Warning.severity_rating = warning['severityLevel']
                            Warning.severity_message = warning['severity']
                            Warning.time = warning['timeRaised']
                            Warning.save()
                            print("Flood warning saved")
                print("----------------------------------------------------------------------------------------------------------------")
                print("================================================================================================================")
                time.sleep(delay)

        try:
            _thread.start_new_thread(query_environment_api, ("https://environment.data.gov.uk/flood-monitoring/id/stations?RLOIid=1143", 900))
            _thread.start_new_thread(query_flood_warnings, ("https://environment.data.gov.uk/flood-monitoring/id/floods?county=kent", 900))
        except:
            print("Error starting thread")
