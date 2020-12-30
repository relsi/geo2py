from django.urls import path
from .views import LocationsMapView

app_name = "locations"

urlpatterns = [
    path("map/", LocationsMapView.as_view()),
]