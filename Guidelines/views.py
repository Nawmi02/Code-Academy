from django.shortcuts import render,redirect
from .models import Guideline
from .forms import * 

def show_guidelines(request):
    all_guidelines = Guideline.objects.all()
    return render(request, 'guidelines.html', {'guidelines': all_guidelines})

def addGuideline(request):
    form = GuidelineForm()
    if request.method == 'POST':
        form = GuidelineForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,template_name = 'Materials/addGuideline.html',context=context)


def updateGuideline(request,id):
    guideline = Guideline.objects.get(primary_key=id)
    form = GuidelineForm(instance=guideline)
    if request.method =='POST':
        form = GuidelineForm(request.POST,request.FILES,instance = guideline)
        if form.is_valid():
            form.save()
            return redirect('home',id = guideline.id)
    context = {'form':form}
    return render(request,template_name = 'Materials/addGuideline.html',context = context)

        
def delete_Guideline(request,id):
    guideline = Guideline.objects.get(primary_key = id)
    if request.method =='POST':
        guideline.delete()
        return redirect('home')

    return render(request,template_name = 'Materials/delete_Guideline.html')