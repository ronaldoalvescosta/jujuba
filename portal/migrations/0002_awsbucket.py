# Generated by Django 4.2.6 on 2023-11-15 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AWSBucket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('tags', models.JSONField(blank=True, null=True)),
                ('arn', models.CharField(editable=False, max_length=200, null=True)),
                ('url', models.CharField(editable=False, max_length=200, null=True)),
                ('acl', models.CharField(editable=False, max_length=200, null=True)),
                ('lifecycle', models.CharField(max_length=200, null=True)),
                ('encryption', models.CharField(max_length=200, null=True)),
                ('versioning', models.CharField(max_length=200, null=True)),
                ('logging', models.CharField(max_length=200, null=True)),
                ('website', models.CharField(max_length=200, null=True)),
                ('notification', models.CharField(max_length=200, null=True)),
                ('policy', models.CharField(max_length=200, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.cloudprovider')),
                ('resource_type', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='portal.cloudresourcetype')),
                ('stage_type', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='portal.cloudstagetype')),
            ],
        ),
    ]