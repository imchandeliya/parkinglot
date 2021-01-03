from django.db import models


class ParkingDetailsModel(models.Model):
    car_number = models.CharField(max_length=20)
    slot = models.IntegerField
