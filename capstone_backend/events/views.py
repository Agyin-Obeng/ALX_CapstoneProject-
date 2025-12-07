from rest_framework import generics, permissions
from .models import Event, TicketType
from .serializers import EventSerializer, TicketTypeSerializer
from .permissions import IsSeller, IsOwner

# List all events (public) and create new events (sellers only)
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.role not in ['seller', 'both']:
            raise PermissionError("Only sellers can create events")
        serializer.save(seller=self.request.user)

# Retrieve, update, delete an event
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

# Update event status
class EventStatusUpdateView(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

# Ticket Types
class TicketTypeCreateView(generics.CreateAPIView):
    serializer_class = TicketTypeSerializer
    permission_classes = [permissions.IsAuthenticated, IsSeller]

    def perform_create(self, serializer):
        event_id = self.kwargs['event_id']
        serializer.save(event_id=event_id)

class TicketTypeListView(generics.ListAPIView):
    serializer_class = TicketTypeSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return TicketType.objects.filter(event_id=event_id)

class TicketTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer
    permission_classes = [permissions.IsAuthenticated, IsSeller]
