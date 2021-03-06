# Generated by Django 2.0.6 on 2021-08-31 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='Fecha de creación')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('last_update', models.DateTimeField(auto_now_add=True, verbose_name='Última actualización')),
            ],
            options={
                'db_table': 'status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('title', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='Fecha de creación')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('last_update', models.DateTimeField(auto_now_add=True, verbose_name='Última actualización')),
            ],
            options={
                'db_table': 'task',
                'managed': False,
            },
        ),
    ]
