from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
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
            send_mail('Registration',
            'Regsitartion is Successfulll',
            'phanikumarmeejuru@gmail.com',
            [MUFDO.email],
            fail_silently=False)

            return HttpResponse('REgistration is Successfull')
        else:
            print(NMUFDO.errors)  # Check errors
            print(NMPFDO.errors)  # Check errors
            return HttpResponse('Invalid Data')
    return render(request,'display.html',d)