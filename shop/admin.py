from django.contrib import admin
from .models import *

class CatagoryAdmin(admin.ModelAdmin):
     list_display=('name','image','description')
class ProductAdmin(admin.ModelAdmin):
     list_display=('name','Catagory','quantity')
admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart)

# Register your models here.
