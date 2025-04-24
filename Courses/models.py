from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta  

class Course(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    academy = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='courses/', null=True, blank=True)  
    registration_link = models.URLField(max_length=500, null=True, blank=True)
    registration_deadline = models.DateTimeField(auto_now_add=True)
    course_type = models.CharField(max_length=100, null=True, blank=True)
    course_days = models.DurationField(default=timedelta(hours=1))

    def __str__(self):
        return self.name