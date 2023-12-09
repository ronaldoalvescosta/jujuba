from django.shortcuts import render
from django.conf import settings
from django_tables2 import SingleTableView

from .models import *
from .tables import *

ms_identity_web = settings.MS_IDENTITY_WEB

def index(request):
    return render(request, "index.html")

@ms_identity_web.login_required
def token_details(request):
    return render(request, "auth/token_details.html")

class CloudProviderListView(SingleTableView):
    model = CloudProvider
    table_class = CloudProviderTable
    template_name = "provider.html"
    table_pagination = {"per_page": 1}

@ms_identity_web.login_required
def provider(request):
    return render(request, "provider.html", CloudProviderListView)