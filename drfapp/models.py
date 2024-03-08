from django.db import models

# Create your models here.
class Mobile(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    specs = models.TextField()
    discount = models.BooleanField(null=True)
    launch_date = models.DateTimeField(auto_now=True)
    
    def __self__(self):
        return self.brand