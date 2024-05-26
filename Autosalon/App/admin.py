from django.contrib import admin
from .models import Cars, Category
# Register your models here.
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'colors', 'speed', 'category')


admin.site.register(Category)
