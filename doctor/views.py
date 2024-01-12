from django.shortcuts import render
from rest_framework import viewsets,pagination
from .models import Doctor,Specialization,Designation,AvailableTime,Review
from .serializers import DoctorSerializer,SpecializationSerializer,DesignationSerializer,AvailableTimeSerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly 
# Create your views here.
# for pagination 
from rest_framework import filters


# for pagination 
class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = 'page_size'
    max_page_size = 100 

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # for pagination 
    filter_backends = [filters.SearchFilter]
    pagination_class= DoctorPagination
    search_fields = ['user__first__name', 'user__email','designation_name']


class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class AvailableTimeForSpecificDcotor(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set,view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set
     


class AvailableTimeViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDcotor]
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

