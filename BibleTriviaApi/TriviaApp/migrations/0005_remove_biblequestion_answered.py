# Generated by Django 3.1.6 on 2021-04-23 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TriviaApp', '0004_auto_20210405_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biblequestion',
            name='Answered',
        ),
    ]