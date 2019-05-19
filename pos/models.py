from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    STOKCEK = (
        ('READY','ready'),
        ('NOTREADY','notready')
    )
    stok = models.CharField(max_length=9, choices=STOKCEK)
    class Meta:
        db_table = "Product"
    def __str__(self):
        return self.name


class Karyawan(models.Model):
    TUGASJOB = (
        ('KASIR','kasir'),
        ('PELAYAN','pelayan')
    )
    identity = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    tugas = models.CharField(max_length=8, choices=TUGASJOB)
    class Meta:
        db_table = "Karyawan"
    def __str__(self):
        return self.name

class Order(models.Model):
    nomor = models.CharField(max_length=25) #ERPtlgblntahun-nomer ERP10102017-001 
    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    namapemesan = models.CharField(max_length=30)
    meja = models.CharField(max_length=10) 
    STATPS = (
        ('AKTIF','aktif'),
        ('NONAKTIF','nonaktif')
    )
    status = models.CharField(max_length=10, choices=STATPS)
    class Meta:
        db_table = "Order"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "OrderItem"
    def __int__(self):
        return self.id





