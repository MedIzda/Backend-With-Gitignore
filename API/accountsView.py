from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import AccountSerializer, ParticularAccountSerializer
from .models import Account

@api_view(['get'])
def getAccounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getAccount(request, pk):
    account = Account.objects.get(ID=pk)
    serializer = ParticularAccountSerializer(account, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def newAccount(request):
    data = request.data
    account = Account.objects.create(
        login = data['login'],
        password = data['password'],
        email = data['email'],
        name = data['name'],
        surname = data['surname'],
        title = data['title']
    )
    
    serializer = ParticularAccountSerializer(account, many=False)

    return Response(serializer.data)

@api_view(['PUT'])
def updateAccount(request, pk):
    account = Account.objects.get(ID = pk)
    serializer = ParticularAccountSerializer(account, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("Failed to update, invalid input data")
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteAccount(request, pk):
    account = Account.objects.get(ID = pk)
    account.delete()

    return Response('Account was deleted')

def login(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response('Succesfully logged in')
    else:
        return Response('Invalid credentials')
    
def logout(request):
    logout(request)
    return Response('Succesfully logged out')