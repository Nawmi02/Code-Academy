from django.forms import ModelForm
from .models import Guideline

class GuidelineForm(ModelForm):
    class Meta:
        model = Guideline  
        fields = '__all__'
