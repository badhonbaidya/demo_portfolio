# Generated by Django 4.2.7 on 2024-01-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_about_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='email',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
