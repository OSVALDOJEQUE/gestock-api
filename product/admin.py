from django.contrib import admin
from .models import Category,Product

admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        '__str__','price','code','description',
    )
    search_fields = ('name',)