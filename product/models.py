from django.db import models
from django.utils.text import slugify
from django.db.models import Max
from mptt.models import MPTTModel, TreeForeignKey


class ActiveManager(models.Manager):
    # ** for using the first builder
    # def get_queryset(self) -> models.QuerySet:
    #     return super().get_queryset().filter(is_active=True)
    
    # * we build a method for using it after the queryset
    def isactive(self):
        return self.filter(is_active=True)
    
class Category(MPTTModel):
    name = models.CharField(max_length=120)
    parent = TreeForeignKey('self',on_delete=models.PROTECT,
                                null=True,
                                blank=True)
    is_active = models.BooleanField(default=True)
    
    objects = ActiveManager()
    
    def __str__(self) -> str:
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    
    objects = ActiveManager()
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False) 
    slug = models.SlugField(max_length=120,unique=True,blank=True,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="products")
    category = TreeForeignKey(Category, on_delete=models.SET_NULL,
                                null=True,
                                related_name="products",
                                blank=True)
    is_active = models.BooleanField(default=False)
   
    # ** Build the direct object manager 
    # objects = models.Manager()
    # isactive = ActiveManager()
    # * Build an just a method for using in the manager
    objects = ActiveManager()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
        
    def __str__(self) -> str:
        return self.name
    
class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2,max_digits=5)
    sku = models.CharField(max_length=120)
    stock_qt = models.IntegerField()
    is_active = models.BooleanField(default=False)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="product_line")
    ordering = models.PositiveIntegerField(default=0,
                                           unique=True)
    
    
    def __str__(self):
        return self.sku
            
    