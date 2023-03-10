from rest_framework.serializers import ModelSerializer
from .models import Patient, Clinic, Appointment, Account

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'surname', 'pesel']

class ParticularPatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class ClinicSerializer(ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'name']

class ParticularClinicSerializer(ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['name', 'surname', 'pesel']

class ParticularVisitSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['login', 'password', 'email']

class ParticularAccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'