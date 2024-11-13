from django.shortcuts import render
from app.forms import *
# Create your views here.
def display(request):
    MF = userform()
    FM = profileform()
    d = {'MF':MF,'FM':FM}
    return render(request,'display.html',d)