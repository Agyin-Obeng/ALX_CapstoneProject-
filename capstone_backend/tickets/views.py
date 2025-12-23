from rest_framework import generics, permissions
from .models import Ticket
from .serializers import TicketSerializer
from events.models import TicketType


# BUY TICKET
class TicketPurchaseView(generics.CreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        if user.role not in ['buyer', 'both']:
            raise PermissionError("Only buyers can purchase tickets")

        ticket_type_id = self.request.data.get('ticket_type')
        ticket_type = TicketType.objects.get(id=ticket_type_id)

        if ticket_type.quantity <= 0:
            raise PermissionError("Tickets sold out")

        # Reduce ticket count
        ticket_type.quantity -= 1
        ticket_type.save()

        serializer.save(
            buyer=user,
            event=ticket_type.event,
            ticket_type=ticket_type
        )


# BUYER DASHBOARD
class MyTicketsView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(buyer=self.request.user)
