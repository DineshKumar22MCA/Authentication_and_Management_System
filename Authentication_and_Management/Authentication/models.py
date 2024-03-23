from django.db import models

class Admin(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name  = models.CharField(max_length= 255)
    email_id   = models.EmailField(max_length= 255)
    user_name  = models.CharField(max_length= 255,unique=True)
    password   = models.CharField(max_length= 255)


class User(models.Model):
    id   = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age  = models.IntegerField()
    city = models.CharField(max_length=255)
    admin = models.CharField(max_length=255) 


