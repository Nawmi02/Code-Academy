from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification
from .forms import NotificationForm

def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notification.html', {'notifications': notifications})

def notification_delete(request, id):
    notification = get_object_or_404(Notification, id=id)
    if request.method == "POST":
        notification.delete()
        return redirect('home')
    return render(request, 'notification_confirm_delete.html', {'notification': notification})
