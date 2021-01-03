from django.shortcuts import render
from rest_framework import parsers
from .serializers import LotSerializer

# Create your views here.

method_type_get = 'GET'
method_type_post = 'POST'
method_type_update = 'UPDATE'


def assign(request):
    if request.method == method_type_post:
        json_parser = parsers.JSONParser()
        data = json_parser.parse(request)
        serializer = LotSerializer(data=data)

        if serializer.is_valid():
            serializer.validate(data)
            serializer.assign_slot(data)

