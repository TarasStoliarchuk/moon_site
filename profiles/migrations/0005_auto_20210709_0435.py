# Generated by Django 3.1.7 on 2021-07-09 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20210705_0326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='bb',
            new_name='post',
        ),
    ]