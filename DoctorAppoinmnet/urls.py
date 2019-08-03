"""DoctorAppoinmnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from doctor import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^$',views.home,name='home'),
    url(r'^doctor/',include('doctor.urls',namespace='doctor')),
    url(r'^logout/', views.UserLogout, name='logout'),
    url(r'^(?P<id>\d+)/DoctorUpdate',views.DoctorDetailsUpdate,name='DoctorUpdate'),
    url(r'^(?P<id>\d+)/DoctorDelete',views.DoctorDelete,name='DoctorDelete'),
    url(r'^(?P<id>\d+)/Yes',views.which,{'choice':'Yes'},name='Yes'),
    url(r'^(?P<id>\d+)/No',views.which,{'choice':'No'},name='No'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
