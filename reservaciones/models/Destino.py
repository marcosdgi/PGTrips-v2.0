from django.db import models

class Destino (models.Model):
    id_destino = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=False,blank=False)
    costo = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"

    def __str__(self):
        return self.nombre