# Generated by Django 2.0.3 on 2019-02-24 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190224_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=8)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Topping_type')),
            ],
        ),
    ]
