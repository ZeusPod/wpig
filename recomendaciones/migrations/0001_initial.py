# Generated by Django 4.1.2 on 2022-11-14 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recomendaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipos', models.PositiveBigIntegerField()),
                ('name', models.CharField(max_length=255, null=True, verbose_name='neuominia')),
                ('recomendaciones', models.TextField()),
            ],
            options={
                'verbose_name': 'Recomendacion',
                'verbose_name_plural': 'Recomendaciones',
            },
        ),
    ]