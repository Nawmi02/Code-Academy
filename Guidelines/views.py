from django.shortcuts import render
from .models import Guideline

def show_guidelines(request):
    all_guidelines = Guideline.objects.all()
    return render(request, 'guidelines.html', {'guidelines': all_guidelines})