from django.contrib import admin

from .models import Patient, Clinic
admin.site.register(Patient)
admin.site.register(Clinic)