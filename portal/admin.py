from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CloudStage)
admin.site.register(CloudProvider)
admin.site.register(CloudProviderRegion)
admin.site.register(CloudProviderSubscription)
admin.site.register(CloudResourceType)
admin.site.register(CloudResource)