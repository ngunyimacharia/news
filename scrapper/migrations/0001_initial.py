# Generated by Django 2.1.5 on 2019-01-08 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('cr_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('up_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapper.Country')),
            ],
        ),
    ]
