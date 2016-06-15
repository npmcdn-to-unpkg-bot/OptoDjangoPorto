from django.contrib import admin
from .models import SizeTft, ResolutionTft, BrandTft, InterfaceTft, Tft
# Register your models here.

@admin.register(SizeTft)
class SizeTftAdmin(admin.ModelAdmin):
    pass


@admin.register(ResolutionTft)
class ResolutionTftAdmin(admin.ModelAdmin):
    pass


@admin.register(BrandTft)
class BrandTftAdmin(admin.ModelAdmin):
    pass


@admin.register(InterfaceTft)
class InterfaceTftAdmin(admin.ModelAdmin):
    pass


@admin.register(Tft)
class TftAdmin(admin.ModelAdmin):
    pass