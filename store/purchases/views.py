import stripe

from django.conf import settings
from django.db.models import F
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Item, Order, OrderItem


def view_all_items(request):
    """ Просмотр всего ассортимента
    """

    items = Item.objects.all()
    context = {'items': items}

    return render(request, 'purchases/view_all_items.html', context)


def item_info(request, item_id):
    """ Просмотр информации о товаре
    """

    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}

    return render(request, 'purchases/item_info.html', context)


def success(request, session_key):
    """ Страница после успешного платежа
    """

    order = Order.objects.filter(session_id=session_key, paid=False).last()
    order.paid = True
    order.save()

    return render(request, 'purchases/success.html')


def cancel(request):
    """ Страница после неудачного платежа
    """

    return render(request, 'purchases/cancel.html')


def buy_item(request, item_id):
    """ Покупка пользователем товара
    """

    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

    item = Item.objects.get(pk=item_id)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price*100,  # unit_amount используется в центах
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel', )

    return redirect(session.url, code=303)


def add_item_order(request, item_id):
    """ Добавляет предмет в корзину
    """

    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key

    try:
        order = Order.objects.get(session_id=session_key, paid=False)

    except Order.DoesNotExist:
        order = Order.objects.create(session_id=session_key)

    item = get_object_or_404(Item, id=item_id)

    try:
        item_in_order = OrderItem.objects.get(order=order, item=item)
        item_in_order.quantity += 1
        item_in_order.save()

    except OrderItem.DoesNotExist:

        OrderItem.objects.create(order=order, item=item)

    return HttpResponseRedirect(reverse('view_all_items'))


def view_order(request):
    """ Выводит страницу с корзиной
    """

    session_key = request.session.session_key

    order = order = Order.objects.filter(session_id=session_key, paid=False).last()
    if order:
        items_in_order = OrderItem.objects.filter(order=order)
        #order_price = OrderItem.objects.filter(order=order).annotate(order_price=F('item__price')*F('quantity'))
        order_price = 0
        for item in items_in_order:
            order_price += item.item.price * item.quantity

        context = {'items_in_order': items_in_order,
                   'order_price': order_price}
    else:
        context = {}

    return render(request, 'purchases/view_order.html', context)


def buy_order(request):
    """ Покупка заказа
    """

    session_key = request.session.session_key
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

    order = Order.objects.get(session_id=session_key, paid=False)
    items_in_order = OrderItem.objects.filter(order=order)
    order_price = 0
    for item in items_in_order:
        order_price += item.item.price * item.quantity

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': f'Заказ {order.date_created}',
                },
                'unit_amount': order_price*100,  # unit_amount используется в центах
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'http://localhost:8000/success/{session_key}',
        cancel_url='http://localhost:8000/cancel', )

    return redirect(session.url, code=303)
