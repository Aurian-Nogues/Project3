# Generated by Django 2.0.3 on 2019-02-24 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190224_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standard_pizza',
            name='size',
        ),
        migrations.RemoveField(
            model_name='standard_pizza',
            name='topping',
        ),
        migrations.DeleteModel(
            name='Standard_pizza',
        ),
    ]
