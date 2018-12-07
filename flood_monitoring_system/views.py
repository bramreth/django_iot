from django.shortcuts import render
from flood_monitoring_system.models import environmental_agency_flood_data, MqttWaterLevelData
# Create your views here.
query = {}
query['api_data'] = environmental_agency_flood_data.get_newest("")
query['sensor_one'] = MqttWaterLevelData.objects.filter(hardware_serial="C0EE400001012345").values()
query['sensor_two'] = MqttWaterLevelData.objects.filter(hardware_serial="C0EE4000010109F3").values()

def index(request):
    return render(request, 'flood_monitoring_system/index.html', {"object_list":query})

def notifications(request):
    return render(request, 'flood_monitoring_system/notifications.html')

def test(request):
    return render(request, 'flood_monitoring_system/test.html', {"object_list":query})


