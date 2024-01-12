from django.contrib import admin
from appointment.models import Appointment
# for mail sending 
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name','patient_name','appointment_types','appointment_status','symptom','time','cancel']

    # obj mani hocche Appointment model er object jeta create hobe value diye submit korar pore eta
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    
    def patient_name(self,obj):
        return obj.patient.user.first_name
    
    def save_model(self,request,obj,form,change):
        obj.save()
        if obj.appointment_status=='Running' and obj.appointment_types =='Online':
            email_subject = 'you Online appointment is Running'
            email_body = render_to_string('admin_email.html',{
                'user':obj.patient.user,
                'doctor':obj.doctor
            })
            to_email = obj.patient.user.email
            send_email = EmailMultiAlternatives(email_subject,'',to=[to_email])
            send_email.attach_alternative(email_body,'text/html')
            send_email.send()

admin.site.register(Appointment,AppointmentAdmin)