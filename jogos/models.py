
from django.db import models
from django.utils import timezone

# Create your models here.

class Modalidade(models.Model):

    OPC = {
        "Coletiva":"Coletiva", 
        "Individual":"Individual"
    }

    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(choices=OPC)
    max_atletas = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Modalidade"
        verbose_name_plural = "Modalidades"

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    curso = models.CharField(max_length=100)
    cor = models.CharField(max_length=7)
    criada_em = models.DateTimeField(auto_now_add=timezone.now())
    # atletas = models.ForeignKey('Atleta', on_delete=models.PROTECT, related_name="atletas")
    # tecnico = models.OneToOneField('Tecnico', on_delete=models.CASCADE, related_name="tecnico")


    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    def __str__(self):
        return self.nome

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tecnico"
        verbose_name_plural = "Tecnicos"

    def __str__(self):
        return self.nome

class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100, unique=True)
    data_nascimento = models.DateField()
    # modalidades = models.ManyToManyField(Modalidade, null=True, blank=True, related_name="modalidades")


    class Meta:
        verbose_name = "Atleta"
        verbose_name_plural = "Atletas"

    def __str__(self):
            return self.nome


