from django.urls import path
from .views import TicketPurchaseView, MyTicketsView

urlpatterns = [
    path('purchase/', TicketPurchaseView.as_view(), name='ticket-purchase'),
    path('my-tickets/', MyTicketsView.as_view(), name='my-tickets'),
]
