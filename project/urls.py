"""
URL configuration for project project.
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
# from . import views
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from ms_identity_web.django.msal_views_and_urls import MsalViews

# msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
    path('', include('portal.urls')),
    # path('sign_in_status', views.index, name='status'),
    # path('token_details', views.token_details, name='token_details'),
    # path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),
    # *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
