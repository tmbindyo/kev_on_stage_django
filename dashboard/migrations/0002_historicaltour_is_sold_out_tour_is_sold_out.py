# Generated by Django 4.2.7 on 2024-02-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltour',
            name='is_sold_out',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tour',
            name='is_sold_out',
            field=models.BooleanField(default=False),
        ),
    ]
