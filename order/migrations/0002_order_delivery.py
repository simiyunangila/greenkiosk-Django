# Generated by Django 4.2.3 on 2023-07-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.ManyToManyField(to='delivery.delivery'),
        ),
    ]
