from rest_framework import serializers
from .models import Event, TicketType

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ['id', 'name', 'price', 'quantity']


class EventSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source='seller.username')
    ticket_types = TicketTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'location', 'date',
            'time', 'price', 'total_tickets', 'status',
            'seller', 'ticket_types', 'created_at'
        ]
