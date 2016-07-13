from django.contrib import admin
from .models import Partner, BusinessArea
# Register your models here.


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass


@admin.register(BusinessArea)
class BusinessAreaAdmin(admin.ModelAdmin):
    pass
