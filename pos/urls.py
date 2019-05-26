from django.urls import path, include
from . import views



urlpatterns = [
    path('pesanan', views.order, name='pesanan'),
    path('order', views.order, name='order'),
    path('show',views.show, name='show'),
    path('edit/<int:id>', views.edit),  
    path('edit/update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='delete'),
    path('pooder', views.pooder, name='pooder'),
    path('pshow',views.pshow, name='pshow'),
    path('pedit/<int:id>', views.pedit),  
    path('pedit/pupdate/<int:id>', views.pupdate, name='pupdate'),  
    path('pdelete/<int:id>', views.pdestroy),

]
