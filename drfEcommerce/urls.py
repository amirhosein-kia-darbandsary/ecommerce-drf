from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from product import views

router = DefaultRouter()
router.register("category",views.CategoryViewSet)
router.register("brand",views.BrandViewSet)
router.register("product",views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls))
]
