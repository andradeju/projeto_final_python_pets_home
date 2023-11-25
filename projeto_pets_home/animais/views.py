from django.shortcuts import render
from animais.models import Animal
from django.shortcuts import get_object_or_404

# Create your views here.
def animal (request, animal_id):
  animal = get_object_or_404(Animal, pk=animal_id)
  return render(request, 'animal.html',{'animal': animal})

