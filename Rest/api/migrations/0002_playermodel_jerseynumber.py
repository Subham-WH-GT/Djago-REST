# Generated by Django 5.0.4 on 2024-07-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playermodel',
            name='jerseyNumber',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
    ]