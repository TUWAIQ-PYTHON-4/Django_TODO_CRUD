from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm

def about(request):
    context = {'f_name': 'Wafa', 'l_name': 'Ali'}
    return render(request, 'about.html', context)


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, id):
    item = List.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect('/')
    # return redirect('home')
    # return render(request, 'home.html', {'all_items': all_items})


def update(request, id):
    if request.method == "POST":
        item = List.objects.get(pk=id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        item = List.objects.get(pk=id)
        return render(request, 'update.html', {'item': item})
