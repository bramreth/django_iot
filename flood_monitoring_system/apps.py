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

        def query_new_water_levels(url, delay):
            from flood_monitoring_system.models import StationInformation, StationReadings

            while(1):
                try:
                    with urllib.request.urlopen(url) as json_url:
                        httpStatusCode = json_url.getcode()
                        if httpStatusCode == 200:
                            readings = json.loads(json_url.read().decode())
                except:
                    httpStatusCode = 0;

                if not httpStatusCode == 200:
                    print(">>Error getting new water level data")
                else:
                    print(">>Getting new water level data")
                    stations = StationInformation.objects.all()
                    station_measures = []

                    for s in stations:
                        station_measures.append(s.measure_id)

                    for reading in readings['items']:
                        if reading['measure'] in station_measures:
                            current_station = stations[station_measures.index(reading['measure'])]
                            #print(current_station.station_reference)
                            if not reading['value'] == StationReadings.get_newest("", current_station)["pin_data"][0]["reading"]:
                                # print(current_station.station_reference)
                                # print(str(
                                #     StationReadings.get_newest("", current_station)["pin_data"][0]["reading"]))
                                # print(str(reading['value']))
                                new_reading = StationReadings()
                                new_reading.station = current_station
                                new_reading.reading = reading["value"]

                                dt = "" + reading["dateTime"] + ""  # daytime
                                d = dt.split("T")[0]  # day
                                t = dt.split("Z")[0].split("T")[1]  # time

                                new_reading.time = int(
                                    time.mktime(time.strptime(d + " " + t, '%Y-%m-%d %H:%M:%S'))) * 1000
                                # print(new_reading.station)
                                # print(new_reading.reading)
                                # print(new_reading.time)
                                new_reading.save()
                    print(">>Water level data updated")
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

        #Grabs the details for the station at the given url
        def query_station_details(url):
            from flood_monitoring_system.models import StationInformation

            #Check if the website is responsive
            try:
                with urllib.request.urlopen(url) as json_url:
                    httpStatusCode = json_url.getcode()
                    if httpStatusCode == 200: #only try to load the json if there is a connection
                        station_data = json.loads(json_url.read().decode())
            except:
                httpStatusCode = 0; #No connection

            if not httpStatusCode == 200: #Anything other than a 200 will abort the database update
                print(">>No connection to the Environment Agency Real Time flood-monitoring API to gather station data")
            elif not StationInformation.objects.exists(): #No data on the given station in the database
                print(">>Gathing station data:")
                for station in station_data["items"]:
                    if 'RLOIid' in station and 'measures' in station:
                        print(station['notation'])
                        new_station = StationInformation()
                        new_station.station_reference = station["notation"]
                        new_station.RLOIid = station["RLOIid"]
                        new_station.measure_id = station["measures"][0]["@id"]
                        new_station.label = station["label"]
                        new_station.river_name = station["riverName"]
                        new_station.town = station["town"]
                        new_station.lat = station["lat"]
                        new_station.long = station["long"]
                        new_station.save()
            else:
                print(">>Station data in database")

        #Digs for the last couple weeks of data from the stations stored in the database and adds the data to the readings database
        def query_historic_data(url_start, url_end):
            from flood_monitoring_system.models import StationInformation, StationReadings
            stations = StationInformation.objects.all()
            for s in stations:
                if not StationReadings.objects.filter(station=s.station_reference).exists():
                    reading_url = url_start + s.station_reference + url_end
                    print(reading_url)
                    try:
                        with urllib.request.urlopen(reading_url) as json_url:
                            httpStatusCode = json_url.getcode()
                            if httpStatusCode == 200:
                                reading_data = json.loads(json_url.read().decode())
                    except:
                        httpStatusCode = 0;

                    if not httpStatusCode == 200:
                        print("Cannot get historic data for station: " + s.station_reference)
                    else:
                        previous_reading = -100
                        for r in reading_data["items"]:
                            if not r['value'] == previous_reading: #Only adds data if its different than the last value to prevent saving
                                print(s.station_reference + ": " + str(r["value"]))
                                new_reading = StationReadings()
                                new_reading.station = StationInformation.objects.filter(station_reference=s.station_reference)[0]
                                new_reading.reading = r["value"]

                                dt = "" + r["dateTime"] + ""  # daytime
                                d = dt.split("T")[0]  # day
                                t = dt.split("Z")[0].split("T")[1]  # time

                                new_reading.time = int(
                                    time.mktime(time.strptime(d + " " + t, '%Y-%m-%d %H:%M:%S'))) * 1000
                                new_reading.save()
                                previous_reading = r['value']

        #Removes duplicate station readings data to save space
        #Only for debugging use, this should be handled by the historic data query
        def remove_station_readings_duplicates():
            from flood_monitoring_system.models import StationInformation, StationReadings
            stations = StationInformation.objects.all()
            for s in stations:
                readings = StationReadings.objects.filter(station=s)
                readings_count = StationReadings.objects.filter(station=s).count()
                print(s.station_reference + ": " + str(readings_count))
                previous_reading = -100
                for r in readings:
                    if r.reading == previous_reading:
                        r.delete()
                    else:
                        previous_reading = r.reading

        api_base_url = 'https://environment.data.gov.uk/flood-monitoring/'
        query_station_details(api_base_url + "id/stations?riverName=Great%20Stour")
        query_historic_data(api_base_url + "id/stations/", "/readings?_sorted")
        #remove_station_readings_duplicates()
        try:
            pass
            _thread.start_new_thread(query_new_water_levels, ("https://environment.data.gov.uk/flood-monitoring/data/readings?latest", 900))
            #_thread.start_new_thread(query_flood_warnings, ("https://environment.data.gov.uk/flood-monitoring/id/floods?county=kent", 900))
            #_thread.start_new_thread(query_station_details, (api_base_url + "id/stations?lat=51.296693&long=1.105983&dist=50&parameterName=Water%20Level", 86400))
        except:
            print("Error starting thread")
