from django.contrib import admin
from .models import AvailableTime, Designation, Doctor, Review, Specialization
# Register your models here.
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
admin.site.register(Designation,DesignationAdmin)
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(Review)