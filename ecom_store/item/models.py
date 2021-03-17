from django.db import models
from django.db.models import F, Q, CheckConstraint
from django.contrib.auth.models import User

from django.utils import timezone
from django.utils.text import slugify

from .exceptions import ProductAlreadyInActiveDeal


class Attributes(models.Model):
    """Attributes name"""
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductAttributes(models.Model):
    """Product attribute and value"""
    name = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    value = models.CharField(max_length=50, blank=False, null=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='attributes')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name}({self.name.name}: {self.value})"


class Category(models.Model):
    """Product category"""
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField()
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)


class ProductImage(models.Model):
    """Images set for a particular product"""
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField()


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail_image = models.ImageField()
    description = models.TextField()
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Review(models.Model):
    """User review for a product"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    rating = models.IntegerField(max_length=1)


class Deal(models.Model):
    title = models.CharField(max_length=100)
    end_date = models.DateTimeField()
    start_date = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(end_date__gt=F('start_date')), name='check_end_date',
            ),
        ]

    def __str__(self):
        return self.title


class DealProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.product} in {self.deal}"

    def save(self, *args, **kwargs):
        """Check if same product in different active deals"""
        if DealProduct.objects.filter(product=self.product, deal__end_date__gt=timezone.now()).exists():
            raise ProductAlreadyInActiveDeal("Product already in active deal.")
        return super(DealProduct, self).save(*args, **kwargs)
