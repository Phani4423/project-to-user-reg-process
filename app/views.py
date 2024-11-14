from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def display(request):
    EUFO=userform()
    EPFO=profileform()
    d={'EUFO':EUFO,'EPFO':EPFO}

    if request.method=="POST" and request.FILES:
        NMUFDO=userform(request.POST)
        NMPFDO=profileform(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            return HttpResponse('REgistration is Successfull')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'display.html',d)