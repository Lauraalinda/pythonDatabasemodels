from rest_framework import viewsets
from wallet.models import Customer
from wallet.models import Wallet
from wallet.models import Currency
from wallet.models import Account
from wallet.models import Third_Party
from wallet.models import Transaction
from wallet.models import Card
from wallet.models import Receipt
from wallet.models import Notification
from wallet.models import Loan
from wallet.models import Reward 
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .serializer import CustomerSerializer
from .serializer import WalletSerializer
from .serializer import CurrencySerializer
from .serializer import AccountSerializer
from .serializer import Third_PartySerializer
from .serializer import TransactionSerializer
from .serializer import CardSerializer
from .serializer import ReceiptSerializer
from .serializer import NotificationSerializer
from .serializer import LoanSerializer
from .serializer import RewardSerializer


class CustomerViewSet (viewsets.ModelViewSet):
    queryset =Customer.objects.all()
    serializer_class=CustomerSerializer
    

class WalletViewSet (viewsets.ModelViewSet):
    queryset =Wallet.objects.all()
    serializer_class=WalletSerializer

class CurrencyViewSet (viewsets.ModelViewSet):
    queryset =Currency.objects.all()
    serializer_class=CurrencySerializer

class AccountViewSet (viewsets.ModelViewSet):
    queryset =Account.objects.all()
    serializer_class=AccountSerializer

class Third_PartyViewSet (viewsets.ModelViewSet):
    queryset =Third_Party.objects.all()
    serializer_class=Third_PartySerializer

class TransactionViewSet (viewsets.ModelViewSet):
    queryset =Transaction.objects.all()
    serializer_class=TransactionSerializer

class CardViewSet (viewsets.ModelViewSet):
    queryset =Card.objects.all()
    serializer_class=CardSerializer

class ReceiptViewSet (viewsets.ModelViewSet):
    queryset =Receipt.objects.all()
    serializer_class=ReceiptSerializer

class NotificationViewSet (viewsets.ModelViewSet):
    queryset =Notification.objects.all()
    serializer_class=NotificationSerializer

class LoanViewSet (viewsets.ModelViewSet):
    queryset =Loan.objects.all()
    serializer_class=LoanSerializer

class RewardViewSet (viewsets.ModelViewSet):
    queryset =Reward.objects.all()
    serializer_class=RewardSerializer

class AccountDepositView(views.APIView):
    def post(self, request, format=None):       
        account_id = request.data["account_id"]
        amount = request.data["amount"]
        try:
            account = Account.objects.get(id=account_id)
        except ObjectDoesNotExist:
            return Response("Account Not Found", status=404)
    
        message, status = account.deposit(amount)
        return Response(message, status=status)
        
class AccountTransferView(views.APIView):
    def post(self, request, format=None):       
        account_id = request.data["account_id"]
        amount = request.data["amount"]
        try:
            account = Account.objects.get(id=account_id)
        except ObjectDoesNotExist:
            return Response("Account Not Found", status=404)
       
        message, status = account.transfer(amount)
        return Response(message, status=status)

class AccountWithdrawView(views.APIView):
    def post(self, request, format=None):
        account_id = request.data["account_id"]
        amount = request.data["amount"]
        try:
            account = Account.objects.get(id = account_id)
        except ObjectDoesNotExist:
            return Response("Account Not Found", status=404)

        message, status = account.withdraw(amount)
        return Response(message, status=status)

class AccountRequest_loanView(views.APIView):
    def post(self, request, format=None):
        account_id = request.data["account_id"]
        amount = request.data["amount"]
        try:
            account = Account.objects.get(id = account_id)
        except ObjectDoesNotExist:
            return Response("Account Not Found", status=404)
        message, status = account.request_loan(amount)
        return Response(message, status=status)

class AccountRepay_loanView(views.APIView):
    def post(self, request, format=None):
        account_id = request.data["account_id"]
        amount = request.data["amount"]
        try:
            account = Account.objects.get(id = account_id)
        except ObjectDoesNotExist:
            return Response("Account Not Found", status=404)
        message, status = account.request_loan(amount)
        return Response(message, status=status)


class  AccountBuyAirtimeView(views.APIView):
    def post(self, request, format=None):
        account_id = request.data["account_id"]
        amount = request.data["amount"]
        try:
            account = Account.objects.get(id = account_id)
        except ObjectDoesNotExist:
            return Response("Account Not Found", status=404)
        message, status = account.buy_airtime((amount)
        return Response(message, status=status)