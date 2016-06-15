from django.contrib import admin
from .models import Oled

# Register your models here.
@admin.register(Oled)
class OledAdmin(admin.ModelAdmin):
    pass