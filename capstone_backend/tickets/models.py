from django.db import models
from users.models import User
from events.models import Event, TicketType
import uuid

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    purchase_date = models.DateTimeField(auto_now_add=True)
    ticket_code = models.CharField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.ticket_code:
            self.ticket_code = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.event.title} - {self.buyer.username}"
