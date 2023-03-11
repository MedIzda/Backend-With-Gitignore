from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AppointmentSerializer
from .models import Appointment, Patient, Clinic

@api_view(['GET'])
def getClinics(request):
    clinic = Appointment.objects.all()
    serializer = AppointmentSerializer(clinic, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getClinic(request, pk):
    clinic = Appointment.objects.get(id = pk)
    serializer = AppointmentSerializer(clinic, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def newClinic(request):
    data = request.data
    clinic = Appointment.objects.create(
        date = data['date'],
        patient = Patient.objects.get(pesel = data['patient']),
        clinic = Clinic.objects.get(id = data['clinic'])
    )
    serialzer = AppointmentSerializer(clinic, many=False)
    
    return Response(serialzer.data)

@api_view(['PUT'])
def updateClinic(request, pk):
    clinic = Appointment.objects.get(id = pk)
    serialzer = AppointmentSerializer(clinic, data=request.data, partial=True)
    if serialzer.is_valid():
        serialzer.save()
    else:
        return Response("Failed to update, invalid input data")

    return Response(serialzer.data)

@api_view(['DELETE'])
def removeClinic(request, pk):
    clinic = Appointment.objects.get(id = pk)
    clinic.delete()

    return Response("Clinic was deleted!")