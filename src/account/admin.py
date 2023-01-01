from django.contrib import admin
from .models import account

class AccoutAdmin(admin.ModelAdmin):
    list_display=('username','password')
    search_fields=['username']
    list_filter=('username','password')
admin.site.register(account,AccoutAdmin)
# Register your models here.
