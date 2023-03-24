from django.contrib import admin

from .models import *
admin.site.register(Patient)
admin.site.register(Clinic)
admin.site.register(Appointment)
admin.site.register(Account)
admin.site.register(Location)