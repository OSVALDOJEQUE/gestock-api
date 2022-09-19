from itertools import product
from django.db import models
from django.db.models.deletion import PROTECT
from user.models import User
from product.models import Product

MOVIMENT = (
    ('e','entrada'),
    ('s','saida'),
)

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=False,auto_now_add=True)


    class Meta:
        abstract = True

class Stock(TimeStampedModel):
    user =models.ForeignKey(User,on_delete=PROTECT,db_column='user')
    code =models.CharField(max_length=45,null=True,blank=True)
    movement =models.CharField(max_length=1, choices=MOVIMENT)
    

    class Meta:
       db_table= 'stock'

    def __str__(self):
        return str(self.pk)


class StockProduct(models.Model):
    stock = models.ForeignKey(Stock,on_delete=PROTECT,db_column='stock')
    product = models.ForeignKey(Product,on_delete=PROTECT,db_column='product')
    quantity = models.PositiveBigIntegerField()
    balance = models.PositiveBigIntegerField()


    class Meta:
       db_table = 'stock_product'
    def __str__(self):
        return '{} - {} - {}'.format(self.pk,self.stock.pk,self.product)




    

