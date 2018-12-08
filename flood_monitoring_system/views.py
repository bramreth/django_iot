from django.shortcuts import render
from flood_monitoring_system.models import environmental_agency_flood_data, MqttWaterLevelData
# Create your views here.
query = {}
query['api_data'] = environmental_agency_flood_data.get_newest("")
print(query['api_data'])
query['sensors'] = MqttWaterLevelData.get_newest("")
query['sensors_all'] = MqttWaterLevelData.get_all("")

def index(request):
    return render(request, 'flood_monitoring_system/index.html', {"object_list":query})

def notifications(request):
    return render(request, 'flood_monitoring_system/notifications.html')

def test(request):
    return render(request, 'flood_monitoring_system/test.html', {"object_list":query})


