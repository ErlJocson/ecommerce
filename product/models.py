from django.db import models

class Product(models.Model):
    name    = models.CharField(max_length=50)
    details = models.TextField()
    price   = models.DecimalField(max_digits=1000, decimal_places=2)
    date    = models.DateTimeField(auto_now_add=True)
    stock   = models.IntegerField()
    image   = models.ImageField()

    def __str__(self):
        return self.name