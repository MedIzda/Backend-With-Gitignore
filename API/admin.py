from django.contrib import admin

from .models import Patient, Clinic, Appointment, Account
admin.site.register(Patient)
admin.site.register(Clinic)
admin.site.register(Appointment)
admin.site.register(Account)