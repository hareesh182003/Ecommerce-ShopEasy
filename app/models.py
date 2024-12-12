from django.db import models
from django.contrib.auth.models import User
from django.core import validators
# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User,on_delete= models.CASCADE) 
    address = models.TextField()
    profile_pic = models.ImageField()
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    mobile = models.CharField(max_length=10,validators=[validators.MinLengthValidator(10),validators.RegexValidator('^[6-9]\d{9}')],null=True)

    def __str__(self) -> str:
        return str(self.username)

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=60)
    product_description = models.TextField()
    product_prize = models.DecimalField(max_digits=10,decimal_places=2)
    
    

    def __str__(self):
        return self.product_name
