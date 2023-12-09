from django.db import models
from animais.models import Animal

# Create your models here.


class AnimalAdocao(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=51)
    email = models.EmailField(max_length=77)
    cpf = models.CharField(max_length=11)
    dataNascimento = models.DateField()
    telefone = models.CharField(max_length=16)
    profissao = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=102)
    estado = models.CharField(max_length=2)
    motivoAdocao = models.TextField()
    emCasoDeViagem = models.TextField()
    experienciaAnterior = models.TextField()
    temAnimal = models.BooleanField(
        choices=[(True, 'Sim'), (False, 'Não')], default=False)
    status = models.CharField(max_length=22, choices=[('Pendente', 'Pendente'), (
        'Aprovada', 'Aprovada'), ('Recusada', 'Recusada')], default='Pendente')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} [{self.cpf}]'

    class Meta:
        verbose_name = 'Formulário de Adoção'
        verbose_name_plural = 'Formulários de Adoções'
        ordering = ['-data']
