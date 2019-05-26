from django.contrib import admin
from .models import Product, Order, OrderItem


admin.site.site_header = 'POS SYSTEM'
admin.site.site_title = 'POS SYSTEM'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','stok')


class KaryawanAdmin(admin.ModelAdmin):
    list_display = ('identity', 'name','tugas')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','nomor','operator','total_price','success','timestamp', 'meja','customer','status')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'timestamp', 'product')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
