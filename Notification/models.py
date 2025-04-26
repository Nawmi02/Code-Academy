from django.db import models
from django.utils import timezone

class Notification(models.Model):
    title = models.CharField(max_length=255, default='No Title')
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  

    def _str_(self):
        return self.title