# Generated by Django 4.2.7 on 2024-01-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_about_date_time_alter_about_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='date_time',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='about',
            name='email',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='about',
            name='no_digital_awards',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='about',
            name='no_exp',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='about',
            name='no_happy_customers',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='about',
            name='no_project_finished',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='about',
            name='v_c',
            field=models.CharField(max_length=5000),
        ),
    ]
