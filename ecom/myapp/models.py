from django.db import models
from django.contrib.auth.models import AbstractUser
from .helpers import Manager
from django.utils.text import slugify
# Create your models here.

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=100)
#     address = models.TextField()
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = Manager()
    
#     def __str__(self) -> str:
#         return self.email
    
class Category(models.Model):
    cat_name = models.CharField(max_length=100) # laptop , #mobile 
    is_active = models.BooleanField(default = True)
    
    def __str__(self):
        return self.cat_name
class Company(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=True) # laptop
    company_name = models.CharField(max_length=100) #hp
    is_active = models.BooleanField(default = True) #true
    
    def __str__(self):
        return self.comp_name

class Product(models.Model):
    
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cateogry') #laptop
    comp_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company') # hp
    product_name = models.CharField(max_length=100) #Hp Probook 440
    product_description = models.TextField()
    orignal_price = models.PositiveIntegerField(default = 0)
    discount_percentage = models.PositiveIntegerField(default = 0)
    discounted_price = models.PositiveIntegerField(default = 0)
    warranty = models.IntegerField(default = 1)
    product_image = models.ImageField(upload_to = 'product_images/')
    is_stock = models.BooleanField(default = True)
    is_active = models.BooleanField(default = True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    
    def discounted_price(self):
        
        discount_amount = (float(self.discount_percentage) / 100) * float(self.orignal_price) #( 10/100) * 1000
        discounted_price = float(self.orignal_price) - discount_amount
        formatted_discounted_price = "{:.2f}".format(round(discounted_price, 2))
        return formatted_discounted_price

    def formatted_price(self):
        return "{:.2f}".format(self.orignal_price)

    def save(self, *args, **kwargs):
        #this line below give to the instance slug field a slug name
        self.slug = slugify(self.product_name)
        #this line below save every fields of the model instance
        super(Product, self).save(*args, **kwargs)    
    
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.email

class FeatureProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feature_product_image') #Iphone 6s
    image = models.ImageField(upload_to = 'product_images/') 
    
    def __str__(self):
        return self.product.product_name

class ProductDescription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prod_description')
    feature = models.CharField(max_length = 100)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to = 'product_images/')
    
    def __str__(self) -> str:
        return self.product.product_name

class AdditionalInformation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='additional_information')
    feature = models.CharField(max_length = 100)
    product_description1 = models.TextField()
    product_description2 = models.TextField()
    product_image = models.ImageField(upload_to = 'product_images/')
    
    def __str__(self) -> str:
        return self.product.product_name

class StayInTouch(models.Model):
    email = models.EmailField(max_length=100)
    
# class Cart(models.Model):

#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_cart')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_cart')
#     quantity = models.PositiveIntegerField(default = 1)
#     is_ordered = models.BooleanField(default = False)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

#     def __str__(self):
#         return self.user.email

# class ShippingAddress(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     comapny = models.CharField(max_length=100)
#     area_code = models.CharField(max_length=100)
#     primary_phone = models.CharField(max_length=100)
#     street_address = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=100)
    