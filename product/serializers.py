from rest_framework import serializers
from .models import Brand, Category, Product, ProductLine


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ProductLineSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = "__all__"
        
class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializers(many=False)
    category = CategorySerializers(many=False)
    product_line = ProductLineSerialzer(many=True, read_only=True)
    
    class Meta:
        model = Product
        exclude = ['id']
    
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        brand_data = validated_data.pop('brand')

        category, created_category = Category.objects.get_or_create(**category_data)
        brand, created_brand = Brand.objects.get_or_create(**brand_data)

        product = Product.objects.create(category=category, brand=brand, **validated_data)
        return product

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        brand_data = validated_data.pop('brand')

        category, created_category = Category.objects.get_or_create(**category_data)
        brand, created_brand = Brand.objects.get_or_create(**brand_data)
        
        instance.category = category
        instance.brand = brand
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        instance.save()
        return instance
        

