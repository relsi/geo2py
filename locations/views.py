import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import Location

class LocationsMapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        location = super().get_context_data(**kwargs)
        location["locations"] = json.loads(serialize("geojson", Location.objects.all()))
        return location
