from django.contrib import admin
from . models import Stock,StockProduct

class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 0

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = (StockProductInline,)
    list_display = ('__str__','code',)
    search_fields =('code',)
    list_filter =('user',)
    date_hierarchy = 'created'
