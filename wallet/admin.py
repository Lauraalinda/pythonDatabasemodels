from django.contrib import admin
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Third_Party, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email",)
    search_fields=("first_name","last_name",)
    
class WalletAdmin(admin.ModelAdmin):
    list_display=("balance","customer","pin","currency","active","datecreated")
    search_fields=("customer",)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("symbol","name","country",)
    search_fields=("customer",)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_type","account_name","wallet",)
    search_fields=("customer",)

class Third_PartyAdmin(admin.ModelAdmin):
    list_display=("full_name","email","phone_number","transaction_cost","currency","account","status")
    search_fields=("customer",)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_type","account_origin","account_destination","third_party","datetime","status",)
    search_fields=("customer",)

class CardAdmin(admin.ModelAdmin):
    list_display=("date_issued","card_status","signature","issuer","account",)
    search_fields=("customer",)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("datecreated","message","status","image",)
    search_fields=("customer",)

class RecieptAdmin(admin.ModelAdmin):
    list_display=("date","transaction","receipt_file",)
    search_fields=("customer",)

class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_type","amount","wallet","datetime","loan_terms")
    search_fields=("customer",)
    
class RewardAdmin(admin.ModelAdmin):
    list_display=("wallet","points","transaction",)
    search_fields=("customer",)

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Third_Party,Third_PartyAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Receipt,RecieptAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Reward,RewardAdmin)