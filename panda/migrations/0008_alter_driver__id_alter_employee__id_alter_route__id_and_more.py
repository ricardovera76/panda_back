# Generated by Django 4.2.6 on 2023-11-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panda', '0007_route_descr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trainingemployee',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='van',
            name='_id',
            field=models.TextField(default='', primary_key=True, serialize=False),
        ),
    ]
