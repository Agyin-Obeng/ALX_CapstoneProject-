from rest_framework import generics, permissions
from .models import Event, TicketType
from .serializers import EventSerializer, TicketTypeSerializer
from .permissions import IsSeller, IsOwner

# List & Create Events
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


# Retrieve, Update, Delete Event
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


# Update Event Status
class EventStatusUpdateView(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


# Create Ticket Type
class TicketTypeCreateView(generics.CreateAPIView):
    serializer_class = TicketTypeSerializer
    permission_classes = [permissions.IsAuthenticated, IsSeller]

    def perform_create(self, serializer):
        event_id = self.kwargs['event_id']
        serializer.save(event_id=event_id)


# List Ticket Types for Event
class TicketTypeListView(generics.ListAPIView):
    serializer_class = TicketTypeSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return TicketType.objects.filter(event_id=event_id)


# Ticket Type Detail (update/delete)
class TicketTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer
    permission_classes = [permissions.IsAuthenticated, IsSeller]
