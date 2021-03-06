# Generated by Django 3.1.2 on 2021-01-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20210106_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item is ready to be purchased'), ('SOLD', 'Item is Sold'), ('OUT OF STOCK', 'Item is out of stock')], default='SOLD', max_length=12),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item is ready to be purchased'), ('SOLD', 'Item is Sold'), ('OUT OF STOCK', 'Item is out of stock')], default='SOLD', max_length=12),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item is ready to be purchased'), ('SOLD', 'Item is Sold'), ('OUT OF STOCK', 'Item is out of stock')], default='SOLD', max_length=12),
        ),
    ]
