from django.contrib import admin
from django.urls import path

from purchases.views import (view_all_items, item_info, buy_item, success, cancel,
                             add_item_order, view_order, buy_order)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_all_items, name='view_all_items'),
    path('view_order/', view_order, name='view_order'),
    path('buy_order/', buy_order, name='buy_order'),
    path('buy/<int:item_id>/', buy_item, name='buy_item'),
    path('item/<int:item_id>/', item_info, name='item_info'),
    path('success/<str:session_key>', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('add/<int:item_id>/', add_item_order, name='add_item_order'),
]
