"""
URL configuration for pets_home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import home, adocao, form_adocao, sobre_nos, como_ajudar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('adocao/', adocao),
    path('form-adocao/', form_adocao),
    path('como-ajudar/', como_ajudar),
    path('sobre-nos/', sobre_nos),
]
