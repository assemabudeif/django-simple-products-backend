# Generated by Django 5.1 on 2024-08-20 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
