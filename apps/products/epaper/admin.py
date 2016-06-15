from django.contrib import admin
from .models import Epaper

# Register your models here.
@admin.register(Epaper)
class EpaperAdmin(admin.ModelAdmin):
    pass