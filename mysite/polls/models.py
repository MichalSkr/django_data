from django.db import models


class DataSet(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=30)
    country = models.CharField(max_length=5, primary_key=True)
    os = models.CharField(max_length=10)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()
