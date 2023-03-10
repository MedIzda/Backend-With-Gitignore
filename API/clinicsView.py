from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClinicSerializer, ParticularClinicSerializer
from .models import Clinic

@api_view(['GET'])
def getClinics(request):
    clinic = Clinic.objects.all()
    serializer = ClinicSerializer(clinic, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getClinic(request, pk):
    clinic = Clinic.objects.get(id = pk)
    serializer = ParticularClinicSerializer(clinic, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def newClinic(request):
    data = request.data
    clinic = Clinic.objects.create(
        name = data['name']
    )
    serialzer = ParticularClinicSerializer(clinic, many=False)
    
    return Response(serialzer.data)

@api_view(['PUT'])
def updateClinic(request, pk):
    clinic = Clinic.objects.get(id = pk)
    serialzer = ClinicSerializer(clinic, data=request.data, partial=True)
    if serialzer.is_valid():
        serialzer.save()
    else:
        return Response("Failed to update, invalid input data")

    return Response(serialzer.data)

@api_view(['DELETE'])
def removeClinic(request, pk):
    clinic = Clinic.objects.get(id = pk)
    clinic.delete()

    return Response("Clinic was deleted!")