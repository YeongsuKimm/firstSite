from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import Argon2PasswordHasher

def programs(request):
    programs = ["Intrdocutrdion to Coding", "Introduction to Python", "ACSL", "USACO", "AP CSA"]
    context = {'programs':programs};
    return render(request, "dbys/programs.html", context)

# Create your views here.
def hello(request):
    
    context = {'name':'Yeongsu'} #/prop
    return render(request, "dbys/index.html", context)

def show_users(request):
    user = User.objects.filter()
    print(user)
    
    context ={
        'users':user
    }
    
    
    return render(request, "dbys/show_user.html", context)

def show_courses(request):
    courses = ["Coding_Chanmin_Kwon", "	Coding_Yeongsu_Kim"]
    courses = User.objects.filter()
    context = { 
        'courses':courses  
    }
    return render(request, "dbys/courses.html", context)
#/login
def login(request):
    if request.method =="GET":
        return render(request, 'dbys/login.html', {})
    if request.method=="POST":
        data = request.POST
        id = data.get('uid')
        pw = data.get('password')
        user = User.objects.filter(username=id);
        if len(user)>0:
            password = User.objects.filter(username=id)[0].password
            if password == pw:
                messages.info(request, "Welcome!")
            else:
                messages.warning(request, "Your password is incorrect")
            return render(request, 'dbys/login.html', {})
        else:
            messages.info(request, "Your id doesn't exist")
            return render(request, 'dbys/login.html', {})

def register(request):
    if request.method == "GET":
        return render(request, 'dbys/register.html', {})
    if request.method == "POST":
        data = request.POST
        id = data.get('uid')
        pw = data.get('password')
        fname = data.get('first-name')
        lname = data.get('last-name')
        ad = data.get('address')
        user = User.objects.filter(username=id)
        if len(user)>0:
            messages.info(request, "User already exists")
            return render(request, 'dbys/register.html', {})
        else:
            User.objects.create(
                username = id,
                password = pw,
                first_name = fname,
                last_name = lname,
                address = ad
            )
            messages.info(request, "User successfully creted")
            return render(request, 'dbys/register.html', {})