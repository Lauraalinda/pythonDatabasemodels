from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet
from .views import WalletViewSet
from .views import CurrencyViewSet
from .views import AccountViewSet
from .views import Third_PartyViewSet
from .views import TransactionViewSet
from .views import CardViewSet
from .views import ReceiptViewSet
from .views import NotificationViewSet
from .views import LoanViewSet
from .views import RewardViewSet
from .views import AccountDepositView
from .views import AccountTransferView
from .views import AccountWithdrawView
from .views import AccountWithdrawView
from .views import AccountWithdrawView
from .views import AccountWithdrawView
from .views import AccountWithdrawView


router =routers.DefaultRouter()
router.register(r"customers", CustomerViewSet) 
router.register(r"wallets", WalletViewSet) 
router.register(r"currencies", CurrencyViewSet) 
router.register(r"accounts", AccountViewSet) 
router.register(r"thirdparties", Third_PartyViewSet) 
router.register(r"transactions", TransactionViewSet) 
router.register(r"cards", CardViewSet) 
router.register(r"receipts", ReceiptViewSet) 
router.register(r"notifications", NotificationViewSet) 
router.register(r"loans", LoanViewSet) 
router.register(r"rewards", RewardViewSet) 

urlpatterns = [
    path('',include(router.urls)), 
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
    path("transfer/", AccountTransferView.as_view(), name="transfer-view"),
    path("withdraw/", AccountWithdrawView.as_view(), name="withdraw-view"),
    path("withdraw/", AccountWithdrawView.as_view(), name="withdraw-view"),
    path("withdraw/", AccountWithdrawView.as_view(), name="withdraw-view"),
    path("withdraw/", AccountWithdrawView.as_view(), name="withdraw-view"),
    
]