# Generated by Django 5.1.2 on 2024-10-12 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='status_profile',
            new_name='status',
        ),
    ]
