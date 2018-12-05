from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'flood_monitoring_system/index.html', {'pin_data': [{'id': 'http://environment.data.gov.uk/flood-monitoring/id/stations/E3966', 'label': 'Vauxhall Bridge', 'river': 'Great Stour', 'town': 'Hales Place', 'lat': 51.296693, 'long': 1.105983, 'reading': 0.635, 'time': '2018-12-02T18:00:00Z'}, {'id': '1', 'label': 'Canterbury Central', 'river': 'Great Stour', 'town': 'Canterbury', 'lat': 51.2802, 'long': 1.0789, 'reading': 1, 'time': '2018-12-02'}]})
    #return render(request, 'flood_monitoring_system/index.html'