# Generated by Django 3.2.8 on 2022-02-27 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0005_alter_sellerdetail_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerdetail',
            name='photo',
            field=models.ImageField(default='User_photos/default.png', upload_to='User_photos'),
        ),
    ]
