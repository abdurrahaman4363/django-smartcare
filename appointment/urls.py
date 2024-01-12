from django.urls import path,include
from rest_framework.routers import DefaultRouter
from contact_us.urls import urlpatterns
from .views import AppointmentViewset

router = DefaultRouter()
router.register('appointment',AppointmentViewset,basename='appointment')

urlpatterns=[
    path('',include(router.urls))
]