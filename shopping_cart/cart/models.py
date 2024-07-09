from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, error_messages={'blank': 'Name is mandatory'})
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], error_messages={'blank': 'Price is mandatory'})
    quantity = models.IntegerField(validators=[MinValueValidator(1)], error_messages={'blank': 'Quantity is mandatory'})

    def __str__(self):
        return self.name

    def clean(self):
       super().clean()
       if self.price <= 0:
           raise ValidationError({'price': 'Price must be greater than zero.'})
       if self.quantity < 0:
           raise ValidationError({'quantity': 'Quantity must be zero or greater.'})
