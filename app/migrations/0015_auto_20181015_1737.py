# Generated by Django 2.0.7 on 2018-10-15 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20181015_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffsubjects',
            name='Subjects',
        ),
        migrations.RemoveField(
            model_name='staffsubjects',
            name='staff',
        ),
        migrations.DeleteModel(
            name='staffSubjects',
        ),
    ]
