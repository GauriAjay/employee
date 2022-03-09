from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Employee(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=20)
    empcode=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    desig=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='images/', default='images/user.png',null=True,blank=True)
    def __str__(self):
        return self.name

