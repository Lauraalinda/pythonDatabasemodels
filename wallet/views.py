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
from  django.shortcuts import redirect


# Create your views here.
def register_customer(request):
     if request.method == "POST":
          form = CustomerRegistrationForm(request.POST)
          if form.is_valid():
             form.save()
     else:
          form= CustomerRegistrationForm()
     return render(request,"wallet/register_customer.html", {"form": form})

def register_walletdetails(request):
     if request.method == "POST":
          form = WalletDetailsForm(request.POST)
          if form.is_valid():
             form.save()
     else:
          form= WalletDetailsForm()
     return render(request,"wallet/register_walletdetails.html",{"form": form})

def register_currencydetails(request):
     if request.method == "POST" :
          form =  CurrencyDetailsForm(request.POST)
          if form.is_valid():
             form.save()
     else:
          form= CurrencyDetailsForm()
     return render(request,"wallet/register_currencydetails.html",{"form": form})

def register_accountdetails(request):
     if request.method == "POST" :
        form = AccountDetailsForm(request.POST)
        if form.is_valid():
           form.save()
     else:
          form = AccountDetailsForm()
     return render(request,"wallet/register_accountdetails.html",{"form": form})

def register_thirdpartydetails(request):
     if request.method == "POST":
          form = Third_PartyDetailsForm(request.POST)
          if form.is_valid():
             form.save()
     else:
          form = Third_PartyDetailsForm()
     return render(request,"wallet/register_thirdpartydetails.html",{"form": form})

def register_transactiondetails(request):
     if request.method == "POST":
          form = TransactionDetailsForm(request.POST)
          if form.is_valid():
             form.save()
     else:
        form = TransactionDetailsForm()
     return render(request,"wallet/register_transactiondetails.html",{"form": form})

def register_carddetails(request):
     if request.method == "POST":
          form = TransactionDetailsForm(request.POST)
          if form.is_valid():
             form.save()
     else:
        form = CardDetailsForm()
     return render(request,"wallet/register_carddetails.html",{"form": form})

def register_receiptdetails(request):
     if request.method == "POST":
          form = ReceiptDetailsForm (request.POST)
          if form.is_valid():
             form.save()
     else:
        form = ReceiptDetailsForm()
     return render(request,"wallet/register_receiptdetails.html",{"form": form})

def register_notificationdetails(request):
     if request.method == "POST":
          form = NotificationDetailsForm(request.POST)
          if form.is_valid():
             form.save()
     else:
        form = NotificationDetailsForm()
     return render(request,"wallet/register_notificationdetails.html",{"form": form})

def register_loandetails(request):
     if request.method == "POST":
          form = LoanDetailsForm(request.POST)
          if form.is_valid():
             form.save()
     else:
        form = LoanDetailsForm()
     return render(request,"wallet/register_loandetails.html",{"form": form})

def register_rewarddetails(request):
     if request.method == "POST":
          form = RewardDetailsForm(request.POST)
          if form.is_valid():
             form.save()
     else:
        form = RewardDetailsForm()
     return render(request,"wallet/register_rewarddetails.html",{"form": form})

def list_customers(request):
     customers = Customer.objects.all()
     return render (request, "wallet/customers_list.html", {"customers":customers})

def list_walletdetails(request):
     wallets = Wallet.objects.all()
     return render (request, "wallet/walletdetails_list.html", {"wallets":wallets})

def list_currency(request):
     currencies = Currency.objects.all()
     return render (request,"wallet/currency_list.html",{"currencies":currencies})

def list_accounts(request):
     accounts = Account.objects.all()
     return render (request,"wallet/account_list.html",{"accounts":accounts})

def list_third_parties(request):
     third_parties = Third_Party.objects.all()
     return render (request,"wallet/thirdparty_list.html",{"third_parties":third_parties})

def list_transactions(request):
     transactions = Transaction.objects.all()
     return render (request,"wallet/transaction_list.html",{"transactions":transactions})

def list_cards(request):
     cards = Card.objects.all()
     return render (request,"wallet/card_list.html",{"cards":cards})

def list_receipts(request):
     receipts = Receipt.objects.all()
     return render (request,"wallet/receipt_list.html",{"receipts":receipts})

def list_notifications(request):
     notifications = Notification.objects.all()
     return render (request,"wallet/notification_list.html",{"notifications":notifications})

def list_loans(request):
     loans = Loan.objects.all()
     return render (request,"wallet/loan_list.html",{"loans":loans})

def list_rewards(request):
     rewards = Reward.objects.all()
     return render (request,"wallet/reward_list.html",{"rewards":rewards})

def  customer_profile(request, id): 
     customer = Customer.objects.get(id = id)
     return render ( request, "wallet/customer_profile.html", {"customer":customer})

def edit_customer(request,id): 
     customer= Customer.objects.get(id = id)
     if request.method =="POST":
        form = CustomerRegistrationForm (request.POST, instance=customer)
        form.is_valid()
        form.save()
        return redirect("customer_profile", id=customer.id)
           
     else :
        form = CustomerRegistrationForm(instance=customer) 
        return render(request, "wallet/edit_profile.html", {"form": form})
           