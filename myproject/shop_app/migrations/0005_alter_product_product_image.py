# Generated by Django 5.0.1 on 2024-02-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, default='Add image', upload_to='images/'),
        ),
    ]
