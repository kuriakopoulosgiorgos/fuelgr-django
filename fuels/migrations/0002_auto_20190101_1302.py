# Generated by Django 2.1.4 on 2019-01-01 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuels', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gasstation',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='pricedata',
            options={'managed': False},
        ),
    ]
