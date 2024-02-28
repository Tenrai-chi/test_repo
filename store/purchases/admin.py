from django.contrib import admin

from .models import Item, Order, OrderItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'user', 'description', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'session_id', 'date_created', 'updated', 'paid')
    list_display_links = ('id',)
    search_fields = ('id',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'item', 'quantity')
    list_display_links = ('id', 'order')
    search_fields = ('id', 'order', 'item')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
