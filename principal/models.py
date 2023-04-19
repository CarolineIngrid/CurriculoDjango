from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(blank=True, null=True, max_length=40)
    mensagem = models.CharField(max_length=30)

    def __str__(self):
        return self.id