# Generated by Django 5.0.7 on 2024-09-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(),
        ),
    ]
