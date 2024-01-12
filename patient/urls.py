from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewset, RegistrationAPIView,activate,LoginAPIView,LogoutAPIView

router = DefaultRouter()
router.register('patient', PatientViewset, basename='patient')

urlpatterns = [
    path('', include(router.urls)),
    path('register/',RegistrationAPIView.as_view() , name='register'),
    path('login/',LoginAPIView.as_view() , name='login'),
    path('logout/',LogoutAPIView.as_view() , name='logout'),
    path('active/<uid64>/<token>/',activate,name='activate')
]