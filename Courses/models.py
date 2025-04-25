from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    academy = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    
    registration_link = models.URLField(max_length=500, null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)
    course_topic = models.CharField(max_length=100, null=True, blank=True)
    course_duration = models.CharField(max_length=100, null=True, blank=True)
    course_fee = models.CharField(max_length=100, null=True, blank=True)  # ➔ New field added

    def __str__(self):
        return self.name
