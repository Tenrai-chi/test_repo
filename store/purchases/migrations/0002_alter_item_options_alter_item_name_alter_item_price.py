# Generated by Django 4.2.10 on 2024-02-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
    ]
