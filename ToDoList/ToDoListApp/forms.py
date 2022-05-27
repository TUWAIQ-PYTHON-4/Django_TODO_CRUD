from dataclasses import fields
from django import forms
from .models import List

# create a form 
class List_Form(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']