from django import forms
from .models import ImageModel

class InputForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image_file']