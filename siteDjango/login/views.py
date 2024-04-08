from django.shortcuts import render
import hashlib as hash
from django.http import HttpResponse

# Create your views here.
#@api_view(['GET'])
def index(request):
    pwd = "test"
    salt = "Don't trust this sh!t"
    encoded = hash.md5(pwd+salt).encode("utf-8").hexdigest()
    return HttpResponse((hash.md5((str(request)+salt).encode("utf-8")).hexdigest()) == encoded)

# throws error : Strings must be encoded before hashing