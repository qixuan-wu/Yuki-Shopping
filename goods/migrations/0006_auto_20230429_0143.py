# Generated by Django 3.2.18 on 2023-04-29 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20230429_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='homedecordetail',
            name='image',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homefurnishingdetail',
            name='image',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]