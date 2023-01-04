# Generated by Django 4.1.4 on 2023-01-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi5', '0008_remove_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='productdetail',
            name='itemno',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]