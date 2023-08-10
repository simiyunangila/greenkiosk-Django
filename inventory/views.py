from django.shortcuts import render
from.forms import ProductUploadForm
from .models import Product
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

# Create your views here.
def product_upload_view(request):
    if request.method == "POST":
        form = ProductUploadForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ProductUploadForm()
            
    return render(request,"inventory/product_upload.html",{"form":form})


def product_list(request):
    products = Product.objects.all()
    return render (request, "inventory/product_list.html",{"products":products})


def product_detail(request,id):
    product = Product.objects.get(id =id)
    return render (request, "inventory/product_detail.html",{"product":product})

def product_update_view (request,id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductUploadForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view",id = product.id)
    else:
        form = ProductUploadForm(instance=product)
    return render(request,"inventory/editproduct.html",{"form":form}) 




def product_delete(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect("product_list_view")

    return render(request, "product_delete.html", {"product": product})