from django.db import models


class CarModel(models.Model):
    car_number = models.CharField(max_length=20)
