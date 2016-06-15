from django.contrib import admin
from .models import Panel_printers

# Register your models here.
@admin.register(Panel_printers)
class TftAdmin(admin.ModelAdmin):
    pass