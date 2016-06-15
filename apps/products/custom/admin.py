from django.contrib import admin
from .models import Custom

# Register your models here.
@admin.register(Custom)
class CustomAdmin(admin.ModelAdmin):
    pass