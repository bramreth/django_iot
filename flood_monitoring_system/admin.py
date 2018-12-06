from django.contrib import admin
from flood_monitoring_system.models import environmental_agency_flood_data, MqttWaterLevelData,Sam_Mqtt

admin.site.register(environmental_agency_flood_data)
admin.site.register(MqttWaterLevelData)
admin.site.register(Sam_Mqtt)