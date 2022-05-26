from django.urls import path
from ToDoList import views


urlpatterns = [
    path('', views.base),
    path('home/', views.home_view, name = 'hhome'),
    path('about/', views.about_view, name = 'aabout'),
    path('publisher_list/', views.publisher_list, name = 'pub'),
    path('delete/<list_id>', views.delete, name = "delete"),
    path('edit/<list_id>', views.edit, name = "edit")

]

