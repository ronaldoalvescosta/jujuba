# Generated by Django 4.2.6 on 2023-12-03 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0009_alter_cloudresource_acl_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloudprovider',
            name='is_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cloudprovider',
            name='is_supported',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cloudproviderregion',
            name='cloud_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.cloudprovider'),
        ),
        migrations.AlterField(
            model_name='cloudprovidersubscription',
            name='cloud_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.cloudprovider'),
        ),
        migrations.AlterField(
            model_name='cloudprovidersubscription',
            name='stage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='portal.cloudstage'),
        ),
        migrations.AlterField(
            model_name='cloudresource',
            name='compartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.cloudresource'),
        ),
        migrations.AlterField(
            model_name='cloudresource',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cloudresource',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.cloudprovider'),
        ),
        migrations.AlterField(
            model_name='cloudresource',
            name='provider_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.cloudproviderregion'),
        ),
        migrations.AlterField(
            model_name='cloudresource',
            name='resource_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.cloudresourcetype'),
        ),
        migrations.AlterField(
            model_name='cloudresource',
            name='stage',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, to='portal.cloudstage'),
        ),
        migrations.AlterField(
            model_name='cloudresource',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.cloudprovidersubscription'),
        ),
    ]