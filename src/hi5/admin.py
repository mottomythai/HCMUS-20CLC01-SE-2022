from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Category)


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Orderdetail)
admin.site.register(Order)
admin.site.register(Gallery)
admin.site.register(Feedback)
