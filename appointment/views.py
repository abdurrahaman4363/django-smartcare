from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AppointmentSerializer
from .models import Appointment
# Create your views here.

class AppointmentViewset(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class = AppointmentSerializer

    #custom query korar jonno niche functin ta use kore
    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        # patient_id = self.request.query_params['patient_id']
        print(self.request)
        # print(self.request.query_params)
        # print(patient_id)
        if patient_id:
            queryset = queryset.filter(patient_id = patient_id)
        return queryset