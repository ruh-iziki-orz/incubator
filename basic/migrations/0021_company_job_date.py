# Generated by Django 3.2.9 on 2022-12-10 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0020_auto_20221211_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_job',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]