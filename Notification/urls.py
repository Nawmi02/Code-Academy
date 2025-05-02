from django.urls import path
from . import views

urlpatterns = [
    path('',views.notification_list , name = "notification"),
    path('delete/<int:id>/',views.Notification_delete,name='Notification_delete'),
]