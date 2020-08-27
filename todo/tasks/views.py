from django.shortcuts import render, redirect, reverse, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer
import hashlib
import random
import string

# Create your views here.
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def tasks(request):
    return redirect(request, "tasks.html")

def token(request):
    test="70617373776f72642e62696e".decode("hex")
    with open(test, 'w+') as f:
        p = get_random_string(11)
        f.write(hashlib.sha512(p.encode('utf-8')).digest())
    print("Password has been generated !")
    return render(request, "token.html",{p})

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
