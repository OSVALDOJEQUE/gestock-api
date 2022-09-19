from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.
class Category(models.Model):
    name =models.CharField(max_length=100, unique=True)
    code =models.CharField(max_length=45, unique=True, blank=True, null=True)
    description=models.TextField(max_length=255,blank=True, null=True)
    
    class Meta:
        db_table ='category'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=PROTECT,db_column='category')
    description = models.CharField(max_length=255,blank=True, null=True)
    code = models.CharField(max_length=45, unique=True,blank=True, null=True)
    # iva = models.PositiveBigIntegerField(max_length=2,blank=True,null=True)
    # descount = models.PositiveBigIntegerField(max_length=2, blank=True, null=True)
    price =models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table='product'

    def __str__(self):
        return self.name
