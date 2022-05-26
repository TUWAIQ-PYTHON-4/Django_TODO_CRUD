from django.contrib import admin
from .models import *

# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display = ('item', 'completed')


admin.site.register(List, ListAdmin)
