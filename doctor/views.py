from django.shortcuts import render,redirect
from doctor.forms import UserForm,UserProfileInfoForm,UserLoginForm,DoctorProfileInfoForm,DoctorLoginForm,DoctorUpdateForm,LocationRegisterForm,BookAppoinmentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from doctor.models import DoctorProfileInfos,UserProfileInfo,Appoinment,Location
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from django.utils import timezone
import datetime
from doctor import models
# Create your views here.
def home(request):
    if request.session.has_key('username'):
        username = request.session['username']
        who = False
        doc = False
        doc_or_not = DoctorProfileInfos.objects.all()
        for j in doc_or_not:
            if j.doctor.username == username:
                doc = True
        print(doc)
        if doc == True:
            doctor_details= DoctorProfileInfos.objects.filter(specialist="Orthologist").filter(doctor__username=username)
            #print(doctor_details, end='\n')
            if doctor_details:
                location=[]
                details=[]
                #print(doctor_details)
                for i  in doctor_details:
                    details.append(i.doctor.username)
                    details.append(i.specialist)
                    details.append(i.profile_pic)
                    details.append(i.certificate)
                    details.append(i.id)
                    details.append(i.age)
                    details.append(i.description)
                    break
                location = Location.objects.filter(Doctor__doctor__username=username)
                return render(request,'doctor/DoctorDetail.html',{ 'docName':username, 'who':True,'location':location,'details':details})
            doctor_details = DoctorProfileInfos.objects.filter(specialist="Cardiologist").filter(doctor__username=username)
            if doctor_details:
                location=[]
                details=[]
                #print(doctor_details)
                for i  in doctor_details:
                    details.append(i.doctor.username)
                    details.append(i.specialist)
                    details.append(i.profile_pic)
                    details.append(i.certificate)
                    details.append(i.id)
                    details.append(i.age)
                    details.append(i.description)
                    break
                location = Location.objects.filter(Doctor__doctor__username=username)
                return render(request,'doctor/DoctorDetail.html',{ 'docName':username, 'who':True,'location':location,'details':details})
            doctor_details = DoctorProfileInfos.objects.filter(specialist="Gastrologist").filter(doctor__username=username)
            if doctor_details:
                location=[]
                details=[]
                #print(doctor_details)
                for i  in doctor_details:
                    details.append(i.doctor.username)
                    details.append(i.specialist)
                    details.append(i.profile_pic)
                    details.append(i.certificate)
                    details.append(i.id)
                    details.append(i.age)
                    details.append(i.description)
                    break
                location = Location.objects.filter(Doctor__doctor__username=username)
                return render(request,'doctor/DoctorDetail.html',{ 'docName':username, 'who':True,'location':location,'details':details})
            doctor_details = DoctorProfileInfos.objects.filter(specialist="General").filter(doctor__username=username)
            if doctor_details:
                location=[]
                details=[]
                #print(doctor_details)
                for i  in doctor_details:
                    details.append(i.doctor.username)
                    details.append(i.specialist)
                    details.append(i.profile_pic)
                    details.append(i.certificate)
                    details.append(i.id)
                    details.append(i.age)
                    details.append(i.description)
                    break
                location = Location.objects.filter(Doctor__doctor__username=username)
                return render(request,'doctor/DoctorDetail.html',{ 'docName':username, 'who':True,'location':location,'details':details})
            doctor_details = DoctorProfileInfos.objects.filter(specialist="Ent").filter(doctor__username=username)
            if doctor_details:
                location=[]
                details=[]
                #print(doctor_details)
                for i  in doctor_details:
                    details.append(i.doctor.username)
                    details.append(i.specialist)
                    details.append(i.profile_pic)
                    details.append(i.certificate)
                    details.append(i.id)
                    details.append(i.age)
                    details.append(i.description)
                    break
                location = Location.objects.filter(Doctor__doctor__username=username)
                return render(request,'doctor/DoctorDetail.html',{ 'docName':username, 'who':True,'location':location,'details':details})
        else:
            user1 = UserProfileInfo.objects.get(user__username = username)
            return render(request,'doctor/Catagories.html',{'user1':user1})
    else:
        return render(request,'doctor/home.html')

@login_required
def Catagories(request):
    return render(request,'doctor/Catagories.html')

@login_required
def UserLogout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('home'))

