from django.db import models

class Staff(models.Model):
    Name = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Email = models.EmailField()

    def __str__(self):
        return self.name
