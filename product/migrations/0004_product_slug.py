# Generated by Django 5.0.7 on 2024-07-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productline_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
