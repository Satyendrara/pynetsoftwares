# Generated by Django 3.2.5 on 2021-09-09 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pynetsoftwares', '0004_auto_20210909_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addcourses',
            old_name='cousrecategory',
            new_name='coursecategory',
        ),
    ]