from django.shortcuts import render
import urllib.request, json
from flood_map.models import environmental_agency_flood_data

def index(request):

    #return render(request, 'flood_map/map.html', {'pin_data': [{'id': 'http://environment.data.gov.uk/flood-monitoring/id/stations/E3966', 'label': 'Vauxhall Bridge', 'river': 'Great Stour', 'town': 'Hales Place', 'lat': 51.296693, 'long': 1.105983, 'reading': 0.635, 'time': '2018-12-02T18:00:00Z'}, {'id': '1', 'label': 'Canterbury Central', 'river': 'Great Stour', 'town': 'Canterbury', 'lat': 51.2802, 'long': 1.0789, 'reading': 1, 'time': '2018-12-02'}]})
    return render(request, 'flood_map/map.html', environmental_agency_flood_data.get_newest(""))


def get_data():
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