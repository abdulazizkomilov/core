from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

class Category(models.Model):

    options = (
        ('phone', 'Phone'),
        ('laptop-fill', 'Computer'),
        ('earbuds', 'HeadPhones'),
        ('apple', 'Apple'),
        ('android2', 'Android'),
        ('bug-fill', 'Items'),
    )


    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=40 ,blank=True)
    image = models.ImageField(upload_to='bg/')
    options = models.CharField(max_length=15, choices=options)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class Product(models.Model):

    DRAFT = 'draft'
    WAITING_APPROVAL = 'waiting approval'
    ACTIVE = 'active'
    DELETED = 'deleted'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (WAITING_APPROVAL, 'Waiting approval'),
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )

    
    options_price = (
        ('discount 75', 'Discount 75%'),
        ('discount 50', 'Discount 50%'),
        ('discount 35', 'Discount 35%'),
        ('discount 10', 'Discount 10%'),
    )


    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)
    status_price = models.CharField(max_length=50, choices=options_price, default='Discount 10%')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.title)

    def get_display_price(self):
        return self.price / 100
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = ImageField(upload_to='product_image')
    

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.first_name)}"
    
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    
    def get_display_price(self):
        return self.price / 100
    
    def __str__(self):
        return f"{str(self.order)} - {str(self.product)}"
    

