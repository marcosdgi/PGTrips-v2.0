from django.urls import path
from autos.views.AutosApiView import AutosApiView

urlpatterns = [
    path('autos/', AutosApiView.as_view(), name='autos-api'),
]