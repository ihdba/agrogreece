from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone






# Create your models here.
class Producer(models.Model):
    
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    contact = models.CharField(max_length=255)
    image = models.ImageField(upload_to='producers/', default='producers/farmer2.jpeg')
    registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Producers"
        ordering = ['-registered']



class Product(models.Model):
    p_name = models.CharField(max_length=255)
    p_desc = models.TextField()  
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    p_img = models.ImageField(upload_to='images/products/', default='/images/olive-oil.jpg')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.p_name}"

    class Meta:
        verbose_name_plural = "Products"
        ordering = ['-published']
        
        
    def get_absolute_url(self):
        return reverse("products:product_detail", args=[self.id])
    