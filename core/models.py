from django.db import models

class Property(models.Model):
    RENT_TYPE_CHOICES = [
        ('rent', 'Rent'),
        ('lease', 'Lease'),
        ('buy', 'Buy'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('shop', 'Shop'),
    ]

    name = models.CharField(max_length=200)
    rent_type = models.CharField(max_length=10, choices=RENT_TYPE_CHOICES)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    rent_price = models.DecimalField(max_digits=12, decimal_places=2)
    deposit = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    area = models.PositiveIntegerField(blank=True, null=True)
    location = models.TextField()
    description = models.TextField()

    image = models.ImageField(upload_to='properties/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
