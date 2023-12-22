# Generated by Django 4.2.6 on 2023-10-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='geo_loc',
        ),
        migrations.RemoveField(
            model_name='trainingemployee',
            name='geo_loc',
        ),
        migrations.AddField(
            model_name='driver',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='trainingemployee',
            name='address',
            field=models.TextField(default=''),
        ),
    ]
