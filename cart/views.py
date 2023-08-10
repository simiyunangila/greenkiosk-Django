from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Cart
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def addProduct(request):
    user = request.user
    product_id = request.GET.get('product_id')
    Cart = Product.objects.get(id=id)
    Cart(user=user, product=product_cart).save()
    return render(request, "inventory/product_list.html",{"products":products})

def delete_cart_item(request):
    cart_item_id = request.GET.get('cart_item_id')
    CartItem.objects.filter(cart__user=request.user.id,id=cart_item_id)
    return render(request, your_template)
