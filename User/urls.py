from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'), 
    path('home/', views.home_view, name='home'),  
    path('login/', views.login_view, name='login'),   
    path('register/', views.register_view, name='register'),  
    path('profile/', views.profile_view, name='profile'),  
    path('delete-profile/', views.delete_profile, name='delete_profile'),
    path('reset-password/', views.reset_password_view, name='reset_password')
]
