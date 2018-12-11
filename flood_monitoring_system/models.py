from email._header_value_parser import Domain
from _datetime import datetime, timedelta
from django.db import models

# Create your models here.
class MqttWaterLevelData(models.Model):
    hardware_serial = models.CharField(max_length=20)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    altitude = models.IntegerField()
    river_height_mm = models.CharField(max_length=6)
    time = models.CharField(max_length=20)

    class Meta:
        unique_together = ("time", "hardware_serial")

    def get_newest(self):
        newest = MqttWaterLevelData.objects.all().order_by('-time')[:1]
        viewdata = {
            "pin_data": [
            ]
        }
        for name in MqttWaterLevelData.objects.all().values("hardware_serial").distinct():
            print(name["hardware_serial"])
            newest = MqttWaterLevelData.objects.all().filter(hardware_serial=name["hardware_serial"]).order_by('-time')[:1]
            viewdata["pin_data"].append({
                    "id": newest[0].hardware_serial,
                    "lat": newest[0].latitude,
                    "long": newest[0].longitude,
                    "alt": newest[0].altitude,
                    "reading": newest[0].river_height_mm,
                    "time": newest[0].time
                })
        #print(viewdata)
        return viewdata

    def get_all(self):
        #results = MqttWaterLevelData.objects.
        viewdata = {
            "results": []
        }
        for name in MqttWaterLevelData.objects.all().values("hardware_serial").distinct():
            newest = MqttWaterLevelData.objects.all().filter(hardware_serial=name["hardware_serial"]).order_by('-time')
            heights_and_times = []
            for item in newest:
                heights_and_times.append((item.time, item.river_height_mm))
            viewdata["results"].append({
                "id": name,
                "time_reading": heights_and_times,
                "lat": newest[0].latitude,
                "long": newest[0].longitude,
            })
        #print(viewdata)
        return viewdata

    def get_between_dates(self, min_time, max_time):
        viewdata = {
            "results": []
        }
        for name in MqttWaterLevelData.objects.all().values("hardware_serial").distinct():
            all_for_station = MqttWaterLevelData.objects.all().filter(hardware_serial=name["hardware_serial"]).order_by('-time')
            heights_and_times = []
            for item in all_for_station:
                cur_time = datetime.fromtimestamp(int(item.time[0:10]))
                if max_time > cur_time > min_time:
                    heights_and_times.append((item.time, item.river_height_mm))
            viewdata["results"].append({
                "id": name,
                "time_reading": heights_and_times,
                "lat": all_for_station[0].latitude,
                "long": all_for_station[0].longitude,
            })

        return viewdata


    def get_presets(self):
        viewdata = {
            "day": [],
            "week": [],
            "month": []
        }
        for name in MqttWaterLevelData.objects.all().values("hardware_serial").distinct():
            all_for_station = MqttWaterLevelData.objects.all().filter(hardware_serial=name["hardware_serial"]).order_by('-time')
            day = []
            week = []
            month = []
            for item in all_for_station:
                cur_time = datetime.fromtimestamp(int(item.time[0:10]))
                if cur_time > datetime.now() - timedelta(days=30):
                    month.append((item.time, item.river_height_mm))
                if cur_time > datetime.now() - timedelta(days=7):
                    week.append((item.time, item.river_height_mm))
                if cur_time > datetime.now() - timedelta(days=1):
                    day.append((item.time, item.river_height_mm))

            viewdata["day"].append({
                "id": name,
                "time_reading": day,
                "lat": all_for_station[0].latitude,
                "long": all_for_station[0].longitude,
            })

            viewdata["week"].append({
                "id": name,
                "time_reading": week,
                "lat": all_for_station[0].latitude,
                "long": all_for_station[0].longitude,
            })

            viewdata["month"].append({
                "id": name,
                "time_reading": month,
                "lat": all_for_station[0].latitude,
                "long": all_for_station[0].longitude,
            })

        return viewdata


class environmental_agency_flood_data(models.Model):
    sensor_id = models.CharField(max_length=80)
    label = models.CharField(max_length=40)
    town = models.CharField(max_length=40)
    river = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=9, decimal_places=7)
    long = models.DecimalField(max_digits=10, decimal_places=7)
    reading = models.FloatField()
    time = models.CharField(max_length = 20)

    def get_newest(self):
        newest = environmental_agency_flood_data.objects.all().order_by('-time')[:1]

        viewdata = {
            "pin_data": [
                {
                    "id": newest[0].sensor_id,
                    "label": newest[0].label,
                    "river": newest[0].river,
                    "town": newest[0].town,
                    "lat": newest[0].lat,
                    "long": newest[0].long,
                    "reading": newest[0].reading,
                    "time": newest[0].time
                }
            ]
        }
        return viewdata

    def get_all(self):
        newest = environmental_agency_flood_data.objects.all().order_by('-time')
        viewdata = {
            "results": []
        }
        heights_and_times = []
        for item in newest:
            heights_and_times.append((item.time, item.reading*1000))
            viewdata["results"].append({
                "id": newest[0].label,
                "time_reading": heights_and_times,
                "lat": newest[0].lat,
                "long": newest[0].long,
            })
        return viewdata


class test_environmental_agency_flood_data(models.Model):
    sensor_id = models.CharField(max_length = 80)
    label = models.CharField(max_length = 40)
    town = models.CharField(max_length=40)
    river = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=9, decimal_places=7)
    long = models.DecimalField(max_digits=10, decimal_places=7)
    reading = models.FloatField()
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    station = models.CharField(null=False, default=False, max_length=10)

    def get_newest(self):
        newest = test_environmental_agency_flood_data.objects.all().order_by('-time')[:1]

        viewdata = {
            "pin_data": [
                {
                    "id": newest[0].sensor_id,
                    "label": newest[0].label,
                    "river": newest[0].sensor_id,
                    "town": newest[0].town,
                    "lat": newest[0].lat,
                    "long": newest[0].long,
                    "reading": newest[0].reading,
                    "time": newest[0].time
                }
            ]
        }
        return viewdata

class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=64)

class Subscriptions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, default=False, on_delete=models.CASCADE)
    label = models.CharField(max_length=50, null=False, default="")
    station = models.CharField(max_length=10)

class Notifications(models.Model):
    NOTIFICATION_TYPE = (
        ("MQTT", "MQTT service"),
        ("REST", "Environment Agency Real Time flood-monitoring API"),
        ("FLOOD", "Flood warning")
    )
    user = models.ForeignKey(User, null=False, default=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, choices=NOTIFICATION_TYPE)
    message = models.CharField(max_length=1000)
    severity_rating = models.IntegerField()
    severity_message = models.CharField(max_length=40)
    time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    read = models.BooleanField(default=False)

class StationInformation(models.Model):
    station_reference = models.CharField(primary_key=True, max_length=20)
    RLOIid = models.CharField(max_length=10)
    measure_id = models.CharField(max_length=200)
    label = models.CharField(max_length=40)
    town = models.CharField(max_length=40)
    river_name = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=9, decimal_places=7)
    long = models.DecimalField(max_digits=10, decimal_places=7)

class StationReadings(models.Model):
    station = models.ForeignKey(StationInformation, on_delete=models.CASCADE)
    reading = models.FloatField()
    time = models.CharField(max_length=20)