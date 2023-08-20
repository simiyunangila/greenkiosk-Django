from django.shortcuts import render
from.forms import OrderUploadForm
from .models import Order
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

# Create your views here.
def order_upload_view(request):
    if request.method == "POST":
        form = OrderUploadForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = OrderUploadForm()
            
    return render(request,"order/order_upload.html",{"form":form})


def order_list(request):
    orders = Order.objects.all()
    return render (request, "order/order_list.html",{" orders": orders})


def  order_detail(request,id):
    order =  Order.objects.get(id =id)
    return render (request, "order/order_detail.html",{" order": order})

def  order_update_view (request,id):
    order =  Order.objects.get(id=id)
    if request.method == "POST":
        form = OrderUploadForm(request.POST,instance= order)
        if form.is_valid():
            form.save()
            return redirect(" order_detail_view",id =  order.id)
    else:
        form = OrderUploadForm(instance= order)
    return render(request,"order/edit_order.html",{"form":form}) 




def  order_delete(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == "POST":
        order.delete()
        return redirect(" order_list_view")

    return render(request, " order_delete.html", {" order":  order})