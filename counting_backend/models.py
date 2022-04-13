from re import T
from django.db import models

# Create your models here.
class consume(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_category = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)

class eating(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)

class drinking(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)
    
class taxing(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)

class traffic(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)
class utility_bill(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)

class clothes(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)

class phonefee(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)


class health(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)


class sport(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)


class beauth(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)


class gift(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)
class social(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)


class stock(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)


class save_money(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateTimeField(primary_key=True)