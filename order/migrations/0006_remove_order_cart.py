# Generated by Django 4.2.3 on 2023-07-28 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
    ]