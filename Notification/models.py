from django.db import models
from django.contrib.auth.models import user

# Create your models here.
class Notification(models.model):
    name = models.Foreignkey(Course,on_delete = models.CASCADE)
    type = models.Charfield(max_length = 100,null = True,blank = True)
    time = models.TimeField(null = True, blank = True)
    message = models.Textfield(max_length = 500,null = True,blank = True)


    def __str__(self):
        return self.name