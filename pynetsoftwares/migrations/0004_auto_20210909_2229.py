# Generated by Django 3.2.5 on 2021-09-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pynetsoftwares', '0003_addcourses_urlstructure'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcourses',
            name='courseimages',
            field=models.ImageField(default='', upload_to='courseimg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addcourses',
            name='cousrecategory',
            field=models.CharField(choices=[('frontends', 'frontends'), ('programming', 'programming'), ('frameworks', 'frameworks'), ('databases', 'databases')], default=' ', max_length=100),
            preserve_default=False,
        ),
    ]