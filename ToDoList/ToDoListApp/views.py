from django.shortcuts import render
from . import models
from .forms import ExampleForm
# Create your views here.
def home(request):
    if request.method == "POST":
        form = ExampleForm(request.POST or None)
        form.save()
        all_items=models.List.objects.all()
        return render(request, "home.html", {"method": request.method, "all_items": all_items})
    else:
        all_items = models.List.objects.all()
        return render(request, "home.html", {"method": request.method, "all_items": all_items})







def about(request):
    return render(request, "about.html")







