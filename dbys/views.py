from django.shortcuts import render
from django.http import HttpResponse

def programs(request):
    programs = ["Intrdocutrdion to Coding", "Introduction to Python", "ACSL", "USACO", "AP CSA"]
    context = {'programs':programs};
    return render(request, "dbys/programs.html", context)

# Create your views here.
def hello(request):
    
    context = {'name':'Yeongsu'} #/prop
    return render(request, "dbys/index.html", context)
