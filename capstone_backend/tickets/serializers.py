from rest_framework import serializers
from .models import Ticket
from events.models import TicketType
import uuid


class TicketSerializer(serializers.ModelSerializer):
    event_title = serializers.ReadOnlyField(source='event.title')
    ticket_type_name = serializers.ReadOnlyField(source='ticket_type.name')
    buyer = serializers.ReadOnlyField(source='buyer.username')

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


class TicketPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['ticket_type']

    def validate(self, data):
        ticket_type = data['ticket_type']

        if ticket_type.quantity <= 0:
            raise serializers.ValidationError("Tickets are sold out.")

        return data

    def create(self, validated_data):
        ticket_type = validated_data['ticket_type']
        user = self.context['request'].user

        # Reduce available tickets
        ticket_type.quantity -= 1
        ticket_type.save()

        ticket = Ticket.objects.create(
            event=ticket_type.event,
            ticket_type=ticket_type,
            buyer=user,
            ticket_code=str(uuid.uuid4())
        )

        return ticket
