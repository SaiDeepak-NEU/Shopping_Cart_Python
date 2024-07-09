from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_product, name='add_product'),
    path('items', views.get_products, name='get_products'),
]
