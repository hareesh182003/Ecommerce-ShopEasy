from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.urls import reverse
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
    product_brand_name = models.CharField(max_length=50,null=True)
    product_name = models.CharField(max_length=60)
    product_description = models.TextField()
    product_prize = models.DecimalField(max_digits=10,decimal_places=2)
    product_feature_description = models.TextField(null=True)
    product_model_number = models.CharField(max_length=50,null=True)
    product_dimensions = models.CharField(max_length=50,null=True)
    product_image = models.ImageField(null=True)


    def get_absolute_url(self):
        return reverse('cart',kwargs={'pk':self.pk})
        

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cartItems')
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10,decimal_places=2,null=True)

    def save(self, *args, **kwargs):
        # Calculate total before saving
        self.total = self.quantity * self.products.product_prize
        super(Cart, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.username)
