from django.contrib import admin
from vendor.models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display=("name","email")


admin.site.register(Vendor,VendorAdmin)  
