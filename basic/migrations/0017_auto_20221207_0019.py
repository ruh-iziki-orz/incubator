# Generated by Django 3.2.9 on 2022-12-06 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0016_user_details_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='ratings_count',
            field=models.CharField(default='1', max_length=20000),
        ),
        migrations.AddField(
            model_name='user_details',
            name='ratings_sum',
            field=models.CharField(default='4', max_length=20000),
        ),
    ]
