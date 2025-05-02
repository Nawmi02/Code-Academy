from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['semester', 'title', 'subject', 'subject_code', 'file']

