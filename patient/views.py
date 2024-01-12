
from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Patient
from django.contrib.auth.models import User
from .serializers import PatientSerializer,RegistrationSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Create your views here.

class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class RegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            print(user.email)

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/active/{uid}/{token}"

            email_subject = 'Confirm you email'
            email_body = render_to_string('confirm_email.html',{
                'confirm_link':confirm_link,
            })
            to_email = user.email
            send_email = EmailMultiAlternatives(email_subject,'',to=[to_email])
            send_email.attach_alternative(email_body,'text/html')
            send_email.send()

            return Response(serializer.data)
        return Response(serializer.errors)
    
def activate(request,uid64,token):
    try:

        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    
class LoginAPIView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data= self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username,password=password)
            if user:
                token,_ = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id})
            else:
                return Response({'error':'Invalid Credential'})
        return Response(serializer.errors)


class LogoutAPIView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')