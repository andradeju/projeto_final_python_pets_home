from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'POST'])
def api_pets(request):
  if request.method == 'POST':
    return Response({'message':f'Essa é a REST API,{request.data.get("name")}'})
  return Response({'message':'API'})
