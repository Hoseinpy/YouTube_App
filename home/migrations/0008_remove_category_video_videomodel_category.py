# Generated by Django 5.0.4 on 2024-04-13 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='video',
        ),
        migrations.AddField(
            model_name='videomodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.category'),
        ),
    ]
