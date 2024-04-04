from django.db import models


class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    placa = models.CharField(max_length=100, null=False, blank=False)
    Imagen = models.ImageField(null=False, upload_to='media/img/')
    km_recorridos = models.IntegerField(null=True, blank=True, default=0)
    fecha_annadido = models.DateField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return self.modelo
