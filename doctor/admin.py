from django.contrib import admin
from doctor.models import UserProfileInfo,User,DoctorProfileInfos,Appoinment,Location

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(DoctorProfileInfos)
admin.site.register(Appoinment)
admin.site.register(Location)
