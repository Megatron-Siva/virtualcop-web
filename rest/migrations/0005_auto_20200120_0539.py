# Generated by Django 3.0.2 on 2020-01-20 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20200120_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='p2mob',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='information',
            name='pin',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='information',
            name='pmob',
            field=models.CharField(max_length=10),
        ),
    ]