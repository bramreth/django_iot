from django.apps import AppConfig
import urllib.request, json
from flood_map.models import environmental_agency_flood_data

class FloodMapConfig(AppConfig):
    name = 'flood_map'

    def get_data(self):
        with urllib.request.urlopen("https://environment.data.gov.uk/flood-monitoring/id/stations?RLOIid=1143") as url:
            data = json.loads(url.read().decode())
        with urllib.request.urlopen(data["items"][0]["measures"][0]['@id']) as url2:
            waterdata = json.loads(url2.read().decode())

        viewdata = {
            "pin_data": [
                {
                    "id": data["items"][0]["@id"],
                    "label": data["items"][0]["label"],
                    "river": data["items"][0]["riverName"],
                    "town": data["items"][0]["town"],
                    "lat": data["items"][0]["lat"],
                    "long": data["items"][0]["long"],
                    "reading": waterdata["items"]["latestReading"]["value"],
                    "time": waterdata["items"]["latestReading"]["dateTime"]
                }
            ]
        }
        return (viewdata)

    def ready(self):
        newdata = get_data(self)