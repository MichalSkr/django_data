from django.db import models


class DataSet(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=30)
    country = models.CharField(max_length=5)
    os = models.CharField(max_length=10)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.IntegerField()
    revenue = models.IntegerField()
