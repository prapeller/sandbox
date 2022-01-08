# Generated by Django 4.0.1 on 2022-01-08 11:31

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=recipes.models.recipe_image_file_path),
        ),
    ]
