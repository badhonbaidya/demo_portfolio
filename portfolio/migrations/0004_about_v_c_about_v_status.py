# Generated by Django 4.2.7 on 2024-01-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_name_about_u_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='v_c',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='v_status',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
