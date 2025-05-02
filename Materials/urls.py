from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.semester_list, name='semester_list'),
    path('semester/<int:semester_id>/', views.semester_base, name='sembase'),  # 👉 eta add korte hobe
    path('semester/<int:semester_id>/books/', views.book_list, name='book_list'),
    path('semester/<int:semester_id>/notes/', views.note_list, name='note_list'),
    
    path('semester/<int:semester_id>/notes/create/', views.note_create, name='note_create'),
    path('semester/<int:semester_id>/notes/<int:id>/update/', views.note_update, name='note_update'),
    path('semester/<int:semester_id>/notes/<int:id>/delete/', views.note_delete, name='note_delete'),

    
    path('semester/<int:semester_id>/codes/', views.code_list, name='code_list'),
    path('semester/<int:semester_id>/codes/create/', views.code_create, name='code_create'),
    path('semester/<int:semester_id>/codes/<int:id>/update/', views.code_update, name='code_update'),
    path('semester/<int:semester_id>/codes/<int:id>/delete/', views.code_delete, name='code_delete'),


    path('semester/<int:semester_id>/previous-questions/', views.previous_question_list, name='previous_question_list'),
]
