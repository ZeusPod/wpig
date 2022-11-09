# Generated by Django 4.1.2 on 2022-11-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sintomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipos', models.PositiveIntegerField()),
                ('sintomas', models.TextField()),
            ],
            options={
                'verbose_name': 'Sintoma',
                'verbose_name_plural': 'Sintomas',
            },
        ),
    ]