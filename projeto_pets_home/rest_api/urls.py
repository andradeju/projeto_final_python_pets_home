from django.urls import path
from rest_api.views import api_pets

app_name = 'rest_api'
urlpatterns = [
  path('api_pets', api_pets, name='api_pets'),
]