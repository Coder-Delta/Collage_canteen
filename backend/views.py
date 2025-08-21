# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
     return render(request, "home.html")

def login_page(request):
     return render(request, "login.html")

def welcome(request):
     return render(request, "welcome.html")