from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    # id = models.CharField(max_length = 10,primary_key=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 150)
    phonenumber = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200)
    def __str__(self) -> str:
        return  (self.fullname)

class Category(models.Model):
    id = models.CharField(max_length = 10,primary_key=True)
    name_category = models.CharField(max_length = 20, null=False)
    def __str__(self) -> str:
        return (self.id + "-" + self.name_category)

class Product(models.Model):
    id = models.CharField(max_length = 10,primary_key=True)
    categoryid = models.ForeignKey(Category,null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length = 350)
    price = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    thumbnail = models.CharField(max_length = 500)
    # thumbnail = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True)
    createdat = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return (self.id + "-" + self.title)
    
    """
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    """

class Gallery(models.Model):
    id = models.CharField(max_length = 10,primary_key=True)
    productid = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    thumbnail = models.CharField(max_length = 1000, null = False)
    def __str__(self) -> str:
        return (self.id)


class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    id = models.CharField(max_length = 10,primary_key=True)
    userid = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length = 200)
    note = models.CharField(max_length = 1000)
    orderdate = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50,null=True,choices=STATUS)
    totalmoney = models.FloatField()
    
    def __str__(self) -> str:
        return (self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderdetail_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderdetail_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class Feedback(models.Model):
    userid = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    feedback = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.userid.fullname + '- ' + self.orderid.id
    class Meta:
        unique_together = ('userid', 'orderid')

class Orderdetail(models.Model):
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    productid = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('productid', 'orderid')

    def __str__(self) -> str:
        return (self.orderid.id +"-"+ self.productid.id)

    @property
    def get_total(self):
        total = self.productid.price * self.quantity
        return total

