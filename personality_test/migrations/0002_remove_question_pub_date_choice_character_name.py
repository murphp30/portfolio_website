# Generated by Django 5.0.1 on 2024-01-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality_test', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='choice',
            name='character_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
