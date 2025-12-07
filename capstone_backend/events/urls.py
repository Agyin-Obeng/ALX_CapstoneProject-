from django.urls import path
from .views import (
    EventListCreateView, EventDetailView, EventStatusUpdateView,
    TicketTypeCreateView, TicketTypeListView, TicketTypeDetailView
)

urlpatterns = [
    path('', EventListCreateView.as_view(), name='events'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('<int:pk>/status/', EventStatusUpdateView.as_view(), name='event-status'),

    # Ticket Types
    path('<int:event_id>/ticket-types/', TicketTypeListView.as_view(), name='ticket-types'),
    path('<int:event_id>/ticket-types/create/', TicketTypeCreateView.as_view(), name='ticket-type-create'),
    path('ticket-types/<int:pk>/', TicketTypeDetailView.as_view(), name='ticket-type-detail'),
]
