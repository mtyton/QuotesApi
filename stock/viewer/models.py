from django.db import models


# Create your models here.
class StockQuotes(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
