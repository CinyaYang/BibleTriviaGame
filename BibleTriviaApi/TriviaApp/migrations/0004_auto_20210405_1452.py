# Generated by Django 3.1.6 on 2021-04-05 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TriviaApp', '0003_auto_20210405_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questioninfo',
            name='Answered',
        ),
        migrations.AddField(
            model_name='biblequestion',
            name='Answered',
            field=models.BooleanField(default=False),
        ),
    ]
