# Generated by Django 3.1.2 on 2021-01-06 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('serial', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('SOLD', 'Item is Sold'), ('AVAILABLE', 'Item is ready to be purchased'), ('OUT OF STOCK', 'Item is out of stock')], default='SOLD', max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('SOLD', 'Item is Sold'), ('AVAILABLE', 'Item is ready to be purchased'), ('OUT OF STOCK', 'Item is out of stock')], default='SOLD', max_length=12),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('SOLD', 'Item is Sold'), ('AVAILABLE', 'Item is ready to be purchased'), ('OUT OF STOCK', 'Item is out of stock')], default='SOLD', max_length=12),
        ),
    ]
