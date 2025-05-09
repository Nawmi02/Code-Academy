from django.shortcuts import render
from .models import Course
from django.db.models import Q  

def course_list(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(
            Q(name__icontains=query) | Q(course_topic__icontains=query)
        )
    else:
        courses = Course.objects.all()

    return render(request, 'courses.html', {
        'courses': courses,
        'query': query
    })
