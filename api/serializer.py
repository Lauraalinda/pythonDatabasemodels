from django.db import models
from rest_framework import serializers
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

class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Customer
        fields =("first_name","email","age","gender","address","nationality","id_number","phone_number","email","profile_picture","marital_status","signature","employment_status")

class WalletSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Wallet
        fields =("balance","customer","pin","currency","active","datecreated")

class CurrencySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Currency
        fields =("symbol","name","country")
 
class AccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        fields =("account_type","account_name","wallet")
 
class Third_PartySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Third_Party
        fields =( "full_name","email","phone_number","transaction_cost","currency","account","status")

class TransactionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Transaction
        fields =( "transaction_type","account_origin","account_destination","third_party","datetime","status")

class CardSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Card
        fields =("date_issued","card_status","security_code","signature","issuer","account")

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Receipt
        fields =( "date","transaction","receipt_file")

class AccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        fields =("account_type","account_name","wallet")

class NotificationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Notification
        fields =( "datecreated","message","status","image")

class LoanSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Loan
        fields =("loan_type","amount","wallet","datetime","loan_terms","payment_due_date","guaranter","balance","duration","interest_rate","balance","status")
 
class RewardSerializer(serializers.ModelSerializer):
    class Meta: 
        model =  Reward
        fields =( "wallet","points","date","transaction")
 
 
 