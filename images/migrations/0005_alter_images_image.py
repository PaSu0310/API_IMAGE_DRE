# Generated by Django 4.0.5 on 2022-06-23 13:45

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to=images.models.user_directory_path),
        ),
    ]