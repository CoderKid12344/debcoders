# Generated by Django 4.0 on 2021-12-25 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=200)),
                ('desc', models.TextField()),
                ('category', models.CharField(default='No Category', max_length=200)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
