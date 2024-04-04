from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from autenticacion.serializers.CustomUserSerializer import CustomUserSerializer
from reservaciones.models.Reservacion import Reservacion
from reservaciones.serializers.ReservacionSerializer import ReservacionSerializer


class ReservationView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    
    def get(self, request, date=None, *args, **kwargs):

        try:
            if date is not None:
                reservation = Reservacion.objects.get(date=date)
                reservation_serializer = ReservacionSerializer(reservation)
                return Response(reservation_serializer.data, status=status.HTTP_200_OK)
            else:
                reservations = Reservacion.objects.filter(a_nombre_de=request.user)
                reservations_serializer = ReservacionSerializer(reservations, many=True)
                return Response(reservations_serializer.data, status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
   
    def post(self, request, *args, **kwargs):

        user = request.user
        reservation = request.data
        reservation_serializer = ReservacionSerializer(data=reservation)
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(reservation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            reservation = Reservacion.objects.get(id_reservacion=pk)
            reservation_serializer = ReservacionSerializer(reservation, data=request.data)
            if reservation_serializer.is_valid():
                reservation_serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(reservation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        try:
            reservation = Reservacion.objects.get(id_reservacion=pk)
            reservation.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
