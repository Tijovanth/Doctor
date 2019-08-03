from django.conf.urls import url
from doctor import views

app_name = 'doctor'

urlpatterns = [
   url(r'^UserLogin/',views.UserLogin,name='UserLogin'),
   url(r'^UserRegistration/',views.UserRegistration,name='UserRegistration'),
   url(r'^DoctorRegistration/',views.DoctorRegistration,name='DoctorRegistration'),
   url(r'^DoctorLogin/',views.DoctorLogin,name='DoctorLogin'),
   url(r'^Catagories/',views.Catagories,name='Catagories'),
   url(r'^Cardiologist/(?P<id>\d+)',views.BookAppoinment,name='BookAppoinment'),
   url(r'^Cardiologist/(?P<name>\D+)',views.DoctorDetails, {'category':'Cardiologist'},name='Detail'),
   url(r'^Cardiologist/',views.cardio,name='Cardiologist'),
   url(r'^Gastrologist/(?P<name>\D+)',views.DoctorDetails, {'category':'Gastrologist'},name='Detail'),
   url(r'^Gastrologist/',views.gastro,name='Gastrologist'),
   url(r'^Orthologist/(?P<id>\d+)',views.BookAppoinment,name='BookAppoinment'),
   url(r'^Orthologist/(?P<name>\D+)',views.DoctorDetails, {'category':'Orthologist'},name='Detail'),
   url(r'^Orthologist/',views.ortho,name='Orthologist'),
   url(r'^General/(?P<id>\d+)',views.BookAppoinment,name='BookAppoinment'),
   url(r'^General/(?P<name>\D+)',views.DoctorDetails, {'category':'General'},name='Detail'),
   url(r'^General/',views.general,name='General'),
   url(r'^ENT/(?P<id>\d+)',views.BookAppoinment,name='BookAppoinment'),
   url(r'^ENT/(?P<name>\D+)',views.DoctorDetails, {'category':'Ent'},name='Detail'),
   url(r'^ENT/',views.ent,name='Ent'),
   url(r'^(?P<id>\d+)/locationregister',views.LocationRegister,name='LocationRegister'),
   url(r'^YourAppointment',views.YourAppointment,name='YourAppointment'),
   url(r'^(?P<id>\d+)',views.AppointmentDelete,name='AppointmentDelete'),
]
