from rest_framework.serializers import ModelSerializer

from reservaciones.models.Reservacion import Reservacion


class ReservacionSerializer(ModelSerializer):
    class Meta:
        model = Reservacion
        fields = '__all__'