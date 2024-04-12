from django.shortcuts import render
import hashlib as hash
from django.http import HttpResponse
import environ
import json
from django.views.decorators.csrf import csrf_exempt

#from siteDjango.login.models import login




env=environ.Env()
environ.Env.read_env()

# Create your views here.
#@api_view(['GET'])
def index(request):
    pwd2 = request.GET.get('request', '')
    pwd = "test"
    salt = env("LOGIN_SALT")
    encoded = hash.sha256((pwd+salt).encode("utf-8")).hexdigest()
    return HttpResponse((hash.sha256((pwd2+salt).encode("utf-8")).hexdigest())== encoded)

#@api_view(['POST'])
#----- DELETE THIS ASAP -----
@csrf_exempt
#----------------------------
def register(request):
    json_data=(json.loads(request.body))
    #exists = login.objects.get(name=json_data['nickname'], email=json_data['email'])

    return HttpResponse(json_data['param'])