from django import forms  
from .models import Order, Product

class OrderForm(forms.ModelForm):  
	class Meta:  
		model = Order  
		fields = "__all__"   	

class ProductForm(forms.ModelForm):  
	class Meta:  
		model = Product  
		fields = "__all__"   	

