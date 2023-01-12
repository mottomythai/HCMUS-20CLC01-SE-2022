from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    ID =models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200, null=False)
    def __str__(self) -> str:
        return f"{self.ID}, {self.name}"

class product(models.Model):
    ID =models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=False)
    price=models.IntegerField(null=True)
    thumbnail=models.CharField(max_length=400,null=True)
    itemno =models.CharField(max_length=50,null=True)
    description= models.CharField(max_length=500,null=True)
    categoryid = models.ForeignKey(category,null=True, on_delete=models.SET_NULL)
    thumbnail2=models.CharField(max_length=500,null=True)
    thumbnail3=models.CharField(max_length=500,null=True)
    thumbnail4=models.CharField(max_length=500,null=True)
    thumbnail5=models.CharField(max_length=500,null=True)
    def __str__(self):
        return f"{self.ID},{self.name},{self.price},{self.thumbnail},{self.itemno},{self.description},{self.thumbnail2},{self.thumbnail3},{self.thumbnail4},{self.thumbnail5}"


        
# class color(models.Model):
#     name = models.CharField(max_length=200)
#     code = models.CharField(max_length=50)
#     def __str__(self) -> str:
#         return f"{self.name}, {self.code}"

class productdetail(models.Model):
    ID =models.AutoField(primary_key=True)
    productid = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=200,null=False)
    size = models.CharField(max_length=10,null=False)
    
    def __str__(self):
        return f"{self.productid.name},{self.color}, {self.size}"


class Order(models.Model):
    items = models.ManyToManyField(product)

    # def get_cart_items(self):
    #     return self.items.all()

    # def get_cart_total(self):
    #     return sum([item.product.price for item in self.items.all()])
