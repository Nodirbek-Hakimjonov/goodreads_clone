# Generated by Django 4.2.3 on 2023-08-31 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='image',
            new_name='profile_picture',
        ),
    ]
