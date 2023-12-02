from django.shortcuts import render
from django.conf import settings
from .models import *

ms_identity_web = settings.MS_IDENTITY_WEB

def index(request):
    return render(request, "index.html")

@ms_identity_web.login_required
def token_details(request):
    return render(request, "auth/token_details.html")

@ms_identity_web.login_required
def provider(request):
    return render(request, "provider.html")