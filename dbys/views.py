from django.shortcuts import render
from django.http import HttpResponse
from .models import User

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