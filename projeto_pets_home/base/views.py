from django.shortcuts import render
from django.http import HttpResponse
from base.forms import AnimalForm
from base.models import AnimalAdocao

def home(request):
  return render(request, 'home.html')

def adocao(request):
  return render(request, 'adocao.html')

def animal(request):
  sucesso = False
  if request.method == 'GET':
    form = AnimalForm()
  else:
    form = AnimalForm(request.POST)
    if form.is_valid():
      sucesso = True
      AnimalAdocao.objects.create(**form.cleaned_data)
      form = AnimalForm()
  contexto = {
        'form': form,
        'sucesso': sucesso
  }  
  return render(request, 'animal.html', contexto) 

def como_ajudar(request):
  return render(request, 'como_ajudar.html')  

def sobre_nos(request):
  return render(request, 'sobre_nos.html')    


