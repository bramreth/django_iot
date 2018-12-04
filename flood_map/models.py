from django.db import models

class environmental_agency_flood_data(models.Model):
    sensor_id = label = models.CharField(max_length = 80)
    label = models.CharField(max_length = 40)
    town = models.CharField(max_length=40)
    river = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=9, decimal_places=7)
    long = models.DecimalField(max_digits=10, decimal_places=7)
    reading = models.FloatField()
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
