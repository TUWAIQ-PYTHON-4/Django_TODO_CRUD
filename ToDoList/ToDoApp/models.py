from django.db import models


# Create your models here.

# class personal_info(models.Model):
#     f_name = models.CharField(max_length=50, help_text="Your first name .")
#     l_name = models.CharField(max_length=50, help_text="Your last name")
#
#     def __str__(self):
#         return self.f_name + ' ' + self.l_name
#
#
# class person_todo_list(models.Model):
#     item = models.CharField(max_length=100, help_text='add your to do list item')
#     person = models.ForeignKey(personal_info, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.item

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' ' + str(self.completed)
