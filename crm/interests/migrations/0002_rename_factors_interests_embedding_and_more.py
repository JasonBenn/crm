# Generated by Django 4.1.2 on 2022-10-31 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interests',
            old_name='factors',
            new_name='embedding',
        ),
        migrations.RemoveField(
            model_name='airtablepersons',
            name='website',
        ),
    ]
