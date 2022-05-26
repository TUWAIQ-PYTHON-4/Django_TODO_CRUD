from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items':all_items})

def about(request):
    context = {'f_name': 'Amal', 'l_name': 'Ahmed'}
    return render(request, 'about.html', context)


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