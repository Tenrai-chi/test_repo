# Generated by Django 4.2.10 on 2024-02-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0004_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID сессии'),
        ),
    ]