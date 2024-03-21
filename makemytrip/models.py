from django.db import models


# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    variant = models.CharField(max_length=10, default='128gb')
    delivery = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name
