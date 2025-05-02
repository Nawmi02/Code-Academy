from django import forms
from .models import Code, Note

class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['semester', 'title', 'description', 'code_text']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['semester', 'title', 'subject', 'subject_code', 'file']

