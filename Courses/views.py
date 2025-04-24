from django.shortcuts import render
from .models import *

# Create your views here.
def Course(request):
    course = Course.objects.all()
    context = {'course': course}
    return render('courses.html', context = context)
    

