# Generated by Django 4.2.13 on 2024-06-12 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/default.jpg', upload_to='blog/'),
        ),
    ]
