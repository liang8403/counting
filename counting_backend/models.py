from re import T
from django.db import models

# Create your models here.
class consume(models.Model):
    consume_item = models.CharField(max_length=50,blank=True,null=True)
    consume_price = models.CharField(max_length=50,blank=True,null=True)
    consume_category = models.CharField(max_length=50,blank=True,null=True)
    consume_date = models.DateField(blank=True,null=True)