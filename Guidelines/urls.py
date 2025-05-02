from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_guidelines, name='guidelines'),
    path('addGuideline/',views.addGuideline,name='addGuideline'),
    path('updateGuideline/<str:id>',views.updateGuideline,name = 'updateGuideline'),
    path('delete_Guideline/<str:id>',views.delete_Guideline,name = 'delete_Guideline'),
]


