from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the task management system")

def contact(request):
    return HttpResponse("<h1 style='color: red'>This is contact</h1>")

def show_task(request):
    return HttpResponse("this is our task page")
    # work with database
    # transform data 
    # data pass
    # Http response / Json response

