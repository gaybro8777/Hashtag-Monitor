# Generated by Django 3.0 on 2019-12-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0018_auto_20191223_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.URLField(blank=True, default=None, max_length=400, null=True, verbose_name='Profile image url'),
        ),
    ]
