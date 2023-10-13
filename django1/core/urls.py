from django.urls import path
from .views import index, contact, product

urlpatterns = [
    path('', index),
    path('contact', contact),
    path('product/<int:id>', product, name='product')
]