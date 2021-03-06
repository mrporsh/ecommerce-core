# Generated by Django 3.0.7 on 2020-06-07 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20200606_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['title'], 'verbose_name_plural': 'Sub Categories'},
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Item')),
                ('last_edited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('item', 'name')},
            },
        ),
        migrations.CreateModel(
            name='ItemVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('attachment', models.ImageField(blank=True, null=True, upload_to='')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now=True)),
                ('last_edited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Variation')),
            ],
            options={
                'unique_together': {('variation', 'value')},
            },
        ),
    ]
