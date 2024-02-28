from django.db import models


class Item(models.Model):
    """ Товары
    """

    name = models.CharField(max_length=50, verbose_name='Товар')
    description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена', help_text='Указывается цена в центах')
    #currency = models.CharField(max_length=3, blank=True, null=True, verbose_name='Валюта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    """ Заказы
    """

    session_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='ID сессии')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    paid = models.BooleanField(default=False, verbose_name='Статус оплаты')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ от {self.date_created}'


class OrderItem(models.Model):
    """ Список товаров в заказах
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    item = models.ForeignKey(Item, on_delete=models.SET_DEFAULT, default=None, related_name='order_items', verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return f'Заказ {self.id}'
