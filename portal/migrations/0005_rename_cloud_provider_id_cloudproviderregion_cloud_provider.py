# Generated by Django 4.2.6 on 2023-11-15 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_cloudprovidersubscription_stage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cloudproviderregion',
            old_name='cloud_provider_id',
            new_name='cloud_provider',
        ),
    ]
