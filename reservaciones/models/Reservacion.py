from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from datetime import date


class Reservacion(models.Model):
    id_reservacion = models.AutoField(primary_key=True)
    a_nombre_de = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    origen = models.CharField(max_length=150, null=False, blank=False)
    destino = models.CharField(max_length=150, blank=False, null=False)
    fecha = models.DateField(null=False, default=now())
    hora = models.TimeField(null=False, default=now())

    class Meta:
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return '%s %s %s %s %s' % (self.origen, self.destino, self.fecha, self.id_reservacion, self.hora)
