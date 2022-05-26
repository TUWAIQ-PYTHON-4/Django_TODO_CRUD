from django.urls import path
import ToDoListApp.views
urlpatterns = [
    path('', ToDoListApp.views.home, name='home'),
    path('about/', ToDoListApp.views.about, name='about'),
    path('delete/<Item_id>', ToDoListApp.views.delete, name='delete'),
    path('edit/<Item_id>', ToDoListApp.views.edit, name='edit')
]