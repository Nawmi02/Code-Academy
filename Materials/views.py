from django.shortcuts import render, get_object_or_404
from .models import Semester, Book, Note, Code, PreviousQuestion

def semester_list(request):
    semesters = Semester.objects.all()
    return render(request, 'materials/semesters.html', {'semesters': semesters})

def semester_base(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    context = {
        'semester': semester,
        'books_count': Book.objects.filter(semester=semester).count(),
        'notes_count': Note.objects.filter(semester=semester).count(),
        'codes_count': Code.objects.filter(semester=semester).count(),
        'questions_count': PreviousQuestion.objects.filter(semester=semester).count(),
    }
    return render(request, 'materials/sembase.html', context)

def book_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    books = Book.objects.filter(semester=semester)
    return render(request, 'materials/books.html', {
        'semester': semester,
        'books': books,
        'materials_active': 'books'
    })

def note_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    notes = Note.objects.filter(semester=semester)
    return render(request, 'materials/notes.html', {
        'semester': semester,
        'notes': notes,
        'materials_active': 'notes'
    })

def code_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    codes = Code.objects.filter(semester=semester)
    return render(request, 'materials/codes.html', {
        'semester': semester,
        'codes': codes,
        'materials_active': 'codes'
    })

def previous_question_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    questions = PreviousQuestion.objects.filter(semester=semester)
    return render(request, 'materials/prevques.html', {
        'semester': semester,
        'questions': questions,
        'materials_active': 'questions'
    })