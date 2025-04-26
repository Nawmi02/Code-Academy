from django.shortcuts import render, get_object_or_404
from .models import Semester, Book, Note, Code, PreviousQuestion

# View: Semester list page (main materials page)
def semester_list(request):
    semesters = Semester.objects.all()
    return render(request, 'materials/semesters.html', {'semesters': semesters})

def semester_base(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    return render(request, 'materials/sembase.html', {'semester': semester})

# View: Book list page for specific semester
def book_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    books = Book.objects.filter(semester=semester)
    return render(request, 'materials/books.html', {'semester': semester, 'books': books})

# View: Notes list page for specific semester
def note_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    notes = Note.objects.filter(semester=semester)
    return render(request, 'materials/notes.html', {'semester': semester, 'notes': notes})

# View: Codes list page for specific semester
def code_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    codes = Code.objects.filter(semester=semester)
    return render(request, 'materials/codes.html', {'semester': semester, 'codes': codes})

# View: Previous Questions list page for specific semester
def previous_question_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    questions = PreviousQuestion.objects.filter(semester=semester)
    return render(request, 'materials/prevques.html', {'semester': semester, 'questions': questions})
