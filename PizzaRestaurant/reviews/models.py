from django.db import models
from orders.models import Pizza

class Review(models.Model):
    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    Reviewer_name = models.CharField(max_length=100)
    Rating = models.PositiveIntegerField()
    Comment = models.TextField()

    def __str__(self):
        return f"Review for {self.pizza.name} by {self.reviewer_name}"
