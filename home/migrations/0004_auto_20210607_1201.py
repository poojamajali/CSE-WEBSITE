# Generated by Django 3.2.3 on 2021-06-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_achievements'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='news',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]