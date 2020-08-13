from django.shortcuts import render, redirect, reverse, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from .models import TaskForm, Task, UsernameForm, Username
from django.template import RequestContext

# Create your views here.

def tasks(request):
    print("Do something here")
    return render(request, "tasks.html")

def token(request):
    print("Press button calls here !!")
    return render(request, "tasks.html")
