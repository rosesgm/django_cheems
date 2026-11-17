from django.db import models

class Ticket(models.Model):

    PRIORITY_CHOICES = [
        ("alta", "Alta"),
        ("media", "Media"),
        ("baja", "Baja"),
    ]
    STATUS_CHOICES = [
        ("abierto", "Abierto"),
        ("en_progreso", "En progreso"),
        ("cerrado", "Cerrado"),
    ]
    title = models.CharField(max_length=150)
    description = models.TextField()
    priority=models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status=models.CharField(max_length=15, choices=STATUS_CHOICES, default="abierto")
    created_at = models.DateTimeField(auto_now_add=True)