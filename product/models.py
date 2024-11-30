from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    brand = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    supplier = models.IntegerField()
    barcode = models.CharField(max_length=100, unique=True)
    sku = models.CharField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('discontinued', 'Discontinued')])
    manufacture_date = models.DateField(blank=True)
    expiry_date = models.DateField(blank=True)

    def __str__(self):
        return self.product_name
