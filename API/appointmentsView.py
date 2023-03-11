from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AppointmentSerializer
from .models import Appointment, Patient, Clinic

@api_view(['GET'])
def getAppointments(request):
    appointment = Appointment.objects.all()
    serializer = AppointmentSerializer(appointment, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getAppointment(request, pk):
    appointment = Appointment.objects.get(id = pk)
    serializer = AppointmentSerializer(appointment, many=False)

    return Response(serializer.data)

@api_view(['GET'])
def getTodays(request, pk):
    appointment = Appointment.objects.get(date = pk)
    serializer = AppointmentSerializer(appointment, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def newAppointment(request):
    data = request.data
    appointment = Appointment.objects.create(
        date = data['date'],
        patient = Patient.objects.get(pesel = data['patient']),
        clinic = Clinic.objects.get(id = data['clinic'])
    )
    serialzer = AppointmentSerializer(appointment, many=False)
    
    return Response(serialzer.data)

@api_view(['PUT'])
def updateAppointment(request, pk):
    appointment = Appointment.objects.get(id = pk)
    serialzer = AppointmentSerializer(appointment, data=request.data, partial=True)
    if serialzer.is_valid():
        serialzer.save()
    else:
        return Response("Failed to update, invalid input data")

    return Response(serialzer.data)

@api_view(['DELETE'])
def removeAppointment(request, pk):
    appointment = Appointment.objects.get(id = pk)
    appointment.delete()

    return Response("Clinic was deleted!")