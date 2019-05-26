from django import forms  
from .models import Order, Product, OrderItem

class OrderForm(forms.ModelForm):  
	class Meta:  
		model = Order  
		fields = "__all__"   	

class ProductForm(forms.ModelForm):  
	class Meta:  
		model = Product  
		fields = "__all__"  

class OrderItemForm(forms.ModelForm):  
	class Meta:  
		model = OrderItem 
		fields = "__all__"  	

