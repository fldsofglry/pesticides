from django.contrib import admin

from .models import Pesticide, Manufacturer, Adjuvant

admin.site.register(Pesticide)
admin.site.register(Manufacturer)
admin.site.register(Adjuvant)