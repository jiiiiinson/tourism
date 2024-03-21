from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Trip

# Create your views here.
def travel(request):
    obj = Trip.objects.all()
    return render(request, "index.html",{'result':obj})
