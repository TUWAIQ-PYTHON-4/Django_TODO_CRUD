from django.db import models

# Create your models here.


class List(models.Model):
    item = models.CharField(max_length=50, help_text="The user to do item.")
    completed = models.BooleanField(default=False)

    def __str__(self) :
        return self.item + '|' + str(self.completed)



'''
The CRUD commands:

from ToDoListApp.models import User, Item
User1 = User.objects.create(name="Bushra", email="bushra@example.com")
user2  = User.objects.create(name="lily", email="lily@example.com")
item1 = Item.objects.create(to_do_item= 'study',to_do_list= User1)
item2 = Item.objects.create(to_do_item= 'work', completed= True, to_do_list= User1)

User.objects.all()
user = User.objects.get(name='Bushra')
item = Item.objects.filter(to_do_list= User1)

'''