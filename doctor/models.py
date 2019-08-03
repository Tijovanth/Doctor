from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.ForeignKey(User)
    age = models.IntegerField()
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username



class DoctorProfileInfos(models.Model):
    doctor = models.ForeignKey(User)
    age = models.PositiveIntegerField()
    description = models.TextField()
    workinglocation = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    certificate = models.ImageField(upload_to='certificate_pics',blank=True)
    FILTER_CHOICES = [
        ('General', 'General'),
        ('Orthologist', 'Orthologist'),
        ('Cardiologist', 'Cardiologist'),
        ('Ent', 'Ent'),
        ('Gastrologist', 'Gastrologist'),
    ]
    specialist = models.CharField(max_length=200,choices=FILTER_CHOICES,)

    def __str__(self):
        return self.doctor.username


class Location(models.Model):
    LocationName = models.CharField(max_length=200)
    LocationAddress = models.TextField(max_length=500)
    TimingFrom = models.TimeField()
    TimingTo = models.TimeField()
    slot = models.PositiveIntegerField()
    Doctor = models.ForeignKey(DoctorProfileInfos)
    Avail=[
    ('1','All days'),
    ('0','Mon-Fri'),
    ]
    Availability=models.CharField(max_length=200,choices=Avail)

    def __str__(self):
        return self.LocationAddress

    def __str__(self):
        return self.Doctor.doctor.username

class Appoinment(models.Model):
    Doctor = models.ForeignKey(DoctorProfileInfos)
    Loc = models.ForeignKey(Location)
    User = models.ForeignKey(UserProfileInfo)
    Slot_No = models.IntegerField(default = 1)
    Date = models.DateField()
    Reason_to_visit = models.TextField(max_length = 1000)

    def __str__(self):
        return self.User.user.username
