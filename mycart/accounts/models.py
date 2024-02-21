from django.db import models

# Create your models here.
class customer(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.EmailField()
    phone_no=models.IntegerField()
    address=models.CharField(max_length=100)
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)


class vender(models.Model):
    vender_name=models.CharField(max_length=50)
    shop_name=models.CharField(max_length=50)
    shop_address=models.CharField(max_length=50)
    shop_licence=models.ImageField(blank=True,upload_to='licence')
    email=models.EmailField()
    vender_phno=models.IntegerField()
    pawd1=models.CharField(max_length=50)
    pswd2=models.CharField(max_length=50)
    is_approved=models.BooleanField(default=False)