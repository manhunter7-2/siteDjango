from django.shortcuts import render
import hashlib as hash
from django.http import HttpResponse
import environ
import json
from django.views.decorators.csrf import csrf_exempt
from login.models import Login

#from siteDjango.login.models import login



env=environ.Env()
environ.Env.read_env()

# Create your views here.
#@api_view(['GET'])
def index(request):
    pwd = request.GET.get('request', '')
    salt = env("LOGIN_SALT")
    return HttpResponse(hash.sha256((pwd+salt).encode("utf-8")).hexdigest())

def encodePwd(pwd):
    pwd=str(pwd)
    salt = env("LOGIN_SALT")
    return hash.sha256((pwd+salt).encode("utf-8")).hexdigest()

#@api_view(['POST'])
#----- DELETE THIS ASAP -----
@csrf_exempt
#----------------------------
def register(request):
    json_data=(json.loads(request.body))
    login = Login
    login.pwd = encodePwd(str(json_data['pwd']))
    print(login.pwd)
    if ((login.objects.filter(nickname=json_data['nickname'], email=json_data['email'])).count() == 0):
        exists = "No"
    else:
        exists = "Yes"
    return HttpResponse(json_data['param']+" "+exists+"\n"+str(login.pwd))