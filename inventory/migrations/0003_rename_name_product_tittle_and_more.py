# Generated by Django 4.2.3 on 2023-07-28 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='tittle',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
