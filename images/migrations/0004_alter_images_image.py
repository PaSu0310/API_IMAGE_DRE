# Generated by Django 4.0.5 on 2022-06-23 13:45

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='posts/default.jpg', max_length=255, upload_to=images.models.user_directory_path),
        ),
    ]
