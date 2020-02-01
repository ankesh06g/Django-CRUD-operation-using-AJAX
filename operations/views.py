from django.shortcuts import render
from django.http import HttpResponse
from operations.models import Language

def home(request):

    languages = Language.objects.all().order_by('id').reverse()

    return render(request, 'index.html', {'languages': languages})

def add(request):
    if request.method == 'POST':   
        text = request.POST['input_text']
        Language.objects.create(title=text)
        languages = Language.objects.all().order_by('id').reverse()
    return render(request, 'list.html', {'languages': languages})


def edit(request):
    if request.method == 'POST':   
        text = request.POST['input_text']
        new_text = request.POST['new_input_text']
        Language.objects.filter(title=text).update(title=new_text)
        languages = Language.objects.all().order_by('id').reverse()
    return render(request, 'list.html', {'languages': languages})


def delete(request):
    if request.method == 'POST':   
        text = request.POST['input_text']
        Language.objects.get(title=text).delete()
        languages = Language.objects.all().order_by('id').reverse()
    return render(request, 'list.html', {'languages': languages})


