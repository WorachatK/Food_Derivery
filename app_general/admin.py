from django.contrib import admin
from .models import *

# Register your models here.

class DesignPost_food(admin.ModelAdmin):
    list_display = ["name","type","price"]
    search_fields = ['name',]

class DesignPost_order_food(admin.ModelAdmin):
    list_display = ["username","phonenumber"]
    search_fields = ['username']    

class DesignPost_check_food(admin.ModelAdmin):
    list_display = ["username","food","time"]
    search_fields = ['username']        

admin.site.register(food,DesignPost_food)
admin.site.register(type_food)
admin.site.register(order_food,DesignPost_order_food)
admin.site.register(check_food,DesignPost_check_food)
