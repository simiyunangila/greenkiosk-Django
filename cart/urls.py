from django.urls import path
from .views import delete_cart_item
from .views import addProduct




urlpatterns = [
    path("products/upload/",delete_cart_item,name = "delete_cart_item"),
    path("cart/addproduct/",addProduct,name = "addProduct"),
    
]