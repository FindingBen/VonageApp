from django.db import models
import uuid

class Sms(models.Model):
    unique_tracking_id = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255, default='Test 1')
    phone_number = models.CharField(max_length=255)
    text_body = models.TextField()
    is_sent = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    not_delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.name