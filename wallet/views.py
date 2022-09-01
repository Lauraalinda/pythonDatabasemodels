from django.shortcuts import render
from .forms import CustomerRegistrationForm
from .forms import WalletDetailsForm
from .forms import CurrencyDetailsForm
from .forms import AccountDetailsForm
from .forms import Third_PartyDetailsForm
from .forms import TransactionDetailsForm
from .forms import CardDetailsForm
from .forms import ReceiptDetailsForm
from .forms import NotificationDetailsForm
from .forms import LoanDetailsForm
from .forms import RewardDetailsForm


# Create your views here.
def register_customer(request):
     form= CustomerRegistrationForm()
     return render(request,"wallet/register_customer.html", {"form": form})

def register_walletdetails(request):
     form= WalletDetailsForm()
     return render(request,"wallet/register_walletdetails.html",{"form": form})

def register_currencydetails(request):
     form= CurrencyDetailsForm()
     return render(request,"wallet/register_currencydetails.html",{"form": form})

def register_accountdetails(request):
     form = AccountDetailsForm()
     return render(request,"wallet/register_accountdetails.html",{"form": form})

def register_thirdpartydetails(request):
     form = Third_PartyDetailsForm()
     return render(request,"wallet/register_thirdpartydetails.html",{"form": form})

def register_transactiondetails(request):
     form = TransactionDetailsForm()
     return render(request,"wallet/register_transactiondetails.html",{"form": form})

def register_carddetails(request):
     form = CardDetailsForm()
     return render(request,"wallet/register_carddetails.html",{"form": form})

def register_receiptdetails(request):
     form = ReceiptDetailsForm()
     return render(request,"wallet/register_receiptdetails.html",{"form": form})

def register_notificationdetails(request):
     form = NotificationDetailsForm()
     return render(request,"wallet/register_notificationdetails.html",{"form": form})

def register_loandetails(request):
     form = LoanDetailsForm()
     return render(request,"wallet/register_loandetails.html",{"form": form})

def register_rewarddetails(request):
     form = RewardDetailsForm()
     return render(request,"wallet/register_rewarddetails.html",{"form": form})