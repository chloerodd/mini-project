from django.contrib import admin
from .models import Shoe, Store, ShoppingCart

# Register your models here.
admin.site.register(Shoe)
admin.site.register(Store)
admin.site.register(ShoppingCart)

