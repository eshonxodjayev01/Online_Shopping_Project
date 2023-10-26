from django.db import models
import uuid


# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name