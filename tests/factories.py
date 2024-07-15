import factory
from product.models import Brand, Category, Product


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
    
    name = "test_str_method_pro"
    description = "test_description"
    is_digital = True
    
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)