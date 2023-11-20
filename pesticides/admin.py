from django.contrib import admin

from .models import Pesticide, Manufacturer, Adjuvant, Formula

admin.site.register(Pesticide)
admin.site.register(Manufacturer)
admin.site.register(Adjuvant)
admin.site.register(Formula)