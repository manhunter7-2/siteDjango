from django.shortcuts import render
import hashlib as hash
from django.http import HttpResponse

# Create your views here.
#@api_view(['GET'])
def index(request):
    pwd2 = request.GET.get('request', '')
    pwd = "test"
    salt = "Don't trust this sh!t"
    encoded = hash.sha256((pwd+salt).encode("utf-8")).hexdigest()
    return HttpResponse((hash.sha256((pwd2+salt).encode("utf-8")).hexdigest()) == encoded)

# throws error : Strings must be encoded before hashing