from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    path('patients/', views.getPatients),
    path('patients/create/', views.newPatient),
    path('patients/<str:pk>/update/', views.updatePatient),
    path('patients/<str:pk>/delete/', views.removePatient),
    path('patients/<str:pk>/', views.getPatient),

    path('clinics/', views.getClinics),
    path('clinics/create/', views.newClinic),
    path('clinics/<str:pk>/update/', views.updateClinic),
    path('clinics/<str:pk>/delete/', views.removeClinic),
    path('clinics/<str:pk>/', views.getClinic),

    path('accounts/', views.getClinics),
    path('accounts/create/', views.newClinic),
    path('accounts/<str:pk>/update/', views.updateClinic),
    path('accounts/<str:pk>/delete/', views.removeClinic),
    path('accounts/<str:pk>/', views.getClinic),

    path('appointments/', views.getAppointments),
    path('appointments/create/', views.newAppointment),
    path('appointments/<str:pk>/update/', views.updateAppointment),
    path('appointments/<str:pk>/delete/', views.removeAppointment),
    path('appointments/<str:pk>/', views.getAppointments),
    path('appointments/day/<str:pk>/', views.getTodays),
]