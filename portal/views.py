from django.shortcuts import render
from django.conf import settings
from .models import *

ms_identity_web = settings.MS_IDENTITY_WEB

def home(request):
    subscriptions = CloudProviderSubscription.objects.all()
    return render(request, "portal/home.html", {"subscriptions": subscriptions})

def index(request):
    return render(request, "portal/auth/status.html")

@ms_identity_web.login_required
def token_details(request):
    return render(request, "portal/auth/token.html")
