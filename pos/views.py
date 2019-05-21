from django.shortcuts import render, redirect
import json
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product, Karyawan, Order, OrderItem
from .forms import OrderForm, ProductForm


def billing(request):
    if request.method == 'GET':
        return render(request, 'billing.html')
    else:
        nik = request.POST.get('karyawanID', None)
        karyawan = Karyawan.objects.get(pk=nik)
        products = list(Product.objects.filter(stok='READY'))
        
    
        return render(request, 'billing_details.html', {'karyawan': karyawan, 'products': products, })

def order(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        print(data)
        karyawan = Karyawan.objects.get(pk=data['karyawan_id']) 
      
        
        
        order = Order.objects.create(    
                                    karyawan=karyawan,      
                                    nomor=data['nomorid'],
                                    namapemesan=data['customerid'],
                                    meja=data['mejaid'],
                                    status=data['statusid'],                    
                                    total_price=data['total_price'],
                                    success=False
                                    )
        for product_id in data['product_ids']:
            OrderItem(product=Product.objects.get(pk=product_id), order=order).save()
    
           
     
            # karyawan.save()
        

            order.success = True
        order.save()
        return render(request, 'order.html', {'success' : order.success})
#=============crudtrasnksi
def show(request):  
    orders = Order.objects.all()  
    return render(request,"show.html",{'orders':orders})

def edit(request, id):  
    order = Order.objects.get(id=id)  
    return render(request,'edit.html', {'order':order})

def update(request, id):  
    order = Order.objects.get(id=id)  
    form = OrderForm(request.POST, instance = order)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'order': order})  
def destroy(request, id):  
    order = Order.objects.get(id=id)  
    order.delete()  
    return redirect("/show")  
def ooder(request):  
    if request.method == "POST":  
        form = OrderForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = OrderForm()  
    return render(request,'ooder.html',{'form':form}) 

#==========api-

class ProductViewSet(viewsets.ModelViewSet):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer

#=========productcrud
def pshow(request):  
    Products = Product.objects.all()  
    return render(request,"pshow.html",{'Products':Products})

def pedit(request, id):  
    produk= Product.objects.get(id=id)  
    return render(request,'pedit.html', {'produk':produk})

def pupdate(request, id):  
    produk = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = produk)  
    if form.is_valid():  
        form.save()  
        return redirect("/pshow")  
    return render(request, 'pedit.html', {'produk': produk})

def pdestroy(request, id):  
    produk = Product.objects.get(id=id)  
    produk.delete()  
    return redirect("/pshow")  
def pooder(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/pshow')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'pooder.html',{'form':form}) 