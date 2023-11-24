from django.contrib import admin
from animais.models import Animal

# Register your models here.
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
  list_display = ['nome', 'especie', 'idade']
  search_fields = ['especie', 'idade', 'raca']
  list_filter = ['idade']