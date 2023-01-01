from django.db import models

# Create your models here.
class account(models.Model):
    username =models.CharField(primary_key=True,max_length=60)
    password=models.CharField(max_length=200,null=False)
    def __str__(self):
        return f"{self.username},{self.password}"
