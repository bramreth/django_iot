from django.db import models

# Create your models here.
class MqttWaterLevelData(models.Model):
    time = models.CharField(max_length=30)
    hardware_serial = models.CharField(max_length=20)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    altitude = models.IntegerField()
    river_height_mm = models.CharField(max_length=6)  # models.IntegerField()

    class Meta:
        unique_together = ("time", "hardware_serial")

