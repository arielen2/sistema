from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=255)
    placa = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)
    
    def __str__(self):
        return self.placa
