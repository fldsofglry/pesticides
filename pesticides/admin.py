from django.contrib import admin

from .models import Pesticide, Manufacturer

admin.site.register(Pesticide)
admin.site.register(Manufacturer)