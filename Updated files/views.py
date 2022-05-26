from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import PublisherList,List
from .form import ListForm

def base(request):
    return render(request, "base.html")


def home_view(request):
    if request.method == "POST":
      form = ListForm(request.POST or None)
      if form.is_valid():
          form.save()
          context = List.objects.all()
          return render(request, "home.html", {'context': context})
    else:
      context = List.objects.all()
      return render(request, "home.html", {'context': context})


def delete(request,list_id):
    context = List.objects.get(pk=list_id)
    context.delete()
    return redirect('hhome')

def edit(request, list_id):
    context = List.objects.get(pk=list_id)
    context.edit
    return redirect('hhome')


def about_view(request):
    context = {'f_name': 'Mohammed', 'l_name': 'Sulaiman'}
    return render(request, "about.html", context)




def publisher_list(request):
    context = PublisherList.objects.all()
    return render(request, "publisher_list.html", {'context': context})


def list(request):
    context = List.objects.all()
    return render(request, "publisher_list.html", {'context': context})





