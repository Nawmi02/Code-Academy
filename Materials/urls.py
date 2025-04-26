from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.semester_list, name='semester_list'),
    path('semester/<int:semester_id>/', views.semester_base, name='sembase'),  # 👉 eta add korte hobe
    path('semester/<int:semester_id>/books/', views.book_list, name='book_list'),
    path('semester/<int:semester_id>/notes/', views.note_list, name='note_list'),
    path('semester/<int:semester_id>/codes/', views.code_list, name='code_list'),
    path('semester/<int:semester_id>/previous-questions/', views.previous_question_list, name='previous_question_list'),
]
