from rest_framework import generics, permissions
from .models import Ticket
from .serializers import TicketSerializer, TicketPurchaseSerializer


class TicketPurchaseView(generics.CreateAPIView):
    serializer_class = TicketPurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]


class MyTicketsView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(buyer=self.request.user)


class SellerSoldTicketsView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(event__seller=self.request.user)
