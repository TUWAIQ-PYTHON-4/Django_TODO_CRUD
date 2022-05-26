from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

def home(request):
    if request.method == "POST":
        form = ItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            context = Item.objects.all()
            return render(request,"home.html",{"context":context})
    else:
        context = Item.objects.all()
        return render(request,"home.html",{"context":context})

def delete(request, Item_id):
    item = Item.objects.get(id=Item_id)
    item.delete()
    return redirect('home')

def edit(request, Item_id):
    if request.method == "POST":
        item = Item.objects.get(id=Item_id)
        form = ItemForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        item = Item.objects.get(id=Item_id)
    return render(request,"edit.html",{'item': item})

def about(request):
    fname = 'Adnan'
    lname = 'Abo Assoud'
    return render(request,"about.html",{'fname':fname,'lname':lname})

# Create your views here.
