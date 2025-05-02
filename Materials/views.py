from django.shortcuts import render,redirect,get_object_or_404
from .models import Semester, Book, Note, Code, PreviousQuestion
from .forms import NoteForm,CodeForm

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

        
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'materials/note_form.html', {'form': form})

        
def note_update(request, id):
    note = get_object_or_404(Note,id=id)
    if request.method=="POST":
        form = NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = NoteForm(instance=note)
    return render(request, 'materials/note_form.html', {'form': form})

def note_delete(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        note.delete()
        return redirect('home')
    return render(request, 'materials/note_confirm_delete.html', {'note': note})


def code_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    codes = Code.objects.filter(semester=semester)
    return render(request, 'materials/codes.html', {
        'semester': semester,
        'codes': codes,
        'materials_active': 'codes'
    })

def code_create(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CodeForm()
    return render(request, 'materials/code_form.html', {'form': form})

def code_update(request, id):
    code = get_object_or_404(Code,id=id)
    if request.method=="POST":
        form = CodeForm(request.POST,instance=code)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = CodeForm(instance=code)
    return render(request, 'materials/code_form.html', {'form': form})

def code_delete(request, id):
    code = get_object_or_404(Code, id=id)
    if request.method == "POST":
        code.delete()
        return redirect('home')
    return render(request, 'materials/code_confirm_delete.html', {'code': code})



def previous_question_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    questions = PreviousQuestion.objects.filter(semester=semester)
    return render(request, 'materials/prevques.html', {
        'semester': semester,
        'questions': questions,
        'materials_active': 'questions'
    })