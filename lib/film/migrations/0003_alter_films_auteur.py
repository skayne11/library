# Generated by Django 4.1.7 on 2023-04-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_rename_title_films_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='auteur',
            field=models.CharField(max_length=250),
        ),
    ]