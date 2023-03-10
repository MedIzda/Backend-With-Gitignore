from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    path('patients/', views.getPatients),
    path('patients/add/', views.newPatient),
    path('patients/<str:pk>/update/', views.updatePatient),
    path('patients/<str:pk>/delete/', views.removePatient),
    path('patients/<str:pk>/', views.getPatient),

    path('clinics/', views.getClinics),
    path('clinics/add/', views.newClinic),
    path('clinics/<str:pk>/update/', views.updateClinic),
    path('clinics/<str:pk>/delete/', views.removeClinic),
    path('clinics/<str:pk>/', views.getClinic),

    path('accounts/', views.getClinics),
    path('accounts/add/', views.newClinic),
    path('accounts/<str:pk>/update/', views.updateClinic),
    path('accounts/<str:pk>/delete/', views.removeClinic),
    path('accounts/<str:pk>/', views.getClinic),
]