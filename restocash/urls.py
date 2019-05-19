"""restocash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from rest_framework import routers
from pos import views

router = routers.DefaultRouter()
router.register('', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pos.urls')),
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
    path('accounts/profile/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    path('', include('django.contrib.auth.urls')), 
]