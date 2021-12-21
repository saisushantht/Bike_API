from django.db import models


class Bike(models.Model):
    name  = models.CharField(max_length=100)
    top_speed = models.IntegerField()
