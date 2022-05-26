from django.shortcuts import render, redirect
from .models import List
from .forms import NewForm


def home(request):
    if request.method == "POST":
        form = NewForm(request.POST or None)
        if form.is_valid():
            form.save()
            items = List.objects.all()
            return render(request, "home.html", {'items': items})
    else:
        items = List.objects.all()
        return render(request, "home.html", {'items': items})


def about(request):
    first_name = "Hawra"
    last_name = "Alomani"
    return render(request, "about.html", {"first_name": first_name, "last_name": last_name})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    return redirect('home')


def edit(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk=list_id)
        form = NewForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})
