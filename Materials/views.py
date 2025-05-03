from django.shortcuts import render,redirect,get_object_or_404
from .models import Semester, Book, Note, Code, PreviousQuestion
from .forms import NoteForm

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
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(
            semester=semester,
            title__icontains=query
        )
    else:
        notes = Note.objects.filter(semester=semester)

    return render(request, 'materials/notes.html', {
        'semester': semester,
        'notes': notes,
        'materials_active': 'notes',
        'query': query
    })

def note_create(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)

    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.semester = semester
            note.save()
            return redirect('materials:note_list', semester_id=semester.id)
    else:
        form = NoteForm(initial={'semester': semester})

    return render(request, 'materials/note_form.html', {
        'form': form,
        'semester': semester
    })

def note_update(request, semester_id, id):
    semester = get_object_or_404(Semester, id=semester_id)
    note = get_object_or_404(Note, id=id, semester=semester)

    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('materials:note_list', semester_id=semester.id)
    else:
        form = NoteForm(instance=note)

    return render(request, 'materials/note_form.html', {
        'form': form,
        'semester': semester
    })

def note_delete(request, semester_id, id):
    note = get_object_or_404(Note, id=id, semester_id=semester_id)
    if request.method == "POST":
        note.delete()
        return redirect('materials:note_list', semester_id=semester_id)
    return render(request, 'materials/notes.html', {'note': note})

def code_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    query = request.GET.get('q')
    if query:
        codes = Code.objects.filter(
            semester=semester,
            title__icontains=query
        )
    else:
        codes = Code.objects.filter(semester=semester)

    return render(request, 'materials/codes.html', {
        'semester': semester,
        'codes': codes,
        'materials_active': 'codes',
        'query': query
    })

def previous_question_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    questions = PreviousQuestion.objects.filter(semester=semester)
    return render(request, 'materials/prevques.html', {
        'semester': semester,
        'questions': questions,
        'materials_active': 'questions'
    })
