from django.urls import path
from .views import TicketPurchaseView, MyTicketsView, SellerSoldTicketsView

urlpatterns = [
    path('purchase/', TicketPurchaseView.as_view(), name='ticket-purchase'),
    path('my-tickets/', MyTicketsView.as_view(), name='my-tickets'),
    path('sold/', SellerSoldTicketsView.as_view(), name='seller-sold-tickets'),
]
