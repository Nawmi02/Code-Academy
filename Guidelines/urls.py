from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path('', views.show_guidelines, name='guidelines'),
]
=======
    path('', views.guideline, name='guidelines'),
]
>>>>>>> Stashed changes
