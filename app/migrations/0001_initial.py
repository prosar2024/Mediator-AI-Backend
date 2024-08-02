# Generated by Django 5.0.6 on 2024-08-02 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation_id', models.UUIDField(unique=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.JSONField(null=True)),
                ('closed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'conversations',
                'db_table': 'conversations',
            },
        ),
        migrations.CreateModel(
            name='ConversationStaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation_id', models.UUIDField(unique=True)),
                ('system_fingerprint', models.UUIDField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.JSONField(null=True)),
            ],
            options={
                'verbose_name': 'conversations_staging',
                'db_table': 'conversations_staging',
            },
        ),
        migrations.CreateModel(
            name='Mediators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediator_id', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_verified', models.BooleanField(default=False)),
                ('email_verified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'mediators',
                'db_table': 'mediators',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.UUIDField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('summary', models.CharField(max_length=4000)),
                ('conversation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.conversations')),
            ],
            options={
                'verbose_name': 'files',
                'db_table': 'files',
            },
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(max_length=20, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('summary', models.CharField(max_length=5000, null=True)),
                ('closed_on', models.DateTimeField(null=True)),
                ('mediator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mediators')),
            ],
            options={
                'verbose_name': 'cases',
                'db_table': 'cases',
            },
        ),
        migrations.CreateModel(
            name='PartiesInvolved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_id', models.CharField(max_length=15, null=True, unique=True)),
                ('role', models.CharField(choices=[('petitioner', 'Petitioner'), ('respondent', 'Respondent'), ('jury', 'Jury')], default='petitioner', max_length=30)),
                ('name', models.CharField(max_length=30, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile_verified', models.BooleanField(default=False)),
                ('email_verified', models.BooleanField(default=False)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cases')),
            ],
            options={
                'verbose_name': 'parties_involved',
                'db_table': 'parties_involved',
            },
        ),
        migrations.AddField(
            model_name='conversations',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.partiesinvolved'),
        ),
    ]
