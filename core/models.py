from django.contrib.sites.models import Site
from django.db import models

# ALLOWS OAUTH

class Sites(models.Model):
    sites = models.ManyToManyField(Site)