from django.urls import path
from autenticacion.views.LoginView import login_view
from autenticacion.views.LogoutView import logout_view
from autenticacion.views.register_user import CreateUserView
urlpatterns = [
    path('login/',login_view,name='inicio_sesion'),
    path('logout/', logout_view, name='cerrar_sesion'),
    path('register/', CreateUserView.as_view(), name='registar_usuario'),
    ]