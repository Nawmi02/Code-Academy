from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')
