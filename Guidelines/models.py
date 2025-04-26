from django.db import models

class Guideline(models.Model):
    topic = models.CharField(max_length=200, null=True, blank=True)
    video_link = models.URLField(max_length=500, null=True, blank=True) 
    description = models.TextField(null=True, blank=True)  

    def _str_(self):
        return self.topic