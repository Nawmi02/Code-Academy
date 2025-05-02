from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileUpdateForm
from .models import UserProfile
from django.conf import settings

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

# User Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()

            UserProfile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                semester=form.cleaned_data['semester'],
                profile_image=form.cleaned_data.get('profile_image')
            )

            return render(request, 'register.html', {'form': form, 'success': True})  
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# User Profile View + Update
@login_required(login_url=settings.LOGIN_URL)
def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile})

# Delete Profile View
@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('landing')  # redirect to landing page after delete
    return render(request, 'profile.html')

#landing view
def landing_view(request):
    return render(request,'landing.html')


# Home Page View (after login)
@login_required
def home_view(request):
    return render(request, 'home.html')

