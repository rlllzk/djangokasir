from django.contrib import admin
from .models import Product, Order, OrderItem, Karyawan


admin.site.site_header = 'POS Administration'
admin.site.site_title = 'POS Administration'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','stok')


class KaryawanAdmin(admin.ModelAdmin):
    list_display = ('identity', 'name','tugas')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','nomor','karyawan','total_price','success','timestamp', 'meja','namapemesan','status')
    list_filter = ('karyawan', 'timestamp')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'timestamp', 'product')
    list_filter = ('order', 'timestamp')



admin.site.register(Karyawan, KaryawanAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
