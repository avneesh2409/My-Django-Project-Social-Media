# Generated by Django 3.0.6 on 2020-05-10 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('education', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
    ]