# Generated by Django 2.1.5 on 2019-01-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0002_auto_20190108_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='cr_at',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='up_at',
        ),
        migrations.AddField(
            model_name='provider',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
