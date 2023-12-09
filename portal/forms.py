from django import forms
from .models import *

class PostCloudProvider(forms.ModelForm):
    class Meta:
        model = CloudProvider
        fields = ("name")