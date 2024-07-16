import factory
from product.models import Brand, Category, Product, ProductLine
from django.utils.text import slugify

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
        
    name = "test_str_method_cat"
    
    
class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
        
    
    name = "test_str_method_bra"
    

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    name = factory.Sequence(lambda n: f'Product {n}')
    slug = factory.Sequence(lambda n: f'product-{n}')
    description = "test_description"
    is_digital = True
    
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    is_active = True
    
class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine
        
    price = 99.99
    sku = factory.Sequence(lambda n: f'12345{n}')
    stock_qt = 100
    is_active = True
    product = factory.SubFactory(ProductFactory)
    ordering = factory.Sequence(lambda n: n)
        
    