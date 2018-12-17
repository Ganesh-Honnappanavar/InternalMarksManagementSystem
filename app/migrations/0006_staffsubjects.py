# Generated by Django 2.0.7 on 2018-10-03 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181003_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='staffSubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Subjects')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
            ],
        ),
    ]
