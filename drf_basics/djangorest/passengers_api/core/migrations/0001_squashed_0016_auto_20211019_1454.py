# Generated by Django 3.2.8 on 2021-10-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('core', '0001_initial'), ('core', '0002_alter_passenger_id'), ('core', '0003_alter_passenger_travel_points'), ('core', '0004_alter_passenger_travel_points'), ('core', '0005_alter_passenger_travel_points'), ('core', '0006_alter_passenger_travel_points'), ('core', '0007_alter_passenger_travel_points'), ('core', '0008_alter_passenger_travel_points'), ('core', '0009_alter_passenger_travel_points'), ('core', '0010_alter_passenger_travel_points'), ('core', '0011_alter_passenger_travel_points'), ('core', '0012_alter_passenger_travel_points'), ('core', '0013_alter_passenger_travel_points'), ('core', '0014_alter_passenger_travel_points'), ('core', '0015_alter_passenger_travel_points'), ('core', '0016_auto_20211019_1454')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('travel_points', models.ManyToManyField(max_length=2, to='core.TravelPoints')),
            ],
        ),
    ]
