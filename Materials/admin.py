from django.contrib import admin
from .models import Semester, Book, Note, Code, PreviousQuestion

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'semester')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'semester')

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'semester')

@admin.register(PreviousQuestion)
class PreviousQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'semester')
