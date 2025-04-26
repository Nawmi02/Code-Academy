<<<<<<< Updated upstream
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    # name = models.ForeignKey(Course,on_delete = models.CASCADE) 
    type = models.CharField(max_length = 100,null = True,blank = True)
    time = models.TimeField(null = True, blank = True)
    message = models.TextField(max_length = 500,null = True,blank = True)


    def __str__(self):
        return self.name
=======
>>>>>>> Stashed changes
