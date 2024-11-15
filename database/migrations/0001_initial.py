# Generated by Django 5.1.3 on 2024-11-12 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'category',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('author', models.CharField(max_length=50, null=True)),
                ('cover', models.FileField(null=True, upload_to='')),
                ('category', models.ForeignKey(db_column='category_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='database.category')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'book',
                'abstract': False,
            },
        ),
    ]
