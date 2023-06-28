# Generated by Django 3.2.5 on 2021-09-10 08:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pynetsoftwares', '0006_rename_urlstructure_addcourses_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagetitle', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=500)),
                ('pagecontent', ckeditor.fields.RichTextField()),
                ('pageimages', models.ImageField(upload_to='courseimg')),
            ],
        ),
    ]
