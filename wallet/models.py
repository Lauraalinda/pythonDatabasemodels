from datetime import datetime
from email import message
from email.policy import EmailPolicy
from platform import mac_ver
from statistics import mode
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
    employment_status=models.BooleanField(default= False)
    

class Wallets (models.Model):
    balance=models.IntegerField(blank=True) 
    customer=models.OneToOneField(Customer,on_delete=   models.CASCADE  )
    pin=models.SmallIntegerField(max_length=8,blank=True)
    # currency=models.ForeignKey(max_length=15,blank=True)
    active=models.BooleanField()
    datecreated=models.DateTimeField()
    type=models.CharField(max_length=10)

# class Account(models.Model):
    # account_type=models.CharField()
    # account_name=models.CharField()
    # savings=models.IntegerField()
    # wallet=models.ForeignKey()
    


# class Transaction(models.Model):
    # transaction_type=models.CharField(max_length=15)
    # account_origin=models.ForeignKey()
    # destination=models.ForeignKey()
    # third_party=models.ForeignKey()
    # datetime=models.ForeignKey()
    # reciept=models.CharField()
    # status=models.CharField()

# class Card(models.Model):
    # date_issued=models.DateTimeField()
    # card_status=models.CharField(max_length=10)
    # security_code=models.PositiveSmallIntegerField()
    # signature=models.ImageField()
    # issuer=models.CharField()
    # account=models.ForeignKey()
# 
# class Third_Party(models.Model):
    # full_name=models.CharField()
    # email=models.EmailField()
    # phone_number=models.CharField()
    # transaction_cost=models.IntegerField()
    # currency=models.ForeignKey()
    # account=models.ForeignKey()
    # status=models.BooleanField(max_length=8)

# class Notifications(models.Model):
    # datecreated=models.DateField()
    # message=models.CharField(max_length=40)
    # receipt=models.ForeignKey(max_length=40)
    # status=models.ForeignKey(max_length=8)
    # image=models.ImageField()
# 
# class Reciept(models.Model):
    # date=models.DateTimeField()
    # transaction=models.ForeignKey()
    # reciept_file=models.FileField()
# 
# class Loan_model(models.Model):
    # loan_type=models.CharField(max_length=15) 
    # amount=models.IntegerField()
    # wallet=models.ForeignKey()
    # datetime=models.DateField()
    # loan_terms=models.CharField(max_length=120)
    # payment_due_date=models.DateField()
    # guaranter=models.CharField(max_length=20)
    # balance=models.IntegerField()
    # duration=models.CharField(max_length=15)
    # interest_rate=models.IntegerField()
    # balance=models.IntegerField()
    # status=models.ForeignKey(max_length=8)
# 
# class Reward(models.Model):
    # wallet=models.ForeignKey()
    # points=models.IntegerField()
    # date=models.IntegerField()
    # transaction=models.ForeignKey()