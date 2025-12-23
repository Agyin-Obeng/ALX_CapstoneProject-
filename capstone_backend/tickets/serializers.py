from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    event_title = serializers.ReadOnlyField(source='event.title')
    ticket_type_name = serializers.ReadOnlyField(source='ticket_type.name')

    class Meta:
        model = Ticket
        fields = [
            'id',
            'event',
            'event_title',
            'ticket_type',
            'ticket_type_name',
            'buyer',
            'purchase_date',
            'ticket_code'
        ]
        read_only_fields = ['buyer', 'purchase_date', 'ticket_code']
