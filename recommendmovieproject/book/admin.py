from django.contrib import admin

# Register your models here.
from .models import Category, Product,Review,Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','image','releasedate','actor','category','link','created','updated']
    # list_editable = ['name','description']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['item','user','rating','comment','created_at']
admin.site.register(Review,ReviewAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','description']
admin.site.register(Item,ItemAdmin)


