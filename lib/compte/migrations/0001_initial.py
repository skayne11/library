# Generated by Django 4.1.7 on 2023-03-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comptes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=500)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]
