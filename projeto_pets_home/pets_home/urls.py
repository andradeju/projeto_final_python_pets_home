from django.contrib import admin
from django.urls import path, include
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
    path('api-auth/', include('rest_framework.urls')),
    path('apipets/', include('rest_api.urls', namespace='apipets'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)