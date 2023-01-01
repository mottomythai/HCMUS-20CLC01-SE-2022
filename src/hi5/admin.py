from django.contrib import admin
from .models import product


# Register your models here.
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display=('ID','name','price','description','thumbnail')
    search_fields=['name']
    list_filter=('ID','name','price')
admin.site.register(product,ProductAdmin)



# admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(Orderdetail)
# admin.site.register(Order)
# admin.site.register(Gallery)
# admin.site.register(Feedback)
