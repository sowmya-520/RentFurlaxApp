from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=10,validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    address = models.CharField(max_length=100)
    password=models.CharField(max_length=50,unique=True)
    last_logged_in = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username
    
class Category(models.Model):
    type = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.type

class Product(models.Model):
    name= models.CharField(max_length=50)
    description= models.CharField(max_length=100)
    condition= models.CharField(max_length=50)
    noofdays= models.IntegerField()
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    options= models.JSONField()
    rentaloptions= models.JSONField()

    def __str__(self):
        return self.name

class Invoice(models.Model):
    name= models.ForeignKey("Customer", on_delete=models.CASCADE) 
    products = models.ManyToManyField(Product)
    status= models.CharField(max_length=50, choices=[
        ('ORDERED','Ordered'),
        ('CANCELLED', 'Cancelled'),
        ('DELIVERED', 'Delivered'),
    ])  
    amount= models.DecimalField(max_digits=10, decimal_places=2)
