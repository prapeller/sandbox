# Generated by Django 2.1.7 on 2019-02-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190215_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(auto_created=True, default='djangodbmodelsfieldscharfield', max_length=200, unique=True),
        ),
    ]