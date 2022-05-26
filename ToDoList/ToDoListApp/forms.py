from django import forms
from .models import List


class NewForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
