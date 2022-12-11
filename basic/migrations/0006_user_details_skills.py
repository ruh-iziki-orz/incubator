# Generated by Django 3.2.9 on 2022-12-05 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_auto_20221205_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=200)),
                ('skills_rate', models.CharField(max_length=200)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.user_details')),
            ],
        ),
    ]
