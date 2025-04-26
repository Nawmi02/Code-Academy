from django.shortcuts import render
from .models import Guideline

<<<<<<< Updated upstream
def show_guidelines(request):
    all_guidelines = Guideline.objects.all()
    return render(request, 'guidelines.html', {'guidelines': all_guidelines})
=======
def guideline(request):
    return render(request, 'guidelines.html') 


>>>>>>> Stashed changes
