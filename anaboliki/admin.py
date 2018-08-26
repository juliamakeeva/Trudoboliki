from django.contrib import admin
from .models import Item, City


class AdminCity(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    list_filter = ('is_approved', 'name')


admin.site.register(Item)
admin.site.register(City, AdminCity)
