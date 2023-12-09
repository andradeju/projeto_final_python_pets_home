from django.db import models

# Create your models here.


class Animal(models.Model):
    GENEROS_ANIMAIS = (
        ('F', 'Fêmea'),
        ('M', 'Macho')
    )
    nome = models.CharField(max_length=55)
    genero = models.CharField(
        max_length=50, choices=GENEROS_ANIMAIS, null=True)
    especie = models.CharField(max_length=50)
    idade = models.PositiveIntegerField()
    peso = models.PositiveIntegerField(null=True)
    raca = models.CharField(max_length=50)
    historico_saude = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return f'{self.nome} - {self.especie} : {self.idade}'

    class Meta:
        verbose_name = 'Cadastro de Animal'
        verbose_name_plural = 'Cadastros de Animais'
        ordering = ['-idade']
