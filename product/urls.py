from django.urls import path
from product.views import ProductListCreateApiView,ProductDestroyUpdateRetrieveApiView
urlpatterns = [
    path('', ProductListCreateApiView.as_view()),
    path('<slug:slug>', ProductDestroyUpdateRetrieveApiView.as_view())
]
