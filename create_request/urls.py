from rest_framework.routers import DefaultRouter
from create_request import views
from django.conf.urls import url,include

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'client_list', views.ClientList,base_name='client_list')
router.register(r'product_list', views.ProductList,base_name='product_list')
router.register(r'new_request', views.CreateRequest,base_name='new_request')


urlpatterns = [
    url(r'^', include(router.urls)),
]

