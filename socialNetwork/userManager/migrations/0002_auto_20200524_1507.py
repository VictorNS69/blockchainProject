# Generated by Django 3.0.5 on 2020-05-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='bytes',
            field=models.CharField(max_length=66),
        ),
    ]