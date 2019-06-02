from django.shortcuts import render, redirect
import json
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product, Order, OrderItem
from .forms import OrderForm, ProductForm, OrderItemForm
from django.contrib.auth.decorators import login_required



@login_required
def order(request):
    form = OrderItemForm()
    products = list(Product.objects.filter(stok='1'))
    if request.method == 'GET':
        return render(request, 'pesanan.html', {'products': products, 'form':form })
        
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        print(data)
  
        order = Order.objects.create(    
                                    operator=data['userid'],      
                                    customer=data['customerid'],
                                    meja=data['mejaid'],
                                    status=data['statusid'],                    
                                    total_price=data['total_price'],
                                    success=False
                                    )
        for product_id in data['product_ids']:
            OrderItem(product=Product.objects.get(pk=product_id), order=order).save()
   
            order.success = True
        order.save()
        return render(request, 'order.html', {'success' : order.success})

@login_required
def show(request):  
    orders = Order.objects.all()  
    return render(request,"show.html",{'orders':orders})
@login_required
def edit(request, id):  
    order = Order.objects.get(id=id) 
    return render(request,'edit.html', {'order':order})
@login_required
def update(request, id):  
    order = Order.objects.get(id=id)  
    form = OrderForm(request.POST, instance = order)  
    if form.is_valid():  
        form.save()  
        return redirect("show")  
    return render(request, 'edit.html', {'order': order})  
@login_required
def destroy(request, id):  
    order = Order.objects.get(id=id)  
    order.delete()  
    return redirect("show")  


class ProductViewSet(viewsets.ModelViewSet):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer


@login_required
def pshow(request):  
    Products = Product.objects.all()  
    return render(request,"pshow.html",{'Products':Products})
@login_required
def pedit(request, id):  
    produk= Product.objects.get(id=id) 
    return render(request,'pedit.html', {'produk':produk})
@login_required
def pupdate(request, id):  
    produk = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = produk)  
    if form.is_valid():  
        form.save()  
        return redirect("pshow")  
    return render(request, 'pedit.html', {'produk': produk})
@login_required
def pdestroy(request, id):  
    produk = Product.objects.get(id=id)  
    produk.delete()  
    return redirect("pshow")
@login_required  
def pooder(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('pshow')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'pooder.html',{'form':form}) 
