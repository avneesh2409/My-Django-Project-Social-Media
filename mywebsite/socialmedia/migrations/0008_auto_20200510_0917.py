# Generated by Django 3.0.6 on 2020-05-10 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0007_auto_20200510_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='slug',
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 10, 9, 17, 53, 863198)),
        ),
    ]