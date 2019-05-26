from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    STOKCEK = (
        ('1','ready'),
        ('0','notready')
    )
    stok = models.CharField(max_length=9, choices=STOKCEK)
    class Meta:
        db_table = "Product"
    def __str__(self):
        return self.name

class Order(models.Model):
    def increment_invoice_number():
        last_invoice = Order.objects.all().order_by('nomor').last()
        if not last_invoice:
            return 'ERP0001'
        nomor = last_invoice.nomor
        # value = datetime.date.today()
        # today = timezone.now().date()  
        invoice_int = int(nomor.split('ERP')[-1])
        width = 4
        new_invoice_int = invoice_int + 1
        formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
        new_invoice_no = 'ERP' + str(formatted) 
        return new_invoice_no

    nomor = models.CharField(max_length=30, default=increment_invoice_number) #ERPtlgblntahun-nomer ERP10102017-001 
    operator = models.CharField(max_length=30)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    customer = models.CharField(max_length=30)
    meja = models.CharField(max_length=3) 
    STATPS = (
        ('1','aktif'),
        ('0','nonaktif')
    )
    status = models.CharField(max_length=10, choices=STATPS)
    class Meta:
        db_table = "Order"
    def __str__(self):
        return self.nomor



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "OrderItem"
    def __int__(self):
        return self.order





