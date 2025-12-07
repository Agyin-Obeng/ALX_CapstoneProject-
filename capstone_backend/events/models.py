from django.db import models
from django.conf import settings

class Event(models.Model):
    STATUS_CHOICES = (
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_tickets = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')

    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="events",
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.seller.username})"


class TicketType(models.Model):
    event = models.ForeignKey(Event, related_name="ticket_types", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # e.g., VIP, Regular
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.event.title}"
