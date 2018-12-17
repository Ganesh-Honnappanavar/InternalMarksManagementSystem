# Generated by Django 2.0.7 on 2018-09-10 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_classstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('subcode', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=25)),
                ('SEM2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.ClassStudents')),
            ],
        ),
    ]
