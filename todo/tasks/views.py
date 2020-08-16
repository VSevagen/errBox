from django.shortcuts import render, redirect, reverse, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer
import hashlib

# Create your views here.

def tasks(request):
    print("Do something here")
    return render(request, "tasks.html")

def token(request):
    with open('password.txt', 'wb') as f:
        p = 'new password'
        f.write(hashlib.sha512(p.encode('utf-8')).digest()) 
    print("Password has been generated !")    
    return render(request, "token.html")

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    

