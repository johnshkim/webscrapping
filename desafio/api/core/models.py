from django.db import models
#criacao da model Cadastro( nome, link e preco)
class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    link = models.TextField()
    preco = models.TextField(max_length=20)
    def __str__(self):
        return self.nome