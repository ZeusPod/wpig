# Generated by Django 4.1.2 on 2022-11-17 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=255, verbose_name='descripcion')),
                ('picture', models.ImageField(blank=True, upload_to='animal/')),
                ('establo', models.CharField(max_length=255, verbose_name='establo')),
                ('galpon', models.CharField(max_length=255, verbose_name='galpon')),
                ('raza', models.CharField(max_length=255, verbose_name='raza')),
                ('register_date', models.DateField(auto_now_add=True)),
                ('born_date', models.DateField()),
                ('place_of_birth', models.CharField(max_length=255, verbose_name='lugar de nacimiento')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animals',
            },
        ),
    ]
