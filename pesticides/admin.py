from django.contrib import admin

from .models import Pesticide, Manufacturer, Adjuvant, Formula, Region, Park, Applicator, Record
admin.site.register(Pesticide)
admin.site.register(Manufacturer)
admin.site.register(Adjuvant)
admin.site.register(Formula)
admin.site.register(Region)
admin.site.register(Park)
admin.site.register(Applicator)
admin.site.register(Record)