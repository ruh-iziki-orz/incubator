# Generated by Django 3.2.9 on 2022-12-05 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0007_user_details_work_employer'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_duration', models.TextField(max_length=2000)),
                ('link', models.TextField(max_length=2000)),
                ('project_describe', models.TextField(max_length=2000)),
                ('project_name', models.TextField(default='NA', max_length=2000)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.user_details')),
            ],
        ),
    ]
