from django import forms
from base.models import AnimalAdocao


class AnimalForm(forms.ModelForm):
  ESTADOS_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)
  class Meta:
    model = AnimalAdocao
    exclude = ['data' ,'animal', 'status']
  animal = forms.IntegerField(widget=forms.HiddenInput(), required=False)  
  nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nome Completo'}),)
  email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':''}),)
  cpf = forms.CharField(max_length=11, label='CPF',widget=forms.TextInput(attrs={'placeholder':'Apenas números'}),)
  dataNascimento = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'placeholder':'DD/MM/YYYY'}), input_formats=['%d/%m/%Y'],)
  telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':''}),)
  profissao = forms.CharField(label='Profissão', widget=forms.TextInput(attrs={'placeholder':''}),)
  endereco = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Rua, nº, complemento'}),)
  cidade = forms.CharField(widget=forms.TextInput(attrs={'placeholder':''}),)
  estado = forms.ChoiceField(choices=ESTADOS_CHOICES)
  cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder':'00000-000'}),)
  motivoAdocao = forms.CharField(label='Motivo da Adoção', widget=forms.Textarea(attrs={'placeholder':'', 'rows':'3'}),)
  emCasoDeViagem = forms.CharField(label='Em caso de viagem, onde você deixará o animal adotado?', widget=forms.TextInput(attrs={'placeholder':''}),)
  experienciaAnterior = forms.CharField(label='Experiência Anterior com Animais de Estimação', widget=forms.Textarea(attrs={'placeholder':'', 'rows': '2'}),)
  temAnimal = forms.ChoiceField(label='Tem algum animal em sua residência?', choices=[(True, 'Sim'), (False, 'Não')], widget=forms.RadioSelect)
  
