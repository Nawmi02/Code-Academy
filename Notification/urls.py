from django.urls import path
from . import views

urlpatterns = [
    path('',views.notification_list , name = "notification"),
    path('delete/<int:id>/',views.notification_delete,name='notification_delete'),
]