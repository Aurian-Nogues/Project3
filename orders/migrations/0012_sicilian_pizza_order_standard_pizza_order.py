# Generated by Django 2.0.3 on 2019-02-24 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_delete_subs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sicilian_pizza_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=8)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Topping_type')),
                ('topping_list', models.ManyToManyField(blank=True, to='orders.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='Standard_pizza_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=8)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Topping_type')),
                ('topping_list', models.ManyToManyField(blank=True, to='orders.Topping')),
            ],
        ),
    ]
