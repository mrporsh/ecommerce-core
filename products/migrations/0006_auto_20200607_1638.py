# Generated by Django 3.0.7 on 2020-06-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_item_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(),
        ),
    ]
