from django.urls import path
from . import views

urlpatterns = [
    path('',views.guidelines , name = "guidelines"),
]