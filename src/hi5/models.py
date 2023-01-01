from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class product(models.Model):
    ID =models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,null=False)
    price=models.IntegerField(null=True)
    description= models.CharField(max_length=300,null=True)
    thumbnail=models.CharField(max_length=400,null=True)
    def __str__(self):
        return f"{self.ID},{self.name},{self.price},{self.description},{self.thumbnail}"
