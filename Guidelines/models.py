from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Guigiline(models.Model):
    name = models.Foreignkey(Course,on_delete = models.CASCADE)
    topic = models.Charfield(max_length = 100,null = True, blank = True)
    text = models.Textfield(max_length = 100,null = True, blank = True)
    time = models.TimeField (null = True, blank = True)


    def __str__(self):
        return self.name
     

