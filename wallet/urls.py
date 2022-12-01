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
from .views import list_customers
from .views import list_walletdetails
from .views import list_currency
from .views import list_accounts
from .views import list_third_parties
from .views import list_transactions
from .views import list_cards
from .views import list_receipts
from .views import list_notifications
from .views import list_rewards
from .views import list_loans
from .views import customer_profile
from .views import wallet_profile
from .views import account_profile
from .views import edit_customer
from .views import edit_wallet
from .views import edit_thirdparty
from .views import edit_account
from .views import edit_currency
from .views import edit_transaction
# from .views import edit_card
# from .views import edit_receipt
# from .views import edit_loan
# from .views import edit_notification
# from .views import edit_reward



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
    path("rewarddetails/",register_rewarddetails, name="registration"),
    path("list/",list_customers, name ="list_customers"),
    path("listwallet/",list_walletdetails, name ="list_walletdetails"),
    path("listcurrency/",list_currency, name ="list_currency"),
    path("listaccount/",list_accounts, name ="list_accounts"),
    path("listthirdparty/",list_third_parties, name ="list_third_parties"),
    path("listtransaction/",list_transactions, name ="list_transactions"),
    path("listcard/",list_cards, name ="list_cards"),
    path("listreceipts/",list_receipts, name ="list_receipts"),
    path("listnotification/",list_notifications, name ="list_notifications"),
    path("listreward/",list_rewards, name ="list_rewards"),
    path("listloan/",list_loans, name ="list_loans"),
    path("customers/<int:id>/",customer_profile, name ="customer_profile"),
    path("wallet/<int:id>/",wallet_profile, name ="wallet_profile"),
    path("customers/edit/<int:id>/",edit_customer, name ="edit_customer"),
    path("wallet/edit/<int:id>/",edit_wallet, name ="edit_wallet"),
    path("account/edit/<int:id>/",edit_account, name ="edit_account"),
    path("thirdparty/edit/<int:id>/",edit_thirdparty, name ="edit_thirdparty"),
    path("currency/edit/<int:id>/",edit_currency, name ="edit_currency"),
    path("transaction/edit/<int:id>/",edit_transaction, name ="edit_transaction"),
    # path("card/edit/<int:id>/",edit_card, name ="edit_card"),
    # path("receipt/edit/<int:id>/",edit_receipt, name ="edit_receipt"),
    # path("loan/edit/<int:id>/",edit_loan, name ="edit_loan"),
    # path("notification/edit/<int:id>/",edit_notification, name ="edit_notification"),
    # path("reward/edit/<int:id>/",edit_reward, name ="edit_reward"),
   
   
    
]





