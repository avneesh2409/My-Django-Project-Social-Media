# Generated by Django 3.0.6 on 2020-05-10 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0005_auto_20200510_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='slug',
            field=models.SlugField(default='id', max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 10, 9, 10, 55, 725473)),
        ),
    ]
