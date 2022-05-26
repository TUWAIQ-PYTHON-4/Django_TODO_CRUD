from django.db import models

class Item(models.Model):
    item = models.CharField(max_length=200, help_text="What to do next ?")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time of creation.")
    completed = models.BooleanField(default=False)

    def __str__(self) :
        return self.item
