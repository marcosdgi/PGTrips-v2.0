from django.urls import path
from reservaciones.views.ReservationView import ReservationView

urlpatterns = [
    path('reservaciones/', ReservationView.as_view(), name='reservaciones'),
    path('reservaciones/<int:pk>', ReservationView.as_view(), name='obtener_reservacion'),
    # path('reservaciones/<str:username>', ReservationView.as_view(), name='realizar_reservacion')
]
