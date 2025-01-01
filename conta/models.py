from django.db import models

class Topico(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Comunicado(models.Model):
    texto = models.TextField()
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.texto[:25]+"..."
