from django.apps import AppConfig
from .models import Slots
import os


def startup():
    Slots.slots = [''] * os.getenv("TOTAL_SLOTS")

class LotConfig(AppConfig):
    name = 'lot'
    startup()
