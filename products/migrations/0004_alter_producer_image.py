# Generated by Django 5.1.3 on 2024-12-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_producer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='image',
            field=models.ImageField(default='images/producers/farmer.jpg', upload_to='images/producers/'),
        ),
    ]