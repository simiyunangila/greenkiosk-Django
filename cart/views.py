from django.shortcuts import render
from.forms import CartUploadForm
from .models import Cart
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

# Create your views here.
def cart_upload_view(request):
    if request.method == "POST":
        form = CartUploadForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CartUploadForm()
            
    return render(request,"Cart/cart_upload.html",{"form":form})


def cart_list(request):
    carts = Cart.objects.all()
    return render (request, "Cart/cart_list.html",{"carts":carts})


def cart_detail(request,id):
    cart = Cart.objects.get(id =id)
    return render (request, "cart/cart_detail.html",{"cart":cart})

def cart_update_view (request,id):
    cart = Cart.objects.get(id=id)
    if request.method == "POST":
        form = CartUploadForm(request.POST,instance=cart)
        if form.is_valid():
            form.save()
            return redirect("cart_detail_view",id = cart.id)
    else:
        form = CartUploadForm(instance=cart)
    return render(request,"cart/editcart.html",{"form":form}) 




def cart_delete(request, id):
    cart= get_object_or_404(Cart, id=id)

    if request.method == "POST":
        cart.delete()
        return redirect("cart_list_view")

    return render(request, "cart_delete.html", {"cart": cart})