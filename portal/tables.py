import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import *

class CloudProviderTable(tables.Table):
    btn_edit = TemplateColumn(verbose_name="", template_code='<a href="{% url "index" %}" class="btn btn-success">Edit</a>')
    class Meta:
        model = CloudProvider
        fields = ("id", "name", "is_enabled", "btn_edit")