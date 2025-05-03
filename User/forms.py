from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

# User Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100)
    semester = forms.CharField(max_length=50)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'full_name',
            'profile_image',
            'semester',
            'university',
            'github',
            'facebook',
            'linkedin'
        ]
#Pass reset

class PasswordResetForm(forms.Form):
    email = forms.EmailField()
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('new_password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

