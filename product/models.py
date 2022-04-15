from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name    = models.CharField(max_length=50)
    details = models.TextField()
    price   = models.DecimalField(max_digits=1000, decimal_places=2)
    date    = models.DateTimeField(auto_now_add=True)
    stock   = models.IntegerField(default=1)
    image   = models.ImageField(upload_to='img/')
    seller  = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.name
        