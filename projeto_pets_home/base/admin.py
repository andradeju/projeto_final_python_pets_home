from django.contrib import admin
from base.models import AnimalAdocao

@admin.register(AnimalAdocao)
class AnimalAdocaoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'email', 'cpf', 'data']
  search_fields = ['nome','cpf']
  list_filter = ['data']
