# Generated by Django 3.2.9 on 2022-12-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0010_income_company_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_details',
            name='vision',
            field=models.TextField(default='noname', max_length=2000),
        ),
    ]
