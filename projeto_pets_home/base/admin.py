from django.contrib import admin
from base.models import AnimalAdocao

@admin.register(AnimalAdocao)
class AnimalAdocaoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'email', 'cpf', 'data', 'status']
  search_fields = ['nome','cpf', 'status']
  list_filter = ['data', 'status']
