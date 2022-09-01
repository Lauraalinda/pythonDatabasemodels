from django import forms
from .models import Customer
from .models import Wallet
from .models import Currency
from .models import Account
from .models import Third_Party
from .models import Transaction
from .models import Card
from .models import Receipt
from .models import Notification
from .models import Loan
from .models import Reward

class CustomerRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = "__all__"

class WalletDetailsForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = "__all__"

class CurrencyDetailsForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = "__all__"


class AccountDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = "__all__"

class Third_PartyDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Third_Party
        fields = "__all__"

class TransactionDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Transaction
        fields = "__all__"

class CardDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Card 
        fields = "__all__"

class ReceiptDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Receipt
        fields = "__all__"

class NotificationDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Notification
        fields = "__all__"

class LoanDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Loan
        fields = "__all__"

class RewardDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Reward
        fields = "__all__"
