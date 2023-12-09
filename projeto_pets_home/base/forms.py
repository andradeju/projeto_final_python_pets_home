from django import forms
from django.core.exceptions import ValidationError
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
        exclude = ['data', 'animal', 'status']
    animal = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    nome = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Nome Completo'}),)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': ''}),)
    cpf = forms.CharField(max_length=11, label='CPF', widget=forms.TextInput(
        attrs={'placeholder': 'Apenas números'}),)
    dataNascimento = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(
        attrs={'placeholder': 'DD/MM/YYYY'}), input_formats=['%d/%m/%Y'],)
    telefone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ''}),)
    profissao = forms.CharField(
        label='Profissão', widget=forms.TextInput(attrs={'placeholder': ''}),)
    cep = forms.CharField(max_length=8, widget=forms.TextInput(
        attrs={'placeholder': 'Apenas números'}),)
    endereco = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Rua, nº, complemento'}),)
    cidade = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ''}),)
    estado = forms.ChoiceField(choices=ESTADOS_CHOICES)
    motivoAdocao = forms.CharField(label='Motivo da Adoção', widget=forms.Textarea(
        attrs={'placeholder': '', 'rows': '3'}),)
    emCasoDeViagem = forms.CharField(
        label='Em caso de viagem, onde você deixará o animal adotado?', widget=forms.TextInput(attrs={'placeholder': ''}),)
    experienciaAnterior = forms.CharField(label='Experiência Anterior com Animais de Estimação', widget=forms.Textarea(
        attrs={'placeholder': '', 'rows': '2'}),)
    temAnimal = forms.ChoiceField(label='Tem algum animal em sua residência?', choices=[
                                  (True, 'Sim'), (False, 'Não')], widget=forms.RadioSelect)

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError(
                "CPF inválido. Certifique-se de inserir apenas números e ter 11 dígitos.")

        return cpf

    def clean_dataNascimento(self):
        data_nascimento = self.cleaned_data.get('dataNascimento')
        if data_nascimento.year < 1900:
            raise ValidationError(
                "Ano de nascimento inválido. Certifique-se de inserir uma data válida.")

        return data_nascimento

    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if len(cep) != 8 or not cep.isdigit():
            raise ValidationError("O CEP deve ter 8 dígitos e apenas números")
        return cep

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not telefone.isdigit():
            raise ValidationError("O telefone deve conter apenas números")
        return telefone

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
