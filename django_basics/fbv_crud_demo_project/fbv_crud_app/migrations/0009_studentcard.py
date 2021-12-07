# Generated by Django 3.2.8 on 2021-11-28 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fbv_crud_app', '0008_auto_20211128_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCard',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('color', models.CharField(choices=[('r', 'red'), ('b', 'blue')], max_length=1)),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fbv_crud_app.student')),
            ],
        ),
    ]