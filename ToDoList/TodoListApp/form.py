from django import forms
from .models import Lista

class ListForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ["item", "completed"]