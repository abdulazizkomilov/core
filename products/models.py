from django.db import models
from users.models import CustomUser
from sorl.thumbnail import ImageField

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
    slug = models.SlugField(max_length=50)
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

    user = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.title)

    def get_display_price(self):
        return self.price / 100
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = ImageField(upload_to='product_image')
    

class Comment(models.Model):
    priduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.body)

