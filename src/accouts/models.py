from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class account(models.Model):
    userid =models.AutoField(primary_key=True)
    username =models.OneToOneField(User,default=None, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, null=False) 
    phone=models.CharField(max_length=12, null=False) 
    address=models.CharField(max_length=200, null=False) 
    profile_pic=models.ImageField(null=True,blank=True)
    def __str__(self):
        return f"{self.userid},{self.username},{self.name},{self.phone},{self.address}"
