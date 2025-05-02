from django.shortcuts import render,redirect,get_object_or_404
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
            return redirect('guidelines')
    context = {'form':form}
    return render(request,template_name = 'guidelineForm.html',context=context)


def updateGuideline(request,id):
    guideline = get_object_or_404(Guideline, pk=id)
    form = GuidelineForm(instance=guideline)
    if request.method =='POST':
        form = GuidelineForm(request.POST,request.FILES,instance = guideline)
        if form.is_valid():
            form.save()
            return redirect('guidelines')
    context = {'form':form}
    return render(request,template_name = 'guidelineForm.html',context = context)

        
def delete_Guideline(request,id):
    guideline = get_object_or_404(Guideline, pk=id)
    if request.method =='POST':
        guideline.delete()
        return redirect('guidelines')

    return render(request,template_name = 'guidelines.html')