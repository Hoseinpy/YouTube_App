# Generated by Django 5.0.4 on 2024-04-13 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commet',
            new_name='comment',
        ),
    ]
