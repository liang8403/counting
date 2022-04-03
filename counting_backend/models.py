from re import T
from django.db import models

# Create your models here.
class consume(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_category = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)

class eating(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)

class drinking(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)
    
class taxing(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)

class traffic(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)
class utility_bill(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)

class clothes(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)

class phonefee(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)


class health(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)


class sport(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)


class beauth(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)


class gift(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)
class social(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)


class stock(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)


class save_money(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)