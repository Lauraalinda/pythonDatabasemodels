from django.contrib import admin
from .models import Account, Card, Currency, Customer, Loan_model, Notification, Receipt, Reward, Third_Party, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email",)
    search_fields=("first_name","last_name",)
    

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Third_Party)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan_model)
admin.site.register(Reward)