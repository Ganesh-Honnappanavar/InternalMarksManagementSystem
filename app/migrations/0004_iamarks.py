# Generated by Django 2.0.7 on 2018-09-10 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='iaMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t1', models.IntegerField()),
                ('t2', models.IntegerField()),
                ('t3', models.IntegerField()),
                ('semIA', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.ClassStudents')),
                ('sub_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Subjects')),
                ('usnIA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Students')),
            ],
        ),
    ]
