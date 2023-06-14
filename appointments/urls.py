# File: urls.py
# Description: Modified for the specific application "panda/appointments"
# Author: Chris Knowles
# Date: Jun 2023


from django.urls import path
from . import views


urlpatterns = [
    path("create-patient/<str:data>/", views.create_patient, name="create-patient"),
    path("retrieve-patient/<str:pk>/", views.retrieve_patient, name="retrieve-patient"),
    path("update-patient/<str:data>/", views.update_patient, name="update-patient"),
    path("delete-patient/<str:pk>/", views.delete_patient, name="delete-patient"),
    path("create-appointment/<str:data>/", views.create_appointment, name="create-appointment"),
    path("retrieve-appointment/<str:pk>/", views.retrieve_appointment, name="retrieve-appointment"),
    path("update-appointment/<str:data>/", views.update_appointment, name="update-appointment"),
    path("delete-appointment/<str:pk>/", views.delete_appointment, name="delete-appointment"),
]