def UserRegistration(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'doctor/UserRegistration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def UserLogin(request):

    if request.method == 'POST':
        # First get the username and password supplied
        user_loginform = UserLoginForm(data=request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                request.session['username'] = username
                # Send the user back to some page.
                # In this case their homepage.
                # return render(request,'doctor/UserLogin.html',{'registered':registered})
                # return render(request,'doctor/intermediate.html',{})
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        userlogin_form = UserLoginForm()
        return render(request, 'doctor/UserLogin.html', {'userlogin_form':userlogin_form})

def DoctorRegistration(request):
    registered = False


    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        doctor_form = UserForm(data=request.POST)
        doctorprofile_form = DoctorProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if doctor_form.is_valid() and doctorprofile_form.is_valid():

            # Save User Form to Database
            doctor = doctor_form.save()
            doctor.set_password(doctor.password)
            doctor.save()
            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            doctorprofile = doctorprofile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            doctorprofile.doctor = doctor

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                doctorprofile.profile_pic = request.FILES['profile_pic']

            if 'certificate' in request.FILES:
                print('found it')
                doctorprofile.certificate = request.FILES['certificate']

            # Now save model
            doctorprofile.save()

            # Registration Successful!
            registered = True


        else:
            # One of the forms was invalid if this else gets called.
            print(doctor_form.errors,doctorprofile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        doctor_form = UserForm()
        doctorprofile_form = DoctorProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'doctor/DoctorRegistration.html',
                          {'doctor_form':doctor_form,
                           'doctorprofile_form':doctorprofile_form,
                           'registered':registered})

def DoctorLogin(request):
    registered = False
    if request.method == 'POST':
        # First get the username and password supplied
        doctor_loginform = DoctorLoginForm(data=request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        doctor = authenticate(username=username, password=password)

        # If we have a user
        if doctor:
            #Check it the account is active
            if doctor.is_active:
                # Log the user in.
                login(request,doctor)
                request.session['username'] = username
                # Send the user back to some page.
                # In this case their homepage.
                # doctor_specialist = User.objects.get(username=username)
                # return render(request,'doctor/inter.html',{'doctor_specialist':doctor_specialist})
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        doctorlogin_form = DoctorLoginForm()
        return render(request, 'doctor/DoctorLogin.html', {'doctorlogin_form':doctorlogin_form,'registered':registered})


@login_required
def cardio(request):
    a = []
    cardionames = []
    cardio = DoctorProfileInfos.objects.filter(specialist="Cardiologist")
    for i in cardio:
        a.append(i.doctor.username)
    cardionames = list(dict.fromkeys(a))
    username = request.session['username']
    user1 = UserProfileInfo.objects.get(user__username = username)
    return render(request,'doctor/Cardiologist.html',{'cardionames':cardionames,'user1':user1})


@login_required
def ortho(request):
    a = []
    orthonames = []
    ortho = DoctorProfileInfos.objects.filter(specialist="Orthologist")
    for i in ortho:
        a.append(i.doctor.username)
    orthonames = list(dict.fromkeys(a))
    username = request.session['username']
    user1 = UserProfileInfo.objects.get(user__username = username)
    return render(request,'doctor/Orthologist.html',{'orthonames':orthonames,'user1':user1})


@login_required
def general(request):
    a = []
    generalnames = []
    general = DoctorProfileInfos.objects.filter(specialist="General")
    for i in general:
        a.append(i.doctor.username)
    generalnames = list(dict.fromkeys(a))
    username = request.session['username']
    user1 = UserProfileInfo.objects.get(user__username = username)
    return render(request,'doctor/General.html',{'generalnames':generalnames,'user1':user1})

@login_required
def gastro(request):
    a = []
    gastronames = []
    gastro = DoctorProfileInfos.objects.filter(specialist="Gastrologist")
    for i in gastro:
        a.append(i.doctor.username)
    gastronames = list(dict.fromkeys(a))
    username = request.session['username']
    user1 = UserProfileInfo.objects.get(user__username = username)
    return render(request,'doctor/Gastrologist.html',{'gastronames':gastronames,'user1':user1})

@login_required
def ent(request):
    a = []
    entnames = []
    ent = DoctorProfileInfos.objects.filter(specialist="Ent")
    for i in ent:
        a.append(i.doctor.username)
    entnames = list(dict.fromkeys(a))
    username = request.session['username']
    user1 = UserProfileInfo.objects.get(user__username = username)
    return render(request,'doctor/ENT.html',{'entnames':entnames,'user1':user1})


@login_required
def DoctorDetails(request, name,category):
    print("view entered")
    docName = name
    docCategory= category
    username = request.session['username']
    # print(docName, category)
    # print(name)
    doctor_details= DoctorProfileInfos.objects.filter(specialist=docCategory).filter(doctor__username=docName)
    if doctor_details:
        location=[]
        details=[]
        for i  in doctor_details:
            details.append(i.doctor.username)
            details.append(i.specialist)
            details.append(i.profile_pic)
            details.append(i.certificate)
            details.append(i.id)
            details.append(i.age)
            details.append(i.description)
            break
        location = Location.objects.filter(Doctor__doctor__username=docName)
        user1 = UserProfileInfo.objects.get(user__username = username)
    return render(request,'doctor/DoctorDetail.html',{ 'docName':username,'location':location,'details':details,'who':False,'user1':user1})


def DoctorDetailsUpdate(request,id):
    pk = id
    print(pk)
    if request.method == 'POST':
        update_form = DoctorUpdateForm(data=request.POST)
        Availability = request.POST.get('Availability')
        TimingFrom = request.POST.get('TimingFrom')
        TimingTo = request.POST.get('TimingTo')
        slot =  request.POST.get('slot')
        hospitaldetails = Location.objects.get(pk=pk)
        hospitaldetails.Availability =  Availability
        hospitaldetails.TimingFrom = TimingFrom
        hospitaldetails.TimingTo = TimingTo
        hospitaldetails.slot = slot
        hospitaldetails.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        hospitaldetails = Location.objects.get(pk=pk)
        update_form = DoctorUpdateForm(instance=hospitaldetails)
        return render(request,'doctor/DoctorUpdate.html',{'update_form':update_form})



@login_required
def LocationRegister(request,id):
    if  request.method == 'POST':
        location_form = LocationRegisterForm(data=request.POST)
        if location_form.is_valid():
            locationform =  location_form.save(commit=False)
            doctor= DoctorProfileInfos.objects.get(pk=id)
            locationform.Doctor = doctor
            locationform.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print(location_form.errors)
    else:
        location_form = LocationRegisterForm()
        return render(request,'doctor/LocationRegister.html',{'location_form':location_form})

@login_required
def DoctorDelete(request,id):
    return render(request,'doctor/DoctorDelete.html',{'id':id})

@login_required
def which(request,choice,id):
    if choice == "Yes":
        Location.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse_lazy('home'))
    else:
        return HttpResponseRedirect(reverse('home'))

@login_required
def BookAppoinment(request,id):
    if request.method == 'POST':
        book = Appoinment()
        reason = request.POST.get('Reason_to_visit')
        date = request.POST.get('date')
        avail = Location.objects.get(pk=id)
        book.Doctor = avail.Doctor
        book.Loc = avail
        username = request.session['username']
        userobj = UserProfileInfo.objects.get(user__username = username)
        book.User = userobj
        TotalSlot = avail.slot
        BookedSlot = Appoinment.objects.filter(Date=date).filter(Loc__id = id)
        count = 0
        for i in BookedSlot:
            count = count + 1
        RemainingSlot = TotalSlot - count
        TokenNum = TotalSlot - RemainingSlot
        TokenNum = TokenNum + 1
        book.Slot_No = TokenNum
        book.Reason_to_visit = reason
        book.Date = date
        book.save()
        return render(request,'doctor/AppointmentSummary.html',{'book':book})
    else:
        book = BookAppoinmentForm()
        avail = Location.objects.get(pk=id)
        avail_2 = avail.Availability
        TotalSlot = avail.slot
        NoSlotes = []
        RemainingSlot=[]
        dateRange = []
        today = timezone.now()
        if(avail_2 == '1'):
            for i in range(1,8):
                BookedSlot = Appoinment.objects.filter(Date=(today+datetime.timedelta(days = i)).date()).filter(Loc__id = id)
                count = 0
                for j in BookedSlot:
                    count = count + 1
                Remainingchecking = TotalSlot - count
                if Remainingchecking > 0:
                    RemainingSlot.append(TotalSlot - count)
                    temp = today+datetime.timedelta(days = i)
                    dateRange.append(temp.date())
                else:
                    temp = today+datetime.timedelta(days = i)
                    NoSlotes.append(temp.date())

        else:
            for i in range(1,10):
                temp = today+datetime.timedelta(days = i)
                if(temp.isoweekday() == 6 or temp.isoweekday() == 7):
                    continue
                BookedSlot = Appoinment.objects.filter(Date=temp.date()).filter(Loc__id = id)
                count = 0
                for j in BookedSlot:
                    count = count + 1
                Remainingchecking = TotalSlot - count
                if Remainingchecking > 0:
                    RemainingSlot.append(TotalSlot - count)
                    dateRange.append(temp.date())
                else:
                    NoSlotes.append(temp.date())
        username1 = request.session['username']
        user1 = UserProfileInfo.objects.get(user__username = username1)
        return render(request,'doctor/BookAppointment.html',{'dateRange':dateRange,'book':book,'RemainingSlot':RemainingSlot,'NoSlotes':NoSlotes,'user1':user1})

@login_required
def YourAppointment(request):
    username = request.session['username']
    today = timezone.now()
    today = today.date()
    Appointment = Appoinment.objects.filter(User__user__username=username , Date__gt = today)
    Appointment_1 = Appoinment.objects.filter(User__user__username=username , Date__lt = today)
    Appointment_2 = Appoinment.objects.filter(User__user__username=username , Date = today)
    print(today)
    username1 = request.session['username']
    user1 = UserProfileInfo.objects.get(user__username = username1)
    return render(request,'doctor/YourAppointment.html',{'Appointment':Appointment,'today':today,'Appointment_1':Appointment_1,'Appointment_2':Appointment_2,'user1':user1})


@login_required
def AppointmentDelete(request,id):
    deleting_person_obj = Appoinment.objects.get(id=id)
    deleted_person_num = deleting_person_obj.Slot_No
    date = deleting_person_obj.Date
    location = deleting_person_obj.Loc.LocationName
    checkingobj = Appoinment.objects.filter(Loc__LocationName = location, Date=date)
    for i in checkingobj:
        some = i.Slot_No
        if i.Slot_No > deleted_person_num:
            i.Slot_No = some - 1
            i.save()
    Appoinment.objects.get(id=id).delete()
    return render(request,'doctor/AppointmentDelete.html',{'id':id})
