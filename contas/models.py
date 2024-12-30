from django.db import models


class Categoia(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacoes(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoia = models.ForeignKey(Categoia, on_delete=models.CASCADE)
    opcional = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.descricao