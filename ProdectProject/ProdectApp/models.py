from django.db import models

class List(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(max_length=10000)

    def __str__(self):
        return self.name + ' | ' + str(self.price)