# Generated by Django 4.1.7 on 2023-04-05 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='films',
            old_name='title',
            new_name='titre',
        ),
    ]
