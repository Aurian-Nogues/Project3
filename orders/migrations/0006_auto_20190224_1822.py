# Generated by Django 2.0.3 on 2019-02-24 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190224_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sicilian_pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=8)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Topping_type')),
            ],
        ),
        migrations.RemoveField(
            model_name='standard_pizza',
            name='flavour',
        ),
        migrations.AlterField(
            model_name='standard_pizza',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AlterField(
            model_name='standard_pizza',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Topping_type'),
        ),
        migrations.DeleteModel(
            name='Flavour',
        ),
    ]
