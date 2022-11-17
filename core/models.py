from django.db import models
from django.contrib.sites.models import Site





# ALLOWS OAUTH

class Sites(models.Model):
    sites = models.ManyToManyField(Site)