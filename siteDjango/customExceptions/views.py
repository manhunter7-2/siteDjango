from django.shortcuts import render
from customExceptions.models import CustomException as cExept

# Create your views here.
def setExc(excValue):
    exception=cExept
    cExept.exceptionCode=excValue
    if (excValue == 1001):
        cExept.exceptionMessage="Wrong Password, try again"
    elif(excValue == 1002):
        cExept.exceptionMessage="Nickname does not exist"