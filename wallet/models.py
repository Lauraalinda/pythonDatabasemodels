from datetime import date, datetime
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=15, blank =True)
    last_name=models.CharField(max_length=15, blank =True)
    gender=models.CharField(max_length=1, blank =True)
    address=models.TextField()
    age=models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=15, blank =True)
    id_number=models.CharField(max_length=15, blank =True)
    phone_number=models.CharField(max_length=15, blank =True)
    email=models.EmailField()
    profile_picture=models.ImageField(default= False)
    marital_status=models.CharField(max_length=15, blank =True)
    signature=models.ImageField(default= False)
    employment_status=models.CharField(max_length=20,default= False)

class Wallet (models.Model):
    balance=models.IntegerField(blank=True) 
    customer=models.OneToOneField(Customer,on_delete= models.CASCADE)
    pin=models.SmallIntegerField(blank=True)
    currency=models.CharField(max_length=10,blank=True)
    active=models.BooleanField()
    datecreated=models.DateTimeField()

class Currency(models.Model):
    symbol=models.CharField(max_length=10,blank=True)
    name=models.CharField(max_length=15,blank=True)
    country=models.CharField(max_length=15,blank=True)
    
class Account(models.Model):
    account_type=models.CharField(max_length=20,blank=True)
    account_name=models.ForeignKey(Customer,on_delete=models.CASCADE)
    wallet=models.ForeignKey(Wallet,on_delete= models.CASCADE)
    
class Third_Party(models.Model):
    full_name=models.CharField(max_length=20,blank=True)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20,blank=True)
    transaction_cost=models.IntegerField(blank=True)
    currency=models.CharField(max_length=20)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    status=models.BooleanField()

class Transaction(models.Model):
    transaction_type=models.CharField(max_length=15,blank=True)
    account_origin=models.ForeignKey(Account, related_name='account_destination',on_delete=models.CASCADE,null=True, blank=True)
    account_destination=models.ForeignKey(Account, related_name='account_origin',on_delete=models.CASCADE,null=True, blank=True)
    third_party=models.ForeignKey(Third_Party,on_delete= models.CASCADE)
    datetime=models.DateTimeField()
    status=models.BooleanField()

class Card(models.Model):
    date_issued=models.DateTimeField(blank=True)
    card_status=models.BooleanField()
    security_code=models.PositiveSmallIntegerField(blank=True)
    signature=models.ImageField()
    issuer=models.CharField(max_length=20)
    account=models.ForeignKey(Account,models.CASCADE,blank=True)

class Receipt(models.Model):
    date=models.DateTimeField(blank=True)
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,blank=True)
    receipt_file=models.FileField(blank=True)

class Notification(models.Model):
    datecreated=models.DateField(blank=True)
    message=models.CharField(max_length=40,blank=True)
    status=models.BooleanField()
    image=models.ImageField()

class Loan(models.Model):
    loan_type=models.CharField(max_length=15,blank=True) 
    amount=models.IntegerField(blank=True)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    datetime=models.DateTimeField()
    loan_terms=models.CharField(max_length=120,blank=True)
    payment_due_date=models.DateField()
    guaranter=models.CharField(max_length=20,blank=True)
    balance=models.IntegerField()
    duration=models.CharField(max_length=15,default=True)
    interest_rate=models.IntegerField()
    balance=models.IntegerField()
    status=models.BooleanField(default=True)

class Reward(models.Model):
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    points=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE)