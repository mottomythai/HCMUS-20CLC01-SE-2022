# Generated by Django 4.1.3 on 2023-01-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hi5", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="size",
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]
