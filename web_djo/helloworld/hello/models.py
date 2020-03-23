from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)

class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()

class user(models.Model):
    name=models.CharField(max_length=30)
    password=models.IntegerField()

class User_admin(models.Model):
    user_name = models.CharField(max_length=30,
                                 primary_key=True)   # 设置为主键
    psw = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)