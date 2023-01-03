from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
    ID =models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200, null=False)
    def __str__(self) -> str:
        return f"{self.ID}, {self.name}"
        
# class color(models.Model):
#     name = models.CharField(max_length=200)
#     code = models.CharField(max_length=50)
#     def __str__(self) -> str:
#         return f"{self.name}, {self.code}"

class product(models.Model):
    ID =models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,null=False)
    price=models.IntegerField(null=True)
    description= models.CharField(max_length=300,null=True)
    thumbnail=models.CharField(max_length=400,null=True)
    categoryid = models.ForeignKey(category,null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.ID},{self.name}, {self.categoryid},{self.price},{self.description},{self.thumbnail}"


class productdetail(models.Model):
    ID =models.AutoField(primary_key=True)
    productid = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=200,null=False)
    size = models.CharField(max_length=10,null=False)
    def __str__(self):
        return f"{self.productid.name},{self.color}, {self.size}"