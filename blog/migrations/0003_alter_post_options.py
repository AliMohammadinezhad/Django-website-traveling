# Generated by Django 4.2.13 on 2024-05-29 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_counted_view_post_created_datetime_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_datetime']},
        ),
    ]