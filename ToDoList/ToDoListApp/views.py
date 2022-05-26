from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm


def home(request):

    if request.method == "POST":
        form = ListForm(request.POST or None)
        form.save()
        all_list = List.objects.all()
        return render(request, 'home.html', {'list': all_list})
    else:
        all_list = List.objects.all()
        return render(request, 'home.html', {'list': all_list})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    return redirect('home')

def edit(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})

def about(request):
    name = 'Bushra Alzahrani'
    return render(request, 'about.html', {'name':name})