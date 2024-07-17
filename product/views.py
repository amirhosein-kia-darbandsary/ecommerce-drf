from rest_framework import viewsets
from rest_framework.response import Response    
from rest_framework import generics


from .models import Brand, Category, Product
from .serializers import (BrandSerializers, CategorySerializers,
                          ProductSerializers)


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.isactive() 
    
    
    
    def list(self, request):
        serializer = CategorySerializers(self.queryset, many=True)
        return Response(serializer.data)
    

class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.isactive()
    
    
    def list(self, request):
        serializer = BrandSerializers(self.queryset, many=True)
        return Response(serializer.data)
    
    
class ProductListCreateApiView(generics.ListCreateAPIView):
    # ** here we can use the manager we have build
    # queryset = Product.isactive.all().select_related("brand","category")
    
    # * we build and use a method for using after the object manager
    queryset = Product.objects.isactive().select_related("brand","category")
    
    
    serializer_class = ProductSerializers
    
class ProductDestroyUpdateRetrieveApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().select_related("brand","category")
    serializer_class = ProductSerializers
    lookup_field = "slug"
    

        
    
    
    
    
    
