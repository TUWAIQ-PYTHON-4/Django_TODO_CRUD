from django.db import models
from django.forms import ModelForm

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length = 200) 
    completed = models.BooleanField(default = False) 
    
    # Add string representation str() 
    def __str__(self):
        return self.item + str(self.completed)