# Generated by Django 4.1.2 on 2024-06-29 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(db_column='idCurso', primary_key=True, serialize=False)),
                ('nombre_curso', models.CharField(max_length=100)),
                ('suspendido', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
    ]