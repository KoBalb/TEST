from django import forms
from .models import Text

class UserTextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['text']