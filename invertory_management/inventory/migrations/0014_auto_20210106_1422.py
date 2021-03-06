# Generated by Django 3.1.2 on 2021-01-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20210106_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('OUT OF STOCK', 'Item is out of stock'), ('SOLD', 'Item is Sold'), ('AVAILABLE', 'Item is ready to be purchased')], default='SOLD', max_length=12),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('OUT OF STOCK', 'Item is out of stock'), ('SOLD', 'Item is Sold'), ('AVAILABLE', 'Item is ready to be purchased')], default='SOLD', max_length=12),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('OUT OF STOCK', 'Item is out of stock'), ('SOLD', 'Item is Sold'), ('AVAILABLE', 'Item is ready to be purchased')], default='SOLD', max_length=12),
        ),
    ]
