# Create your models here.
from django.contrib import admin
from .models import account

class AccoutAdmin(admin.ModelAdmin):
    list_display=('userid','username','name','phone','address')
    search_fields=['userid','username']
    list_filter=('userid','username')
admin.site.register(account,AccoutAdmin)
# Register your models here.