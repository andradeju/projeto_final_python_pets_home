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
from django.conf import settings
from django.conf.urls.static import static
from base.views import home, adocao, animal_detalhes, busca_site, sobre_nos, como_ajudar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='inicio'),
    path('adocao/', adocao, name='adocao'),
    path('animal_detalhes/<int:animal_id>/', animal_detalhes, name='animal_detalhes'),
    path('como-ajudar/', como_ajudar, name='como_ajudar'),
    path('sobre-nos/', sobre_nos, name='sobre_nos'),
    path('busca/', busca_site, name='busca_site'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)