from django.contrib import admin

from reservaciones.models.Destino import Destino
from reservaciones.models.Origen import Origen
from reservaciones.models.Reservacion import Reservacion

admin.site.register(Reservacion)
admin.site.register(Destino)
admin.site.register(Origen)