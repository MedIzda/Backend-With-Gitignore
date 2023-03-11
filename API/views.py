from .patientsView import *
from .clinicsView import *
from .appointmentsView import *
from .accountsView import *

@api_view(['GET'])
def getRoutes(request):
    patients = [{
            "Endpoint": "/patients/",
            "Method": "GET",
            "Body": None,
            "Descp": "List of all patients"
         },
         {
            "Endpoint": "/patients/create",
            "Method": "POST",
            "Body": {
                "name" : "",
                "surname": "",
                "pesel": ""
            },
            "Descp": "Creating a new patient"
         },
        {
            "Endpoint": "/patients/pesel",
            "Method": "GET",
            "Body": None,
            "Descp": "Viewing all details about a given patient"
         },
        {
            "Endpoint": "/patients/pesel/delete",
            "Method": "DELETE",
            "Body": None,
            "Descp": "Deletes currently selected patient from the database"
         },
        {
            "Endpoint": "/patients/pesel/update",
            "Method": "PUT",
            "Body": {
                "name":"",
                "surname":""
            },
            "Descp": "Updates information of currently selected patient"
         },
    ]

    clinics = [{
            "Endpoint": "/clinics/",
            "Method": "GET",
            "Body": None,
            "Descp": "List of all clinics"
         },
         {
            "Endpoint": "/clinics/create",
            "Method": "POST",
            "Body": {
                "name" : "",
            },
            "Descp": "Creating a new clinic"
         },
        {
            "Endpoint": "/clinics/id",
            "Method": "GET",
            "Body": None,
            "Descp": "Viewing all details about a given clinic"
         },
        {
            "Endpoint": "/clinics/id/delete",
            "Method": "DELETE",
            "Body": None,
            "Descp": "Deletes currently selected clinic from the database"
         },
        {
            "Endpoint": "/clinics/id/update",
            "Method": "PUT",
            "Body": {
                "name":""
            },
            "Descp": "Updates information of currently selected clinic"
         }
    ]
    
    accounts = [{
                "Endpoint": "/accounts/",
                "Method": "GET",
                "Body": None,
                "Descp": "List of all accounts credentials (login, password, email)"
            },
            {
                "Endpoint": "/accounts/create",
                "Method": "POST",
                "Body": {
                    "login":"",
                    "password":"",
                    "email":"",
                    "name" : "",
                    "surname": "",
                    "title": ""
                },
                "Descp": "Creating a new account"
            },
            {
                "Endpoint": "/accounts/id",
                "Method": "GET",
                "Body": None,
                "Descp": "Viewing all details about a given account"
            },
            {
                "Endpoint": "/accounts/id/delete",
                "Method": "DELETE",
                "Body": None,
                "Descp": "Deletes currently selected account from the database"
            },
            {
                "Endpoint": "/accounts/id/update",
                "Method": "PUT",
                "Body": {
                    "login":"",
                    "password":"",
                    "email":"",
                    "name":"",
                    "surname":"",
                    "title":""
                },
                "Descp": "Changes information about an account"
            },
    ]

    appointments = [{
            "Endpoint": "/appointments/",
            "Method": "GET",
            "Body": None,
            "Descp": "List of all appointments"
         },
         {
            "Endpoint": "/appointments/create",
            "Method": "POST",
            "Body": {
                "date" : "",
                "patient": "pesel",
                "clinic": "id",
            },
            "Descp": "Creating a new appointment"
         },
        {
            "Endpoint": "/appointments/id",
            "Method": "GET",
            "Body": None,
            "Descp": "Viewing all details about a given appointment"
         },
        {
            "Endpoint": "/appointments/id/delete",
            "Method": "DELETE",
            "Body": None,
            "Descp": "Deletes currently selected appointment from the database"
         },
        {
            "Endpoint": "/appointments/id/update",
            "Method": "PUT",
            "Body": {
                "date":""
            },
            "Descp": "Placeholder, not used for now"
         }
    ]

    routes = [patients, clinics, accounts, appointments]
    return Response(routes)