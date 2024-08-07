# Generated by Django 5.0.6 on 2024-08-07 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='name',
        ),
        migrations.RemoveField(
            model_name='files',
            name='summary',
        ),
        migrations.AddField(
            model_name='files',
            name='actual_file_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='files',
            name='description',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='files',
            name='unique_file_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='FilesStaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.UUIDField(unique=True)),
                ('unique_file_name', models.CharField(max_length=200, null=True)),
                ('actual_file_name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=4000, null=True)),
                ('conversation_staging', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.conversationstaging')),
            ],
            options={
                'verbose_name': 'files_staging',
                'db_table': 'files_staging',
            },
        ),
    ]
