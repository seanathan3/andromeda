# Generated by Django 5.0.6 on 2024-12-28 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='name',
            field=models.CharField(default='name', max_length=30),
        ),
    ]
