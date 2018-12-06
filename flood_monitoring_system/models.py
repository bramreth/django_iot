from django.db import models

# Create your models here.
class MqttWaterLevelData(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    hardware_serial = models.CharField(max_length=20)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    altitude = models.IntegerField()
    river_height_mm = models.CharField(max_length=6)  # models.IntegerField()

class Sam_Mqtt(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    hardware_serial = models.CharField(max_length=20)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    altitude = models.IntegerField()
    river_height_mm = models.CharField(max_length=6)
    time = models.CharField(max_length=20)


class environmental_agency_flood_data(models.Model):
    sensor_id = models.CharField(max_length = 80)
    label = models.CharField(max_length = 40)
    town = models.CharField(max_length=40)
    river = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=9, decimal_places=7)
    long = models.DecimalField(max_digits=10, decimal_places=7)
    reading = models.FloatField()
    time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def get_newest(self):
        newest = environmental_agency_flood_data.objects.order_by('-time')[:1]

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