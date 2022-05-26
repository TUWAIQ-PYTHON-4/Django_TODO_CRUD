from django.shortcuts import render, redirect
from .forms import Form
from .models import Item

def home(request):
    if request.method == "POST":
        form = Form(request.POST or None)
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
        form = Form(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        item = Item.objects.get(id=Item_id)
    return render(request,"edit.html",{'item': item})

def edit_date(request, Date_id):
    if request.method == "POST":
        date_created = Item.objects.get(id=Date_id)
        form = Form(request.POST or None, instance=date_created)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        date_created = Item.objects.get(id=Date_id)
    return render(request,"edit_date.html",{'date_created':date_created})
def about(request):
    fname = 'Ruba'
    lname = 'ALmohya'
    context ={'fname':fname,'lname':lname}
    return render(request,"about.html",context)