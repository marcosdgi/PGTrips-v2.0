import json

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from django.utils.datastructures import MultiValueDictKeyError
from django.middleware.csrf import get_token


def get_csrf(request):
    csrf_token = get_token(request)
    return csrf_token


@api_view(['GET', 'POST'])
@csrf_exempt
@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            user_id = User.objects.get(username=username)
            credenciales = {
                'username': username,
                'password': password,
                'id': user_id.id
            }
            return Response(credenciales, status=status.HTTP_200_OK)
        else:
            response = {
                "message": "Usuario incorrecto"
            }
            return Response(status=status.HTTP_404_NOT_FOUND)
