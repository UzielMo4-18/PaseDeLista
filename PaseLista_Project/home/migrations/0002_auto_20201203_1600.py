# Generated by Django 3.1.3 on 2020-12-03 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='id_asistencias',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='id_clases',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='id_materia',
        ),
        migrations.AddField(
            model_name='clase',
            name='id_materia',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='home.materia'),
        ),
        migrations.AddField(
            model_name='materia',
            name='id_profesor',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='home.profesor'),
        ),
    ]
