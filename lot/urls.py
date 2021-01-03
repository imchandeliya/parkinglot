from django.urls import path
from lot.views import *

urlpatterns = [
    path('company/', company)
]