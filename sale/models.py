from django.db import models
from product.models import Product
from stock.models import StockProduct, Stock
from user.models import User
from django.db.models.deletion import PROTECT

class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=PROTECT, db_column ='user')
    product = models.ForeignKey(Product, on_delete=PROTECT, db_column='product')
    quantity = models.PositiveBigIntegerField()
    descount = models.PositiveBigIntegerField(max_length=2,blank=True, null=True)
    total = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=False,auto_now_add=True)

    class Meta:
        db_table = 'sale'

    def __str__(self) -> str:
        return '{}  - {} - {}'.format(self.pk,self.product,self.quantity,self.total)