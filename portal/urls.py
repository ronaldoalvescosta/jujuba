from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ms_identity_web.django.msal_views_and_urls import MsalViews
from . import views

msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('sign_in_status', views.index, name='status'),
    path('token_details', views.token_details, name='token_details'),
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
