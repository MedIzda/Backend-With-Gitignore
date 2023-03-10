from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatientSerializer, ParticularPatientSerializer
from .models import Patient

@api_view(['GET'])
def getPatients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPatient(request, pk):
    patient = Patient.objects.get(pesel = pk)
    serializer = PatientSerializer(patient, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def newPatient(request):
    data = request.data
    patient = Patient.objects.create(
        name = data['name'],
        surname = data['surname'],
        pesel = data['pesel']
    )
    serialzer = PatientSerializer(patient, many=False)
    return Response(serialzer.data)

@api_view(['PUT'])
def updatePatient(request, pk):
    patient = Patient.objects.get(pesel = pk)
    serialzer = PatientSerializer(patient, data=request.data, partial=True)
    if serialzer.is_valid():
        serialzer.save()
    else:
        return Response("Failed to update, invalid input data")

    return Response(serialzer.data)

@api_view(['DELETE'])
def removePatient(request, pk):
    patient = Patient.objects.get(pesel = pk)
    patient.delete()

    return Response("Patient was deleted!")