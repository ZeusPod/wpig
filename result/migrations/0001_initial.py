# Generated by Django 4.1.2 on 2022-11-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_id', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('name_foto', models.CharField(max_length=255)),
                ('establo', models.CharField(max_length=255)),
                ('galpon', models.CharField(max_length=255)),
                ('raza', models.CharField(max_length=255)),
                ('register_date', models.CharField(max_length=255)),
                ('born_date', models.CharField(max_length=255)),
                ('place_of_birth', models.CharField(max_length=255)),
                ('resultado', models.CharField(max_length=255)),
                ('sintomas', models.TextField()),
                ('recomendaciones', models.TextField()),
                ('result_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Resultado',
                'verbose_name_plural': 'Resultados',
            },
        ),
    ]
