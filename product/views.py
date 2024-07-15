from rest_framework import viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import (BrandSerializers, CategorySerializers,
                          ProductSerializers)


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all() 
    
    
    
    def list(self, request):
        serializer = CategorySerializers(self.queryset, many=True)
        return Response(serializer.data)
    

class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()
    
    
    def list(self, request):
        serializer = BrandSerializers(self.queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    
    
    def list(self, request):
        serializer = ProductSerializers(self.queryset, many=True)
        return Response(serializer.data)
        
    
    
    
    
    
