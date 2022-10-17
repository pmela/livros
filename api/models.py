from django.db import models


# Create your models here.
class Livro(models.Model):
    nome = models.CharField(max_length=64)
    autor = models.CharField(max_length=64)
    categoria = models.CharField(max_length=64)
    descricao = models.CharField(max_length=256)

    def __str__(self):
        return self.nome