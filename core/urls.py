from django.urls import path
from .views import index, contact, product

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact),
    path('product/<int:pk>', product, name='product')
]