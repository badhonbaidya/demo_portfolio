# Generated by Django 4.2.7 on 2024-01-22 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_rename_v_c_about_vf_c_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='vf_c',
            new_name='v_c',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='vf_status',
            new_name='v_status',
        ),
    ]