from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from base.forms import AnimalForm
from base.models import AnimalAdocao
from animais.models import Animal
from animais.filters import AnimalFilter
from django.db.models import Q


def home(request):
    animais = Animal.objects.all()[:4]
    return render(request, 'home.html', {'animais': animais})


def adocao(request):
    animais = Animal.objects.all()
    return render(request, 'adocao.html', {'animais': animais})


def animal_detalhes(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    form = AnimalForm()

    contexto = {
        'sucesso': False,
        'animal': animal,
        'form': form,
    }

    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            AnimalAdocao.objects.create(**form.cleaned_data)
            contexto['sucesso'] = True
            form = AnimalForm()

    return render(request, 'animal.html', contexto)


def busca_site(request):
    query = request.GET.get('q')
    has_results = False
    animal_filter = None

    if query:
        animal_filter = AnimalFilter(
            data={'search': query}, queryset=Animal.objects.all())
        has_results = animal_filter.qs.exists()

    return render(request, 'busca_resultados.html', {'filter': animal_filter, 'has_results': has_results})


def como_ajudar(request):
    return render(request, 'como_ajudar.html')


def sobre_nos(request):
    return render(request, 'sobre_nos.html')
