from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import *


def launch(request):
    return render(request, 'app/launch.html')


def home(request):
    notice = Notice.objects.all()
    attendance = Attendance.objects.all()
    marks = Marks.objects.all()

    context = {
        'notice': notice,
        'marks': marks,
        'attendance': attendance,
    }
    return render(request, 'app/home.html', context)


def addAttendance(request):
    if request.user.is_authenticated:
        form = addAttendanceform()
        if(request.method == 'POST'):
            form = addAttendanceform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'app/addAttendance.html', context)
    else:
        return redirect('home')


def addMarks(request):
    if request.user.is_authenticated:
        form = addMarksform()
        if(request.method == 'POST'):
            form = addMarksform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'app/addMarks.html', context)
    else:
        return redirect('home')


def addNotice(request):
    if request.user.is_authenticated:
        form = addNoticeform()
        if(request.method == 'POST'):
            form = addNoticeform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'app/addNotice.html', context)
    else:
        return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            fname = request.POST['fname']
            lname = request.POST['lname']

            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            return redirect('login')

       
        return render(request, 'app/register.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('loginusername')
            password = request.POST.get('loginpassword')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        context = {}
        return render(request, 'app/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')
