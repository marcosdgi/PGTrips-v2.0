from django.db import models

class Origen(models.Model):
    id_origen = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,null=False,blank=False)


    def __str__(self):
        return self.nombre