from django.db import models
from orders.models import Pizza

class Review(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.pizza.name} by {self.reviewer_name}"
