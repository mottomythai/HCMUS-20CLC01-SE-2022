# Generated by Django 4.1.4 on 2023-01-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi5', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
