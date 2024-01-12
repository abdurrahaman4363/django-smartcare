from django.urls import path,include
from rest_framework.routers import DefaultRouter
from contact_us.urls import urlpatterns
from .views import DoctorViewset ,SpecializationViewset,DesignationViewset,AvailableTimeViewset,ReviewViewset

router = DefaultRouter()
router.register('doctor',DoctorViewset,basename='doctor')
router.register('specialization',SpecializationViewset,basename='specialization')
router.register('designation',DesignationViewset,basename='designation')
router.register('availableTime',AvailableTimeViewset,basename='availableTime')
router.register('reviews',ReviewViewset,basename='review')

urlpatterns=[
    path('',include(router.urls)),
]