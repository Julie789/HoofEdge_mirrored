# Generated by Django 2.0.5 on 2018-10-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20181020_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('Green', 'Green'), ('Blue', 'Blue'), ('Red', 'Red'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Black', 'Black'), ('White', 'White')], default='green', max_length=20),
        ),
    ]