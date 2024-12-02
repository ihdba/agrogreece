# Generated by Django 5.1.3 on 2024-12-01 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=255)),
                ('image', models.ImageField(default='images/farmer.jpg', upload_to='products/')),
                ('registered', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Producers',
                'ordering': ['-registered'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=255)),
                ('p_desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('p_img', models.ImageField(default='images/olive-oil.jpg', upload_to='images/products/')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producer')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['-published'],
            },
        ),
    ]
