from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.billing, name='billing'),
    path('billing/order', views.order, name='order'),

]
