# Generated by Django 3.1.7 on 2021-02-22 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webtheme',
            old_name='avatar',
            new_name='image',
        ),
    ]
