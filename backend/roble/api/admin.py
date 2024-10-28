from django.contrib import admin
from .models import Poi

# Register your models here.
models = [
    Poi
]
admin.site.register(models)