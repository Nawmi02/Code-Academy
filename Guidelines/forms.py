from django.forms import ModelForm
from .model import *
class GuidelineForm(ModelForm):
    class Meta:
        model = MethodGuidelineForm
        fields = '__all__'