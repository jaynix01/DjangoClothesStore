from django.contrib import admin
from products.models import ProductCategory,Product, Basket
# Register your models here.

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity','category')
    fields = ('image','name', 'description',('price','quantity'),'category')
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    readonly_fields = ('created_timestamp',)
    fields = ('product', 'quantity','created_timestamp')
    extra = 0