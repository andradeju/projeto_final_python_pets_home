import django_filters
from django.db.models import Q
from animais.models import Animal
from unidecode import unidecode

class AnimalFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')

    class Meta:
        model = Animal
        fields = '__all__'
        exclude = ['imagem']

    def filter_search(self, queryset, _, value):
        if not value:
            return queryset

        value = unidecode(value.lower())
        q_objects = [
            Q(**{f'{field}__icontains': value}) 
            for field in ['nome', 'genero', 'especie', 'idade', 'raca', 'historico_saude']
        ]

        genero_mapping = {'macho': 'M', 'femea': 'F'}
        q_objects.append(Q(genero__iexact=genero_mapping.get(value, '')))
            
        q_object = Q()
        for obj in q_objects:
            q_object |= obj

        return queryset.filter(q_object)

