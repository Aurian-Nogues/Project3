# Generated by Django 2.0.3 on 2019-02-24 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190224_1810'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pizza',
            new_name='Standard_pizza',
        ),
    ]
