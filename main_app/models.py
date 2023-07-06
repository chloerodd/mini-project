from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    price = models.CharField(max_length=7)
    verified_shoe = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        
        
class Store(models.Model):

    title = models.CharField(max_length=150)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name="stores")

    def __str__(self):
        return self.title
    
    
class ShoppingCart(models.Model):
    title = models.CharField(max_length=150)
    stores =  models.ManyToManyField(Store)
    
    def __str__(self):
        return self.title