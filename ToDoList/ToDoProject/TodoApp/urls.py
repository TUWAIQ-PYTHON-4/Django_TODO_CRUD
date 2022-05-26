from django.urls import path
from . import views

app_name = 'ToDoApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<id>/', views.delete, name='delete'),
    path('update/<id>/', views.update, name='update')
]