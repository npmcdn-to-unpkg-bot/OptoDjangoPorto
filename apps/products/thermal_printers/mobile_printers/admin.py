from django.contrib import admin
from .models import Mobile_printers

# Register your models here.
@admin.register(Mobile_printers)
class Mobile_printersAdmin(admin.ModelAdmin):
    pass