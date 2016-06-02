from django.contrib import admin
from .models import Tft

# Register your models here.
@admin.register(Tft)
class TftAdmin(admin.ModelAdmin):
    pass