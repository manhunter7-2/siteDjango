from django.shortcuts import render
import hashlib as hash
from django.http import HttpResponse

# Create your views here.
def index(request):
    salt = "Don't trust this sh!t"
    return HttpResponse(hash.hexdigest(request+salt).toString())