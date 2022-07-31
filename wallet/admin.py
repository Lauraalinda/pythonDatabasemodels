from django.contrib import admin
from .models import Customer,Wallets

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email",)
    search_fields=("first_name","last_name",)
    

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallets)