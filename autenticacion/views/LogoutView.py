from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required
def logout_view(request):
    logout(request)
