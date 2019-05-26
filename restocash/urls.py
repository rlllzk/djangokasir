
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
    path('pos/', include('pos.urls')),
    path('accounts/profile/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    path('', include('django.contrib.auth.urls')),
     
]