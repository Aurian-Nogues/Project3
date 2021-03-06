# Generated by Django 2.0.3 on 2019-02-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_sicilian_pizza_order_standard_pizza_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sicilian_pizza_order',
            name='size',
        ),
        migrations.RemoveField(
            model_name='sicilian_pizza_order',
            name='topping',
        ),
        migrations.RemoveField(
            model_name='sicilian_pizza_order',
            name='topping_list',
        ),
        migrations.RemoveField(
            model_name='standard_pizza_order',
            name='size',
        ),
        migrations.RemoveField(
            model_name='standard_pizza_order',
            name='topping',
        ),
        migrations.RemoveField(
            model_name='standard_pizza_order',
            name='topping_list',
        ),
        migrations.RenameField(
            model_name='sicilian_pizza',
            old_name='price',
            new_name='price_large',
        ),
        migrations.RenameField(
            model_name='standard_pizza',
            old_name='price',
            new_name='price_large',
        ),
        migrations.AddField(
            model_name='sicilian_pizza',
            name='price_small',
            field=models.FloatField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='standard_pizza',
            name='price_small',
            field=models.FloatField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Sicilian_pizza_order',
        ),
        migrations.DeleteModel(
            name='Standard_pizza_order',
        ),
    ]
