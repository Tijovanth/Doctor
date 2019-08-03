from django import forms
from django.contrib.auth.models import User
from doctor.models import UserProfileInfo,DoctorProfileInfos,Location,Appoinment
from django.contrib.admin import widgets

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('age','profile_pic')

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')


class DoctorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')



class DoctorProfileInfoForm(forms.ModelForm):

    class Meta():
        model = DoctorProfileInfos
        fields = ('age','description','profile_pic','certificate','specialist')

class DoctorLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')


class DoctorUpdateForm(forms.ModelForm):
    class Meta():
        model = Location
        fields = ('Availability','TimingFrom','TimingTo','slot',)

class LocationRegisterForm(forms.ModelForm):
    
    class Meta():
        model = Location
        fields = ('LocationName','LocationAddress','Availability','TimingFrom','TimingTo','slot',)

class BookAppoinmentForm(forms.ModelForm):
    class Meta():
        model = Appoinment
        fields = ('Date','Reason_to_visit',)
        # Date=[('select1','select 1'),
        #  ('select2','select 2')]
        #
        # like = forms.ChoiceField(choices=Date, widget=forms.RadioSelect)
        # widgets = {
        #     'Date': forms.RadioSelect(attrs={'class': 'RadioSelectclass'}),
        # }
