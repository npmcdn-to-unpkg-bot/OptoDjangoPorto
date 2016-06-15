from django.contrib import admin
from .models import Lcd

# Register your models here.
@admin.register(Lcd)
class LcdAdmin(admin.ModelAdmin):
    pass