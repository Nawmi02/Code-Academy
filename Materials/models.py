from django.db import models
from django.contrib.auth.models import User

class Semester(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Book(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)         
    subject_code = models.CharField(max_length=50)      
    file = models.FileField(upload_to='materials/books/')
    cover_image = models.ImageField(upload_to='materials/book_covers/', null=True, blank=True)

    def __str__(self):
        return self.title

class Note(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=50)
    file = models.FileField(upload_to='materials/notes/')

    def __str__(self):
        return self.title

class Code(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    code_text = models.TextField()

    def __str__(self):
        return self.title

class PreviousQuestion(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='materials/previous_questions/')

    def __str__(self):
        return self.title
