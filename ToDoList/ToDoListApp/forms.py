from django import forms


from .models import List

class ExampleForm(forms.ModelForm):
    class Meta:
        model = List
        fields = "__all__" #اقدر احط الي ابي هنا مثلا [complate,"item"]


