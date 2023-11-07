from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def adocao(request):
  return render(request, 'adocao.html')

def form_adocao(request):
  return render(request, 'form_adocao.html')  

def como_ajudar(request):
  return render(request, 'como_ajudar.html')  

def sobre_nos(request):
  return render(request, 'sobre_nos.html')    


