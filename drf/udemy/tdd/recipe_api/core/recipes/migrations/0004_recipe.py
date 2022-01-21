# Generated by Django 4.0 on 2022-01-07 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_name'),
        ('recipes', '0003_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time_minutes', models.DecimalField(decimal_places=1, max_digits=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
                ('tags', models.ManyToManyField(to='recipes.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]