from django.urls import path
from .views import register_customer
from .views import register_walletdetails
from .views import register_currencydetails
from .views import register_accountdetails
from .views import register_thirdpartydetails
from .views import register_transactiondetails
from .views import register_carddetails
from .views import register_receiptdetails
from .views import register_notificationdetails
from .views import register_loandetails
from .views import register_rewarddetails


urlpatterns = [
    path("register/",register_customer, name="registration"),
    path("walletdetails/",register_walletdetails, name="registration"),
    path("currencydetails/",register_currencydetails, name="registration"),
    path("accountdetails/",register_accountdetails, name="registration"),
    path("thirdpartydetails/",register_thirdpartydetails, name="registration"),
    path("transactiondetails/",register_transactiondetails, name="registration"),
    path("carddetails/",register_carddetails, name="registration"),
    path("receiptdetails/",register_receiptdetails, name="registration"),
    path("notificationdetails/",register_notificationdetails, name="registration"),
    path("loandetails/",register_loandetails, name="registration"),
    path("rewarddetails/",register_rewarddetails, name="registration")


    
]





