from django.contrib import admin

# Register your models here.
from .models import Client, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)