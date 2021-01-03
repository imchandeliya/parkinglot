from rest_framework import serializers
from .models.CarModel import *
from rest_framework import exceptions
from .models.Slots import *

def validate_car_number(data):
    car_number = str(data)
    if len(car_number) is 0:
        raise exceptions.ValidationError('car number cannot be blank')
    # need to check if there has to be more validations


def assign_slot(data):

    for i in range(len(slots)) :
        if len(str(slots[i])) is 0:
            slots[i] = data
            break;

    return exceptions.NotAcceptable('Parking lot is full, there is no space to acquire more vehicle')


def unassign_slot(data):


class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

    def validate(self, attrs):
        validate_car_number(attrs['car_number'])
        return attrs

    def assign_slot(self, attrs):
        assign_slot(attrs['car_number'])

    def unassign_slot(self, attrs):
        unassign_slot(attrs['car_number'])
