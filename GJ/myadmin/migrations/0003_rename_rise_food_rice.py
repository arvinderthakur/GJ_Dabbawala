# Generated by Django 5.0.3 on 2024-04-19 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_profile_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='rise',
            new_name='rice',
        ),
    ]
