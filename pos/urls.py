from django.urls import path, include
from . import views



urlpatterns = [
    path('pos/', views.billing, name='billing'),
    path('billing/order', views.order, name='order'),
    path('ooder', views.ooder),
    path('show',views.show, name='show'),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy),
    path('pooder', views.pooder, name='pooder'),
    path('pshow',views.pshow, name='pshow'),
    path('pedit/<int:id>', views.pedit),  
    path('pupdate/<int:id>', views.pupdate, name='pupdate'),  
    path('pdelete/<int:id>', views.pdestroy),

]
