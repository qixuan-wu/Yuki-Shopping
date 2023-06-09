# Generated by Django 4.1.2 on 2023-04-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeDecor',
            fields=[
                ('rank', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('ratings', models.TextField()),
                ('price', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeFurnishing',
            fields=[
                ('rank', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('ratings', models.TextField()),
                ('price', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeImprovement',
            fields=[
                ('rank', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('ratings', models.TextField()),
                ('price', models.TextField()),
            ],
        ),
    ]
