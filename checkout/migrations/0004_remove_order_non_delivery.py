# Generated by Django 3.1.1 on 2020-11-02 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_non_delivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='non_delivery',
        ),
    ]
