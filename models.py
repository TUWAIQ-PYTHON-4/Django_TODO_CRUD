from django.db import models


# Create your models here.
class List(models.Model):
    # name = models.CharField(max_length=50, help_text="The name ")
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)


