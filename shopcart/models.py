from django.db import models
import uuid
import datetime
from customer.models import Customer
from product.models import Product, Category
# Create your models here.
class Shopcard(models.Model):
    PAYMANT_CHOICS = (
        ('Payme,', 'Paymedan'),
        ('Click', 'Clickdan'),
        ('Uzum', 'Uzumdan'),
        ('Cash', 'Naqd pul'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    date = models.DateTimeField(auto_now_add=datetime.datetime.now())
    product = models.ManyToManyField(Product, related_name='Product', blank=True)
    owner = models.ForeignKey(Customer, related_name="Customer", on_delete=models.CASCADE)
    payment = models.CharField(max_length=10, choices=PAYMANT_CHOICS, default="CARD")

    def __str__(self) -> str:
        return self.owner.name

    def get_total_price(self):
        product: Product
        a = 0
        for product in self.product.all():
            a += product.price
        return a

