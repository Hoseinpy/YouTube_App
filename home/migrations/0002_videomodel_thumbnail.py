# Generated by Django 5.0.4 on 2024-04-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnails/'),
        ),
    ]
