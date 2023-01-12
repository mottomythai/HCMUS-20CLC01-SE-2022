from django.contrib import admin


# Register your models here.
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display=('ID','name','price','thumbnail','itemno','description','thumbnail2','thumbnail3','thumbnail4','thumbnail5')
    search_fields=['name']
    list_filter=('ID','name','price')
admin.site.register(product,ProductAdmin)

class ProductDetailAdmin(admin.ModelAdmin):
    list_display=('ID','productid','color','size')
    search_fields=['color,size']
    list_filter=('ID','productid','color','size')
    
admin.site.register(productdetail,ProductDetailAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('ID','name')
    search_fields=['name']
    list_filter=('ID','name')
admin.site.register(category,CategoryAdmin)

admin.site.register(Order)


# admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(Orderdetail)
# admin.site.register(Order)
# admin.site.register(Gallery)
# admin.site.register(Feedback)
