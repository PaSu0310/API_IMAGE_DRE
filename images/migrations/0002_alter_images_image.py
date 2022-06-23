# Generated by Django 4.0.5 on 2022-06-23 13:31

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to=images.models.user_directory_path),
        ),
    ]
