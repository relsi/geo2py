
from django.contrib.gis.db.models import PointField
from django.db import models

class Location(models.Model):
    place = models.CharField(max_length=255)
    location = PointField()