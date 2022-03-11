from django.contrib import admin

# Register your models here.
from .models import Category, Product, Team
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
class TeamAdmin(admin.ModelAdmin):
    list_display=['name','position','is_approved']
    list_filter=['is_approved','name']
    search_fields=['name','position']

admin.site.register(Team, TeamAdmin)
admin.site.register(Product, ProductAdmin)