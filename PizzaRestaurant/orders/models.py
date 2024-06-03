from django.db import models

PIZZA_CHOICES = [
    ('margherita', 'Margherita'),
    ('pepperoni', 'Pepperoni'),
    ('vegetarian', 'Vegetarian'),
]
class Pizza(models.Model):

    Name = models.CharField(max_length=100, choices=PIZZA_CHOICES)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.name

class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    Customer_name = models.CharField(max_length=100)
    Customer_address = models.CharField(max_length=255)
    Customer_phone = models.CharField(max_length=15)
    Quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
