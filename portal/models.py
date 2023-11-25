from django.conf import settings
from django.db import models
from django.utils import timezone
from model_utils import Choices

# CLOUD_STAGES = Choices('dev', 'hml', 'prd')
# CLOUD_PROVIDERS = Choices('aws', 'azure', 'gcp', 'oci')
# CLOUD_RESOURCE_TYPES = Choices('s3', 'storageaccount')

"""
django model representing cloud providers such as aws, azure, gcp, oci, etc
"""
class CloudProvider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_cloud_provider_id(cls, cloud_provider_name: str) -> int:
        cloud_provider, created = cls.objects.get_or_create(name=cloud_provider_name)
        return cloud_provider.id

"""
django model representing cloud provider regions such as aws us-east-1, azure eastus, gcp us-central1, etc
"""
class CloudProviderRegion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    cloud_provider = models.ForeignKey(CloudProvider, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_cloud_provider_region_id(cls, cloud_provider_region_name: str, cloud_provider_id: int) -> int:
        cloud_provider_region, created = cls.objects.get_or_create(name=cloud_provider_region_name, cloud_provider=cloud_provider_id)
        return cloud_provider_region.id

"""
django model representing stage type such as dev, hml, prod, etc
"""
class CloudStage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    @classmethod
    def get_cloud_stage_id(cls, cloud_stage_name: str) -> int:
        cloud_stage, created = cls.objects.get_or_create(name=cloud_stage_name)
        return cloud_stage.id

"""
django model representing cloud provider accounts such as aws account number, azure subscription id, etc
"""
class CloudProviderSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    subscription = models.CharField(max_length=200)
    cloud_provider = models.ForeignKey(CloudProvider, on_delete=models.PROTECT)
    stage = models.ForeignKey(CloudStage, on_delete=models.PROTECT, default=CloudStage.get_cloud_stage_id("dev"))

    def __str__(self):
        return self.name
    
    @classmethod
    def get_cloud_provider_subscription_id(cls, cloud_provider_id: int, stage_id: int) -> int:
        cloud_provider_subscription = cls.objects.get(cloud_provider=cloud_provider_id, stage=stage_id)
        return cloud_provider_subscription.id
    
    @classmethod
    def get_cloud_provider_subscription_value(cls, cloud_provider_id: int, stage_id: int) -> int:
        cloud_provider_subscription = cls.objects.get(cloud_provider=cloud_provider_id, stage=stage_id)
        return cloud_provider_subscription.subscription

"""
django model representing resource type such as objectstorage, messagequeue, etc
"""
class CloudResourceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def get_cloud_resource_type_id(cls, cloud_resource_type_name: str) -> int:
        cloud_resource_type, created  = cls.objects.get_or_create(name=cloud_resource_type_name)
        return cloud_resource_type.id

"""
django model representing cloud resouce instances such as aws s3, azure resource group, azure storage account, etc
"""
class CloudResource(models.Model):    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    resource_type = models.ForeignKey(CloudResourceType, on_delete=models.PROTECT)    
    provider = models.ForeignKey(CloudProvider, on_delete=models.PROTECT)
    provider_region = models.ForeignKey(CloudProviderRegion, on_delete=models.PROTECT)
    stage = models.ForeignKey(CloudStage, max_length=50, on_delete=models.PROTECT)
    subscription = models.ForeignKey(CloudProviderSubscription, on_delete=models.PROTECT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    compartment = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    tags = models.JSONField(null=True, blank=True)
    resource_id = models.CharField(max_length=200, editable=False, null=True, blank=True)
    private_endpoint = models.CharField(max_length=200, editable=False, null=True, blank=True)
    acl = models.CharField(max_length=200, editable=False, null=True, blank=True)
    lifecycle = models.CharField(max_length=200, null=True, blank=True)
    encryption = models.CharField(max_length=200, null=True, blank=True)
    versioning = models.CharField(max_length=200, null=True, blank=True)
    logging = models.CharField(max_length=200, null=True, blank=True)
    public_endpoint = models.CharField(max_length=200, null=True, blank=True)
    notification = models.CharField(max_length=200, null=True, blank=True)
    policy = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_cloud_resource_id(cls, cloud_resource_name: str, subscription_id: int) -> int:
        cloud_resource = cls.objects.get(name=cloud_resource_name, subscription=subscription_id)
        return cloud_resource.id